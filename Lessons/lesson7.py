def sum_num(a,b):
    c = a + b
    return c


def symbol_line(char: str,repetition: int):
    return char * repetition


names = ['Jacob','Jana','Petr','Klaraaaaaaaaa']


def count_of_chars_in_list(names):
    count = 0
    for name in names:
        count += len(name)
    return count


def deleni(a, b):
    if b != 0:
        return a / b

print(deleni(4,0))