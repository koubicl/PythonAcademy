import sys
days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
day_nr = input('Please enter the number of the day: ')

if not day_nr:
    print('No input provided')
elif not day_nr.isnumeric():
    print('Enter only numbers, please')
    day_nr = input('Please enter the number of the day: ')


elif int(day_nr) > 7 or int(day_nr) < 1:
    day_nr = input('Please insert number 1-7: ')


else:
    print(days[int(day_nr)-1])