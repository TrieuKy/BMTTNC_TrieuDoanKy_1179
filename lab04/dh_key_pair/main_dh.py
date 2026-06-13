import sys
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from PyQt5 import QtWidgets
from ui.dh_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.server_priv = None
        self.server_pub = None

        self.btnGenClient.setEnabled(False)

        self.btnGenServer.clicked.connect(self.gen_server)
        self.btnGenClient.clicked.connect(self.gen_client)

    def gen_server(self):
        parameters = dh.generate_parameters(generator=2, key_size=2048)
        self.server_priv = parameters.generate_private_key()
        self.server_pub = self.server_priv.public_key()

        pem = self.server_pub.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        self.txtServerPub.setPlainText(pem.decode())
        self.txtServerShared.clear()
        self.txtClientShared.clear()
        self.lblStatus.setText("")

        self.btnGenClient.setEnabled(True)

    def gen_client(self):
        parameters = self.server_pub.parameters()
        client_priv = parameters.generate_private_key()
        client_pub = client_priv.public_key()

        client_shared = client_priv.exchange(self.server_pub)
        server_shared = self.server_priv.exchange(client_pub)

        self.txtClientShared.setPlainText(client_shared.hex())
        self.txtServerShared.setPlainText(server_shared.hex())

        if client_shared == server_shared:
            self.lblStatus.setText("Shared secret khớp")
        else:
            self.lblStatus.setText("Không khớp")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())