from collections import Counter
discount = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
price = 8

def total(basket):
    packs = []

    # Collection of books
    amount = Counter(basket)

    # while loop with walrus operator, stops when len(amount) == 0
    while count := len(amount):
        packs.append(count)
        # Substraction of one book of each
        amount.subtract(amount.keys())
        # Remove zero and negative counts
        amount = +amount

    # replace (3,5) by (4,4)
    while 5 in packs and 3 in packs:
        packs.remove(3)
        packs.remove(5)
        packs += [4, 4]

    #Total:
    return sum([int(pack)*(100-discount[pack])*price for pack in packs])
