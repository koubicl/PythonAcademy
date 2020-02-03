from datetime import datetime

age = input('How old are you? ')
birth_year = int(datetime.now().strftime('%Y'))-int(age)

print('You were (probably) born in 1982.')