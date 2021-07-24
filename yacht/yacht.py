from collections import Counter

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "count1"
TWOS = "count2"
THREES = "count3"
FOURS = "count4"
FIVES = "count5"
SIXES = "count6"
FULL_HOUSE = "house"
FOUR_OF_A_KIND = "four"
LITTLE_STRAIGHT = "lstr"
BIG_STRAIGHT = "bstr"
CHOICE = "choice"


def score(dice, category=''):
    counted_dices = Counter(dice)
    points = 0
    if category == "count1":
        points += counted_dices[1]
    elif category == "count2":
        points += counted_dices[2]*2
    elif category == "count3":
        points += counted_dices[3]*3
    elif category == "count4":
        points += counted_dices[4]*4
    elif category == "count5":
        points += counted_dices[5]*5
    elif category == "count6":
        points += counted_dices[6]*6
    elif category == "house":
        if counted_dices.most_common(2)[0][1] == 3 and counted_dices.most_common(2)[1][1] == 2:
            points += counted_dices.most_common(2)[0][0]*3 + counted_dices.most_common(2)[1][0]*2
    elif category == "four":
        if counted_dices.most_common()[0][1] >= 4:
            points += counted_dices.most_common()[0][0]*4
    elif category == "yacht":
        if len(counted_dices) == 1:
            points = 50
    elif category == "lstr":
        if len(counted_dices) == 5 and 6 not in dice:
            points = 30
    elif category == "bstr":
        if len(counted_dices) == 5 and 1 not in dice:
            points = 30
    elif category == "choice":
        points = sum(dice)
    return points
