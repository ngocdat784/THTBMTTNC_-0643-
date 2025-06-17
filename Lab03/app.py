from flask import Flask, render_template, redirect
import subprocess
import sys
import os

app = Flask(__name__)

# Hàm mở file form GUI bằng subprocess
def open_form(script_name):
    path = os.path.abspath(script_name)
    subprocess.Popen([sys.executable, path])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    open_form("ceasar_cipher.py")
    return redirect("/")

@app.route("/vigenere")
def vigenere():
    open_form("vigenere_cipher.py")
    return redirect("/")

@app.route("/railfence")
def railfence():
    open_form("railfence_cipher.py")
    return redirect("/")

@app.route("/playfair")
def playfair():
    open_form("playfair_cipher.py")
    return redirect("/")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)