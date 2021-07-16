class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        if self.card_num.isdigit() == False:
            return False
        else:
            card_num_cleaned = list(map(int, self.card_num))
            for ind in range(len(card_num_cleaned)-2,-1,-2):
                card_num_cleaned[ind] = card_num_cleaned[ind]*2
                if card_num_cleaned[ind] > 9:
                    card_num_cleaned[ind] -= 9
        return True if sum(card_num_cleaned)%10==0 and len(card_num_cleaned) > 1 else False
