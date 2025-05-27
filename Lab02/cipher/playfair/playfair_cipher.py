class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = list(key)

        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)
                key_set.add(letter)
            if len(matrix) == 25:
                break

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1  # Trường hợp không tìm thấy

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""
        i = 0

        while i < len(plain_text):
            char1 = plain_text[i]
            if i + 1 < len(plain_text):
                char2 = plain_text[i + 1]
                if char1 == char2:
                    char2 = "X"
                    i += 1
                else:
                    i += 2
            else:
                char2 = "X"
                i += 1

            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            char1, char2 = cipher_text[i], cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text


def clean_decrypted_text(decrypted_text):
    banro = ""
    # Loại bỏ ký tự 'X' nếu nó là ký tự chèn giữa hai ký tự giống nhau
    for i in range(0, len(decrypted_text) - 2, 2):
        if decrypted_text[i] == decrypted_text[i + 2]:
            banro += decrypted_text[i]
        else:
            banro += decrypted_text[i] + decrypted_text[i + 1]

    # Xử lý hai ký tự cuối cùng
    if decrypted_text[-1] == "X":
        banro += decrypted_text[-2]
    else:
        banro += decrypted_text[-2] + decrypted_text[-1]

    return banro
