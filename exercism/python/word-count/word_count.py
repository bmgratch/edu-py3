def count_words(sentence):
    counter = {}
    word_list = strip_punctuation(sentence.lower()).split()
    for word in word_list:
        if word != '':
            counter.setdefault(word.strip("'"), 0)
            counter[word.strip("'")] += 1
    return counter


# just get rid of non-apostrophe punctuation
def strip_punctuation(sentence):
    new = []
    for c in sentence:
        if c.isalnum() or c == "'":
            new.append(c)
        else:
            new.append(' ')
    return ''.join(new)
