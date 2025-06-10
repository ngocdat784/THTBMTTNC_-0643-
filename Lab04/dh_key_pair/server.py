from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# ----------------------------------------
# 1. Tạo tham số Diffie-Hellman (prime + generator)
# ----------------------------------------
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

# ----------------------------------------
# 2. Sinh cặp khóa DH từ tham số
# ----------------------------------------
def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# ----------------------------------------
# 3. Chạy chính
# ----------------------------------------
def main():
    # Sinh tham số và cặp khóa
    parameters = generate_dh_parameters()
    private_key, public_key = generate_server_key_pair(parameters)

    # Lưu public key vào file
    with open("server_public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("✅ Đã tạo và lưu public key của server vào server_public_key.pem")

# ----------------------------------------
# 4. Gọi main nếu chạy trực tiếp
# ----------------------------------------
if __name__ == '__main__':
    main()
