from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for ch in text:
            if ch in self.alphabet:
                letter_index = self.alphabet.index(ch)
                output_index = (letter_index + key) % alphabet_len
                encrypted_text.append(self.alphabet[output_index])
            else:
                encrypted_text.append(ch)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for ch in text:
            if ch in self.alphabet:
                letter_index = self.alphabet.index(ch)
                output_index = (letter_index - key) % alphabet_len
                decrypted_text.append(self.alphabet[output_index])
            else:
                decrypted_text.append(ch)
        return "".join(decrypted_text)
