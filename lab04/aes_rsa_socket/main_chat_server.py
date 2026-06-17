import sys, socket, threading
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PyQt5 import QtWidgets, QtCore
from ui.chat_server_ui import Ui_MainWindow


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(message.encode(), AES.block_size))


def decrypt_message(key, data):
    iv, ct = data[:16], data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    log_signal = QtCore.pyqtSignal(str)
    status_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.log_signal.connect(self.txtLog.append)
        self.status_signal.connect(self.lblStatus.setText)

        self.clients = []
        self.btnStart.clicked.connect(self.start_server)

    def start_server(self):
        self.btnStart.setEnabled(False)
        self.server_key = RSA.generate(2048)
        threading.Thread(target=self.run_server, daemon=True).start()
        self.status_signal.emit("Status: Running on port 12345")
        self.log_signal.emit("Server started on port 12345...")

    def run_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 12345))
        s.listen(5)
        while True:
            client_socket, addr = s.accept()
            self.log_signal.emit(f"Client connected: {addr}")
            threading.Thread(
                target=self.handle_client, args=(client_socket, addr), daemon=True
            ).start()

    def handle_client(self, client_socket, addr):
        client_socket.send(self.server_key.publickey().export_key())
        client_pub = RSA.import_key(client_socket.recv(2048))

        aes_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(client_pub)
        client_socket.send(cipher_rsa.encrypt(aes_key))

        self.clients.append((client_socket, aes_key))

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            msg = decrypt_message(aes_key, data)
            self.log_signal.emit(f"[{addr}] {msg}")

            for c, k in self.clients:
                if c != client_socket:
                    c.send(encrypt_message(k, msg))

            if msg == "exit":
                break

        self.clients.remove((client_socket, aes_key))
        client_socket.close()
        self.log_signal.emit(f"Connection {addr} closed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())