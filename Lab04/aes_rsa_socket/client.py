from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

# ----------------------------------------
# 1. Kết nối tới server
# ----------------------------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# ----------------------------------------
# 2. Tạo cặp khóa RSA cho client
# ----------------------------------------
client_key = RSA.generate(2048)

# Nhận public key từ server
server_public_key = RSA.import_key(client_socket.recv(2048))

# Gửi public key của client cho server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# ----------------------------------------
# 3. Nhận và giải mã khóa AES từ server
# ----------------------------------------
encrypted_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# ----------------------------------------
# 4. Hàm mã hóa & giải mã tin nhắn bằng AES
# ----------------------------------------
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# ----------------------------------------
# 5. Nhận tin nhắn từ server (thread riêng)
# ----------------------------------------
def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print("📩 Nhận: ", decrypted_message)
        except Exception as e:
            print("⚠️ Lỗi khi nhận tin nhắn:", e)
            break

# Khởi động luồng nhận tin nhắn
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# ----------------------------------------
# 6. Gửi tin nhắn từ client tới server
# ----------------------------------------
try:
    while True:
        message = input("📝 Nhập tin nhắn ('exit' để thoát): ")
        encrypted_message = encrypt_message(aes_key, message)
        client_socket.send(encrypted_message)

        if message.strip().lower() == "exit":
            break
except Exception as e:
    print("⚠️ Lỗi khi gửi tin nhắn:", e)
finally:
    client_socket.close()
    print("🔒 Đã đóng kết nối.")
