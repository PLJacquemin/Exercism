units = {1:"one",2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",9:"nine"}
teen = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifyeen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
ty = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixteen",7:"seventy",8:"eighty",9:"ninety"}
mil = [""," thousand "," million "," billion "]

def say(number):
    list_mil = []
    text_list = []
    # Case zero
    if number == 0:
        return "zero"
    # Case negative
    elif number < 0:
        raise ValueError("negative number")
    # Outside range
    elif number >= 10**12:
        raise ValueError("too high")
    # creating a list of thousands
    elif number > 0:
        while number:
            list_mil.append(number%1000)
            number = number//1000
        for i in range(len(list_mil)):
            text = ""
            m = int(list_mil[i])
            # Case 0
            if m == 0:
                text_list.append('')
                continue
            # amount of hundred
            if m//100 != 0:
                text += "{} hundred ".format(units[m//100])
            # tens
            if m%100 != 0:
                if m%100 < 10:
                    text += units[m%100]
                elif m%100 < 20:
                    text += teen[m%100]
                elif m%100%10 != 0:
                    text += "{}-{}".format(ty[m%100//10],units[m%100%10])
                else:
                    text += ty[m%100//10]
            text_list.append(text+mil[i])
        text_list.reverse()
        return ''.join(m for m in text_list).strip()
