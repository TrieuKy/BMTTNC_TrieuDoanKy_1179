import sys, socket, threading
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from PyQt5 import QtWidgets, QtCore
from ui.chat_client_ui import Ui_MainWindow


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
        self.status_signal.connect(self.lblStatus_2.setText)

        self.sock = None
        self.aes_key = None
        self.btnSend.setEnabled(False)

        self.btnConnect.clicked.connect(self.connect_server)
        self.btnSend.clicked.connect(self.send_message)

    def connect_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 12345))

        client_key = RSA.generate(2048)
        server_pub = RSA.import_key(self.sock.recv(2048))
        self.sock.send(client_key.publickey().export_key())

        encrypted_aes_key = self.sock.recv(2048)
        cipher_rsa = PKCS1_OAEP.new(client_key)
        self.aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        self.status_signal.emit("Status: Connected")
        self.log_signal.emit("Connected & key exchanged.")
        self.btnSend.setEnabled(True)
        self.btnConnect.setEnabled(False)

        threading.Thread(target=self.receive_loop, daemon=True).start()

    def receive_loop(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            msg = decrypt_message(self.aes_key, data)
            self.log_signal.emit("Received: " + msg)

    def send_message(self):
        msg = self.txtMessage.text()
        if not msg:
            return
        self.sock.send(encrypt_message(self.aes_key, msg))
        self.log_signal.emit("Sent: " + msg)
        self.txtMessage.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())