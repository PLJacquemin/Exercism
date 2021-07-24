import re

template = '[0-9]{9}[0-9|X]'

def is_valid(isbn):
    isbn = isbn.replace("-","")
    # check if 10 digit or 9 digit + X, if match: sum
    if re.fullmatch(template,isbn):
        total=sum(int(isbn[i])*(10-i) if isbn[i].isdigit() else 10 for i in range(len(isbn)))
    else:
        return False
    return total%11==0
