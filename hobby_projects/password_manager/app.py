from flask import Flask, jsonify, request, render_template
import uuid
import json

# Create a flask app
app = Flask(__name__)

# File where i want to store the password
PASSWORD_FILE = '/Users/shrilc/IdeaProjects/shrilc/batch2/hobby_projects/secrets/test_passwords.json'

# # plain json approach
#
# passwords = {
#     "1": {"username": "John", "password": "John24"},
#     "2": {"username": "Jane", "password": "Jane24"}
# }


def read_passwords():
    with open(PASSWORD_FILE, 'r') as f:
        return json.load(f)


def write_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)


# Define endpoints

# get all records
@app.route('/passwords', methods=['GET'])
def get_passwords():
    passwords = read_passwords()
    return jsonify(passwords)

# get password
@app.route('/passwords/<string:id>', methods=['GET'])
def get_password(id):
    passwords = read_passwords()
    if id in passwords:
        return jsonify(passwords[id])
    return jsonify({"error": "Password not found."})

# add password
@app.route('/passwords/add', methods=['POST'])
def add_password():
    passwords = read_passwords()
    data = request.json
    id = str(uuid.uuid4())
    passwords[id] = {"username": data["username"], "password": data["password"]}
    write_passwords(passwords)
    return jsonify({"id": id})


# update password
@app.route('/passwords/update/<string:id>', methods=['PUT'])
def update_password(id):
    passwords = read_passwords()
    if id in passwords:
        data = request.json
        passwords[id]['username'] = data['username']
        passwords[id]['password'] = data['password']
        write_passwords(passwords)
        return jsonify({"message": "Records updated"})
    else:
        return jsonify({"error": "Password record not found"})


# delete password
@app.route('/passwords/delete/<string:id>', methods=['DELETE'])
def delete_password(id):
    passwords = read_passwords()
    if id in passwords:
        del passwords[id]
        write_passwords(passwords)
        return jsonify({"message": "Records deleted"})
    else:
        return jsonify({"error": "Password record not found"})


if __name__ == "__main__":
    app.run(debug=True)
