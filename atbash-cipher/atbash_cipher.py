lo = "abcdefghijklmnopqrstuvwxyz"

def encode(plain_text):
    out_t = ""
    for l in plain_text:
        if l.isalpha():
            out_t += lo[(25-lo.index(l.lower()))%26]
        elif l.isdigit():
            out_t += l
    return ' '.join(out_t[i:i+5] for i in range(0, len(out_t), 5))

def decode(ciphered_text):
    out_t = ""
    for l in ciphered_text:
        if l.isalpha() and l in lo:
            out_t += lo[(25-lo.index(l))%26]
        elif l.isdigit():
            out_t += l
    return out_t
