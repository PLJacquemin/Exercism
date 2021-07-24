score= [
 "cats",
 "pollen",
 "chocolate",
 "tomatoes",
 "strawberries",
 "shellfish",
 "peanuts",
 "eggs"]

class Allergies:

    def __init__(self, score):
        self.score = "%08d"%int(bin(score%256)[2:])
        self.all_list = []

    def allergic_to(self, item=None):
        return item in self.lst

    @property
    def lst(self):
        for i in range(len(self.score)):
            if self.score[i] == '1':
                self.all_list.append(score[i])
        return self.all_list
