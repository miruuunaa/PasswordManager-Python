from encryption import encrypt_password

def save_password(service, username, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.txt", "a") as file:
        file.write(f"{service} | {username} | {encrypted_password}\n")
    print("Parola a fost salvată cu succes!")

if __name__ == "__main__":
    save_password("Facebook", "user123", "parolaMea123")
