import sys
import hashlib
from Crypto.Hash import SHA3_256
from PyQt5 import QtWidgets
from ui.hash_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnHash.clicked.connect(self.on_hash)

    def on_hash(self):
        text = self.txtInput.toPlainText().encode("utf-8")
        algo = self.cboAlgo.currentText()

        if algo == "MD5":
            result = hashlib.md5(text).hexdigest()
        elif algo == "SHA-256":
            result = hashlib.sha256(text).hexdigest()
        elif algo == "SHA-3":
            result = SHA3_256.new(text).hexdigest()
        elif algo == "BLAKE2":
            result = hashlib.blake2b(text, digest_size=64).hexdigest()
        else:
            result = ""

        self.txtOutput.setText(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())