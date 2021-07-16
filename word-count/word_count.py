def count_words(sentence):
    words_counted = {}
    cleaned_list = []
    separators = [",","\t","\n","_"]

    # remove separators and create a list of words
    for sep in separators:
        sentence = sentence.replace(sep, " ")
    words_list = sentence.lower().split()

    # clean the list: remove starting/ending "'" and all non alphanumeric characters != "'"
    for word in range(len(words_list)):
        cleaned_word = ""
        words_list[word] = words_list[word].lstrip("'").rstrip("'")
        for letter in words_list[word]:
            if letter.isalnum() == True or letter == "'":
                cleaned_word += letter
        cleaned_list.append(cleaned_word)

    # create a dictionnary and count the words
    for word in range(len(cleaned_list)):
        if cleaned_list[word] in words_counted:
            words_counted[cleaned_list[word]] += 1
        else:
            words_counted[cleaned_list[word]] = 1

    return words_counted
