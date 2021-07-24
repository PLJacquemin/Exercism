from collections import Counter

def find_anagrams(word, candidates):
    result = []
    for c in candidates:
        if Counter(word.lower()) == Counter(c.lower()) and c.lower() != word.lower():
            result.append(c)
    return result
