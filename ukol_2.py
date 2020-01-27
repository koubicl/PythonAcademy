from datetime import datetime
import sys

# Greet the client
print('=' * 80)
print('''Welcome to the DESTINATIO,
      place where people plan their trips''')
print('=' * 80)

# Offer destinations
print('We can offer you the following destinations:')
print('-' * 80)
print('''
      1 - Prague | 1000
      2 - Wien | 1100
      3 - Brno | 2000
      4 - Svitavy | 1500
      5 - Zlin | 2300
      6 - Ostrava | 3400
      ''')
print('-' * 80)

# Get input from user about destination
selection = int(input('Please enter the destination number to select: '))

# Assign variables appropriate data
DESTINATIONS = ['Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Check, whether entered valid input

# Get data from variables based on user's input

destination = DESTINATIONS[selection - 1]
if destination in DISCOUNT_25:
    print('You have discount 25%!')
    price = PRICES[selection - 1] * 0, 75
price = PRICES[selection - 1]

# Calculate the price and check whether discount applicable for the selected destination

# Introduce registration

# Get input from user about personal data
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth_year = input('YEAR of BIRTH: ')
if birth_year == '':
    birth_year = input('Zadejte prosim YEAR of BIRTH: ')
elif int(birth_year) > int(datetime.now().strftime('%Y'))-15:
    print('Je vam pod 15 let. Nemuzeme vam vyhovet.')
    sys.exit()
print('=' * 40)
if birth_year=='':
    print('Jste hloupej, nechceme vas tady.')
    sys.exit()
email = input('EMAIL: ')
if '@' in email:
    pass
else:
    print('Email neobsahuje @, neplatny mail.')
    email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD: ')
if len(password) < 8:
    print('Heslo musi byt dlouhe alespon 8 znaku.')
    password = input('PASSWORD: ')
if len(password) < 8:
    print('Jste hloupej, nechceme vas tady.')
    sys.exit()
elif password[0].isnumeric() or password[-1].isnumeric():
    print('Heslo nesmi zacinat nebo koncit cislici')
    password = input('PASSWORD: ')
if password[0].isnumeric() or password[-1].isnumeric():
    print('Jste hloupej, nechceme vas tady.')
    sys.exit()
if not password.isalnum():
    print('Heslo musi obsahovat znaky!')
    password = input('PASSWORD: ')
if not password.isalnum():
    print('Jste hloupej, nechceme vas tady.')
    sys.exit()




print('=' * 80)

# Check if the user is older than 15 years old

# Check if email contains @ symbol

# Check if password
# - is at least 8 chars long,
# - doesn't begin and end with a number
# - and contains both letters and numbers

# Thank user by the input name and inform him/her about the reservation made
