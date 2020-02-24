'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
creds = {'bob': '123', 'ann': 'pass123', 'mike': 'password123','liz':'pass123'}
print(60*'-')
tree = input('Hey man, welcome to the app.\nIf you want to login type L, if you want to register type R: ')
tree_valid = False

while not tree_valid:

    if tree.lower() == 'l':
        username = input('Username: ')
        pw = input('Password: ')
        if username not in creds.keys() or pw != creds[username]:
            print('Password or username is wrong.')
        else:
            print('Permission granted.')
            tree_valid = True

    elif tree.lower() == 'r':
        reg_username = input('Please insert your username, you\'ll want to use: ')
        reg_pw = input('Please insert your password, you\'ll want to use: ')
        while reg_username in creds.keys():
            reg_username = input('Please choose another username, this one is already registered: ')
            if reg_username not in creds.keys():
                reg_pw = input('Please repeat the password: ')

        creds[reg_username] = reg_pw
        print('Credentials were inserted into DB, please now log in.')
        username = input('Username: ')
        pw = input('Password: ')
        if username not in creds.keys() or pw != creds[username]:
            print('Password or username is wrong.')
        else:
            print('Permission granted.')
            tree_valid = True
    else:
        tree = input('Please again. L for login / R for register: ')

print(60*'-')
choice = int(input('There are {} texts ready to be analysed. Please enter 1-{}: '.format(len(TEXTS),len(TEXTS))))
while choice > len(TEXTS) or choice <= 0:
    choice = int(input('Please enter 1-{}: '.format(len(TEXTS),len(TEXTS))))
print(60*'-')
text_choice = TEXTS[choice-1]
words_list = text_choice.split()
count_of_capitals = 0
count_of_uppercases = 0
count_of_lowercases = 0
count_of_numeric = 0
sum_of_words = 0
print('There are {} words in total.'.format(len(words_list)))
for word in words_list:

    if word.istitle():
        count_of_capitals += 1
    elif word.isupper():
        count_of_uppercases += 1
    elif word.islower():
        count_of_lowercases += 1
    elif word.isnumeric():
        count_of_numeric += 1
        sum_of_words += int(word)


print('There are {} words starting with capital letter.'.format(count_of_capitals))
print('There are {} uppercase words.'.format(count_of_uppercases))
print('There are {} lowercase words.'.format(count_of_lowercases))
print('There are {} numeric words.'.format(count_of_numeric))
print(60*'-')

count_dict = {}

for word in words_list:
    char_count = len(word)

    if char_count not in count_dict.keys():
        count_dict[char_count] = 1
    else:
        count_dict[char_count] += 1
key_list = []
for dict_key in count_dict:
    key_list.append(dict_key)

key_list.sort()

for key in key_list:
    print(key,'*'*count_dict[key],count_dict[key])

print(60*'-')

print('The sum of numeric words is:',sum_of_words)

print(60*'-')



