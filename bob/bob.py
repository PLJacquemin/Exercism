def response(hey_bob):
    hey_bob = ''.join(hey_bob.split())
    if not hey_bob:
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
