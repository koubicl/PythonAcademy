data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

username = input('Please enter username: ')
pw = input('Please enter password: ')

if username not in data.keys() or pw != data[username]:
    print('Password or username is wrong')
else:
    print('Permission granted')
