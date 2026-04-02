import re

common_passwords = ["123456", "password", "12345678", "qwerty", "Abc123"]

while True:
    password = input("Enter your password (or 'exit' to quit): ")
    if password.lower() == 'exit':
        break

    if password in common_passwords:
        print("Very Weak Password (common password)")
    else:
        strength = 0

        if len(password) >= 8:
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[a-z]", password):
            strength += 1
        if re.search(r"[0-9]", password):
            strength += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            strength += 1

        if strength <= 2:
            print("Weak Password")
        elif strength <= 4:
            print("Medium Password")
        else:
            print("Strong Password")
    print()

    #http://127.0.0.1:5000