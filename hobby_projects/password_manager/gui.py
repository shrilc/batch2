import PySimpleGUI as sg
import requests

# API Endpoints
GET_ALL_PASSWORD_API = 'http://localhost:5000/passwords'


# All the stuff inside your window.
layout = [  [sg.Text('Username:'), sg.Input(key='username')],
            [sg.Text('Password:'), sg.Input(key='password')],
            [sg.Button('Add'), sg.Button('Update'), sg.Button('Delete')],
            [sg.Table(values=[], headings=['ID', 'Username', 'Password'], key='table')]
        ]

# Create the Window
window = sg.Window('Window Title', layout, finalize=True)


# Populate the table
response = requests.get(GET_ALL_PASSWORD_API)
passwords = response.json()
table_data = [[id, data['username'], data['password']] for id, data in passwords.items()]
window['table'].update(values=table_data)

# for id, data in passwords.items:
#     id = id
#     username = data['username']
#     password = data['password']
#     table_data.append([id, username, password])

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()