
word = open('words','r')

wordclean = [word.strip().lower() for word in open('words','r')]


def signature(word):
    return ''.join(sorted(word))

def anagram(myword):
    result = []
    for word in wordclean:
        if signature(word) == signature(myword):
            result.append(word)
    return result

# to speed up we can create a dictionary of signatures first

words_bysig = {}

for word in wordclean:
    words_bysig[signature(word)].append(word)

