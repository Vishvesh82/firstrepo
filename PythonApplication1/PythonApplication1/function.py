sentence='My name is Ram'
def sentenceReverse(s):
    m = s.split()[::-1]
    seperator = ' '
    print(seperator.join(m))
sentenceReverse(sentence)