from flask import Flask, jsonify, request, render_template
import uuid

# Create a flask app
app = Flask(__name__)

# File where i want to store the password
# FILE_PATH = 'passwords.bin'

# plain json approach

passwords = {
    "1": {"username": "John", "password": "John24"},
    "2": {"username": "Jane", "password": "Jane24"}
}

# Define endpoints

# get all records
@app.route('/passwords', methods=['GET'])
def get_passwords():
    return jsonify(passwords)

# get password
@app.route('/passwords/<string:id>', methods=['GET'])
def get_password(id):
    if id in passwords:
        return jsonify(passwords[id])
    return jsonify({"error": "Password not found."})

# add password
@app.route('/passwords/add', methods=['POST'])
def add_password():
    data = request.json
    id = str(uuid.uuid4())
    passwords[id] = {"username": data["username"], "password": data["password"]}
    return jsonify({"id": id})


if __name__ == "__main__":
    app.run(debug=True)