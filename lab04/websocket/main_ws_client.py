import sys, asyncio, threading
import tornado.websocket
from PyQt5 import QtWidgets, QtCore
from ui.ws_client_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    log_signal = QtCore.pyqtSignal(str)
    status_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.log_signal.connect(self.txtLog.append)
        self.status_signal.connect(self.lblStatus.setText)

        self.conn = None
        self.loop = asyncio.new_event_loop()
        self.btnSend.setEnabled(False)

        self.btnSend.clicked.connect(self.send_message)

        threading.Thread(target=self.start_loop, daemon=True).start()

    def start_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.connect_ws())
        self.loop.run_forever()

    async def connect_ws(self):
        try:
            self.conn = await tornado.websocket.websocket_connect(
                "ws://localhost:8888/ws"
            )
            self.status_signal.emit("Đã kết nối")
            self.btnSend.setEnabled(True)
            asyncio.create_task(self.listen())
        except Exception as e:
            self.status_signal.emit("Lỗi kết nối")
            self.log_signal.emit(f"Connect error: {e}")

    async def listen(self):
        while True:
            msg = await self.conn.read_message()
            if msg is None:
                self.status_signal.emit("Mất kết nối")
                break
            self.log_signal.emit("Server: " + msg)

    def send_message(self):
        msg = self.txtMessage.text()
        if not msg:
            return
        
        # Đã sửa thành call_soon_threadsafe để tương thích với asyncio loop
        self.loop.call_soon_threadsafe(self.conn.write_message, msg)
        
        self.log_signal.emit("Sent: " + msg)
        self.txtMessage.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())