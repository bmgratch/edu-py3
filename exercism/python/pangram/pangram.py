def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for a in alphabet:
        if sentence.lower().count(a) == 0:
            return(False)
    return(True)

