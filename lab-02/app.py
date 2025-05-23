from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    result = f"Encrypted text: {encrypted_text}"
    return render_template('caesar.html', result=result, inputPlainText=text, inputKeyPlain=key)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    result = f"Decrypted text: {decrypted_text}"
    return render_template('caesar.html', result=result, inputCipherText=text, inputKeyCipher=key)

#router routes for playfair cypher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    result = f"Encrypted text: {encrypted_text}"
    return render_template('playfair.html', result=result, inputPlainText=text, inputKeyPlain=key)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    result = f"Decrypted text: {decrypted_text}"
    return render_template('playfair.html', result=result, inputCipherText=text, inputKeyCipher=key)

#router routes for railfence cypher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    if key <= 1 or key >= len(text):
        return render_template('railfence.html', result="Key phải lớn hơn 1 và nhỏ hơn độ dài chuỗi!", inputPlainText=text, inputKeyPlain=key)
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    result = f"Encrypted text: {encrypted_text}"
    return render_template('railfence.html', result=result, inputPlainText=text, inputKeyPlain=key)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    if key <= 1 or key >= len(text):
        return render_template('railfence.html', result="Key phải lớn hơn 1 và nhỏ hơn độ dài chuỗi!", inputCipherText=text, inputKeyCipher=key)
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    result = f"Decrypted text: {decrypted_text}"
    return render_template('railfence.html', result=result, inputCipherText=text, inputKeyCipher=key)

#router routes for transposition cypher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    if key <= 1 or key >= len(text):
        return render_template('transposition.html', result="Key phải lớn hơn 1 và nhỏ hơn độ dài chuỗi!", inputPlainText=text, inputKeyPlain=key)
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    result = f"Encrypted text: {encrypted_text}"
    return render_template('transposition.html', result=result, inputPlainText=text, inputKeyPlain=key)

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    if key <= 1 or key >= len(text):
        return render_template('transposition.html', result="Key phải lớn hơn 1 và nhỏ hơn độ dài chuỗi!", inputCipherText=text, inputKeyCipher=key)
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    result = f"Decrypted text: {decrypted_text}"
    return render_template('transposition.html', result=result, inputCipherText=text, inputKeyCipher=key)

#router routes for vigenere cypher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    if not key.isalpha():
        return render_template('vigenere.html', result="Key phải là chuỗi ký tự không dấu, không rỗng!", inputPlainText=text, inputKeyPlain=key)
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    result = f"Encrypted text: {encrypted_text}"
    return render_template('vigenere.html', result=result, inputPlainText=text, inputKeyPlain=key)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    if not key.isalpha():
        return render_template('vigenere.html', result="Key phải là chuỗi ký tự không dấu, không rỗng!", inputCipherText=text, inputKeyCipher=key)
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    result = f"Decrypted text: {decrypted_text}"
    return render_template('vigenere.html', result=result, inputCipherText=text, inputKeyCipher=key)

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)