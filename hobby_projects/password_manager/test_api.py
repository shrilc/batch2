import requests


def test_get_passwords():
    response = requests.get(
        url='http://127.0.0.1:5000/passwords'
    )
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"message": str(e)}


def test_add_password(data):
    response = requests.post(
        url='http://127.0.0.1:5000/passwords/add',
        json=data
    )
    return response.json()


def test_update_password(id, data):
    response = requests.put(
        url=f'http://127.0.0.1:5000/passwords/update/{id}',
        json=data
    )
    return response.json()


def test_delete_password(id):
    response = requests.delete(
        url=f'http://127.0.0.1:5000/passwords/delete/{id}'
    )
    return response.json()


def workflow():
    data = {
        "username": "testaccount",
        "password": "testaccount24"
    }

    # Test get all passwords
    get_all_passwords = test_get_passwords()
    print(get_all_passwords)

    # Test add a password
    add_a_password = test_add_password(data)
    print(add_a_password['id'])

    print(test_get_passwords())

    # Test update a password record
    data = {
        "username": "testaccount",
        "password": "testaccount2424"
    }
    update_a_password = test_update_password(add_a_password['id'], data)
    print(update_a_password)
    print(test_get_passwords())

    # Test delete a password record
    delete_a_password = test_delete_password(add_a_password['id'])
    print(delete_a_password)
    print(test_get_passwords())


if __name__ == "__main__":
    workflow()
