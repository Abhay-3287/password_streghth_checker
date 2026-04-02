from flask import Flask, render_template, request
import re

app = Flask(__name__)
count = 0

common_passwords = ["123456", "password", "12345678", "qwerty"]

def check_password(password):
    if password in common_passwords:
        return "Very Weak Password (common password)"

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
        return "Weak Password"
    elif strength <= 4:
        return "Medium Password"
    else:
        return "Strong Password"

@app.route("/", methods=["GET", "POST"])
def home():
    global count
    result = ""

    if request.method == "POST":
        password = request.form["password"]
        result = check_password(password)
        count += 1
        with open("password_stats.txt", "a") as f:
            f.write(f"Length:{len(password)}, Strength:{result}\n")



    return render_template("index.html", result=result, count=count)

if __name__ == "__main__":
    app.run(debug=True)