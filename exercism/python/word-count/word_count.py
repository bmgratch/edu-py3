def count_words(sentence):
    counter = {}
    word_list = strip_punctuation(sentence.lower()).split()
    for word in word_list:
        if len(word) > 0:
            counter.setdefault(word.strip("'"), 0)
            counter[word.strip("'")] += 1
    return counter

def word_strip(word):
    return "".join(c for c in word if c.isalnum())

# just get rid of non-apostrophe punctuation
def strip_punctuation(sentence):
    new = []
    for c in sentence:
        if c.isalnum() or c == "'":
            new.append(c)
        else:
            new.append(' ')
    return ''.join(new)
