up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    cipher = ''
    for t in text:
        if t in lo:
            cipher += lo[lo.index(t)+key-26]
        elif t in up:
            cipher += up[up.index(t)+key-26]
        else:
            cipher += t
    return cipher
