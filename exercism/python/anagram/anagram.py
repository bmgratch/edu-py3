def find_anagrams(word, candidates):
    answers = []
    for word2 in candidates:
        if sorted(word.lower()) == sorted(word2.lower()) and word.lower() != word2.lower():
            answers.append(word2)
    return answers

