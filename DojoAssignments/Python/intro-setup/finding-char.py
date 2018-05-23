def findChar(list, char):
    newList = []
    for word in list:
        for c in word:
            if c == char:
                newList.append(word)
                break
    print newList


word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChar(word_list, char)
