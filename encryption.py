import hashlib

def encrypt_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

if __name__ == "__main__":
    parola = input("Introdu parola: ")
    print("Parola criptată:", encrypt_password(parola))
