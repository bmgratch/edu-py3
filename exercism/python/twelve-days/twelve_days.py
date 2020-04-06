def recite(start_verse, end_verse):
    gifts = ["a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"]
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
    for i in range(start_verse - 1, end_verse):
        verse_gifts = gifts[i::-1]
        if i != 0:
            verse_gifts[-1] = "and %s" % verse_gifts[-1]
        song.append("On the %s day of Christmas my true love gave to me: %s." % (xth[i], (', '.join(verse_gifts))))
    return song
