from collections import Counter

def is_pangram(sentence):
    letter_list = []
    for s in sentence:
        if s.isalpha():
            letter_list.append(s.lower())
    letter_count = sorted(Counter(letter_list))
    return len(letter_count) == 26
