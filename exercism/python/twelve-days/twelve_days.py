def recite(start_verse, end_verse):
    gifts = {
        1: "a Partridge in a Pear Tree.",
        2: "two Turtle Doves, ",
        3: "three French Hens, ",
        4: "four Calling Birds, ",
        5: "five Gold Rings, ",
        6: "six Geese-a-Laying, ",
        7: "seven Swans-a-Swimming, ",
        8: "eight Maids-a-Milking, ",
        9: "nine Ladies Dancing, ",
        10: "ten Lords-a-Leaping, ",
        11: "eleven Pipers Piping, ",
        12: "twelve Drummers Drumming, "
        }
    xth = [ None,
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
            "twelfth"]
    song = []
    for i in range(start_verse, end_verse + 1):
        verse = "On the %s day of Christmas my true love gave to me: " % xth[i]
        for n in range(i, 0, -1):
            if n == 1 and i != 1:
                verse +="and %s" % gifts[n]
            else:
                    verse += gifts[n]
        song.append(verse)
    return song
