import PySimpleGUI as sg
import requests

# API Endpoints
GET_ALL_PASSWORD_API = 'http://localhost:5000/passwords'
ADD_PASSWORD_URL = 'http://localhost:5000/passwords/add'
UPDATE_PASSWORD_URL = 'http://localhost:5000/passwords/update/{}'
DELETE_PASSWORD_URL = 'http://localhost:5000/passwords/delete/{}'

# All the stuff inside your window.
layout = [  [sg.Text('Username:'), sg.Input(key='username', size=(50, 1))],
            [sg.Text('Password:'), sg.Input(key='password', size=(50, 1))],
            [sg.Button('Add'), sg.Button('Update'), sg.Button('Delete')],
            [sg.Table(values=[], headings=['ID', 'Username', 'Password'],auto_size_columns=True,enable_click_events=True, key='table', size=(20, 20))]
]

# Create the Window
window = sg.Window('Window Title', layout, finalize=True, resizable=True) # resizable=True

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
selected=-1
while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == 'Add':
        data = {'username': values['username'], 'password': values['password']}
        response = requests.post(ADD_PASSWORD_URL, json=data)
        password_id = response.json()['id']
        passwords[password_id] = data
    elif event == 'Update':
        if selected==-1:
            sg.popup_no_buttons('Select a row to Update', non_blocking=True)
            continue
        password_id = table_data[selected][0]
        data = {'username': values['username'], 'password': values['password']}
        response = requests.put(UPDATE_PASSWORD_URL.format(password_id), json=data)
        passwords[password_id] = data
    elif event == 'Delete':
        if selected==-1:
            sg.popup_no_buttons('Select a row to Delete', non_blocking=True)
            continue
        password_id = table_data[selected][0]
        response = requests.delete(DELETE_PASSWORD_URL.format(password_id))
        del passwords[password_id]
        window['username'].update("")
        window['password'].update("")
        selected=-1
    
    if isinstance(event, tuple):
        if event[2][0] == None:
            window['username'].update("")
            window['password'].update("")
            selected=-1

        elif event[2][0] >=0:
            # window['username'].update(values[event[2][0]][event[2][1]])
            window['username'].update(table_data[window['table'].SelectedRows[0]][1])
            window['password'].update(table_data[window['table'].SelectedRows[0]][2])
            selected=window['table'].SelectedRows[0]

    table_data = [[id, record['username'], record['password']] for id, record in passwords.items()]
    window['table'].update(values=table_data)

window.close()