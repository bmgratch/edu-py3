def recite(start_verse, end_verse):
    gifts = ["a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
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
    xth = [ "first",
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
    verse = ["On the ", None , " day of Christmas my true love gave to me: "]
    for i in range(start_verse - 1, end_verse):
        verse = verse[:3]
        verse[1] = xth[i]
        for n in range(i, -1, -1):
            if n == 0 and i != 0:
                verse.append("and ")
            verse.append(gifts[n])
        song.append(''.join(verse))
    return song
