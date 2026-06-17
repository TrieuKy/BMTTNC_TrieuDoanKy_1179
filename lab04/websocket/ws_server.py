import tornado.ioloop, tornado.web, tornado.websocket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

AES_KEY = get_random_bytes(16)  # khoá cố định khi demo

def encrypt_aes(plaintext: str) -> str:
    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    ct = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct).decode()

class EchoHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Client connected")

    def on_message(self, message):
        encrypted = encrypt_aes(message)
        print(f"Received: {message} -> Sent encrypted: {encrypted}")
        self.write_message(encrypted)

    def on_close(self):
        print("Client disconnected")

def main():
    app = tornado.web.Application([(r"/ws", EchoHandler)])
    app.listen(8888)
    print("Server listening on ws://localhost:8888/ws")
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()