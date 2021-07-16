def recite(start_verse, end_verse):

    when = "On the {} day of Christmas my true love gave to me: "

    days = [
"first",
"second",
"third",
"fourth",
"fifth",
"sixth",
"seventh",
"eighth",
"ninth",
"tenth",
"eleventh",
"twelfth"
]

    things = [
"a Partridge in a Pear Tree.",
"two Turtle Doves, and ",
"three French Hens, ",
"four Calling Birds, ",
"five Gold Rings, ",
"six Geese-a-Laying, ",
"seven Swans-a-Swimming, ",
"eight Maids-a-Milking, ",
"nine Ladies Dancing, ",
"ten Lords-a-Leaping, ",
"eleven Pipers Piping, ",
"twelve Drummers Drumming, "]

    song = []
    verse = start_verse
    while end_verse - verse >= 0:
        sentence = when.format(str(days[verse-1]))
        for times in reversed(range(verse)):
            sentence = sentence + things[times]
        song.append(sentence)
        verse += 1
    return song
