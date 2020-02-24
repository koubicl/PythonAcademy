anything = input('Give me some input: ')
if anything.isalpha():
    print('Letters Only.')
elif anything.isnumeric():
    print('Numeric.')
else:
    print('Mixed.')