import requests

data = {
    "username": "testaccount",
    "password": "testaccount24"
}

add_password = requests.post(
    url='http://127.0.0.1:5000/passwords/add',
    json=data
)

print("Add a password :", add_password.json())

get_passwords = requests.get(
    url='http://127.0.0.1:5000/passwords'
)

print()
print("Records")
print(get_passwords.json())