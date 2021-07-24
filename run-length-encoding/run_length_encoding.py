def decode(string):
    last = ""
    output = ""
    count = ""
    for letter in string:
        if letter.isdigit():
            count+=letter
        else:
            output += (int(count) if count else 1)*letter
            count = ""
    return output


def encode(string):
    last = ""
    output = ""
    count = 0
    for letter in string:
        # first letter
        if letter != last and last:
            output += str(count if count > 1 else "") + last
            count = 1
        # same letter
        else:
            count += 1
        last = letter
    output += str(count if count > 1 else "") + last
    return output
