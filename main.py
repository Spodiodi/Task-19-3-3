import requests
import json


def print_res(res, method):
    print('\n', res.status_code, method)

    if 'application/json' in res.headers['Content-Type']:
        print(res.json())
    else:
        print(res.text)


url = "https://petstore.swagger.io/v2"
headers = {'accept': 'application/json'}
params = {'status': 'available'}
username = 'NatashaUser1'


# GET pet
res = requests.get(f'{url}/pet/findByStatus', params=params, headers=headers)
print_res(res, 'get pet')


# GET user before all and delete
res = requests.get(f'{url}/user/{username}')
print_res(res, 'get user before all')
# if user exists, login and delete
status_code = res.status_code
if status_code == 200:
    params = {'status': 'available', 'username': username, 'password': '12345678'}
    res = requests.get(f'{url}/user/login', params=params, headers=headers)
    print_res(res, 'get user after login')
# delete all user with the same name
while status_code == 200:
    res = requests.delete(f'{url}/user/{username}')
    print_res(res, 'del user')
    res = requests.get(f'{url}/user/{username}')
    status_code = res.status_code


# POST user
data = {
    'id': 0,
    'username': username,
    'firstName': 'NatashaUserFirst',
    'lastName': 'NatashaUserLast',
    'email': 'tre@ma.ru',
    'password': '12345678',
    'phone': '8123456789',
    'userStatus': 1}

res = requests.post(f'{url}/user', headers=headers, json=data)
# translate json into dict
user = json.loads(res.content)
# get user id
user_id = user['message']
print_res(res, f'post user {user_id}')


# GET test creating user
res = requests.get(f'{url}/user/{username}')
print_res(res, 'get user after post')


# GET for login
params = {'status': 'available', 'username': username, 'password': '12345678'}
res = requests.get(f'{url}/user/login', params=params, headers=headers)
print_res(res, 'get user after login')


# PUT
data = {
    'id': user_id,
    'username': username,
    'firstName': 'NatashaUserFirst',
    'lastName': 'NatashaUserLast',
    'email': 'new_tre@ma.ru',
    'password': '12345678',
    'phone': '8123456000',
    'userStatus': 1}

res = requests.put(f'{url}/user/{username}',
                   headers=headers,
                   json=data)
print_res(res, 'put user')


# GET test changing user
res = requests.get(f'{url}/user/{username}')
print_res(res, 'get user after put')


# DELETE
res = requests.delete(f'{url}/user/{username}')
print_res(res, 'del user')


# GET test changing user
res = requests.get(f'{url}/user/{username}')
print_res(res, 'get user after delete')
