class PlayfairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        matrix_chars = []
        for char in key:
            if char not in matrix_chars and char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
                matrix_chars.append(char)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in matrix_chars:
                matrix_chars.append(char)
                
        playfair_matrix = [matrix_chars[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1 

    # --- HÀM MỚI TỪ ẢNH CỦA BẠN ---
    def split_pairs(self, text):
        text = text.upper().replace('J', 'I').replace(' ', '')
        # Bộ lọc an toàn đảm bảo không có ký tự lạ lọt vào
        text = "".join([c for c in text if c in "ABCDEFGHIKLMNOPQRSTUVWXYZ"])
        pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i+1]
                if a == b:
                    pairs.append(a + 'X')
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + 'X')
                i += 1
        return pairs
                
    def playfair_encrypt(self, plain_text, matrix):
        # SỬ DỤNG HÀM TÁCH CẶP VỪA TẠO
        pairs = self.split_pairs(plain_text)
        encrypted_text = ""
        
        for pair in pairs:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == -1 or row2 == -1:
                continue

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        cipher_text = "".join([c for c in cipher_text if c in "ABCDEFGHIKLMNOPQRSTUVWXYZ"])
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            if len(pair) < 2:
                break
                
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == -1 or row2 == -1:
                continue
                
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        banro = ""
        for i in range(0, len(decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + "" + decrypted_text[i+1]
                
        if len(decrypted_text) >= 2:
            if decrypted_text[-1] == "X":
                banro += decrypted_text[-2]
            else:
                banro += decrypted_text[-2]
                banro += decrypted_text[-1]
            
        return banro