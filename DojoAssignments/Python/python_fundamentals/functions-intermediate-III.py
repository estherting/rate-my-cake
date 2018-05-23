def returnASCdictionary(min=40, max=200):
    dict = {}
    for i in range(min, max+1):
        dict[i] = chr(i)
    return dict

# print returnASCdictionary()

# A - 65
# a - 97
def returnUpper(string):
    newString = ""
    for c in string:
        if c == " ":
            newString += c
        newString += chr(ord(c)-32)
    return newString

# print returnUpper("hello")

def returnLower(string):
    newString = ""
    for c in string:
        if c == " ":
            newString += c
        elif ord(c) >= 97:   # if character is lowercase
            newString += c
        else:
            newString += chr(ord(c)+32)
    return newString
print returnLower("Hello Joe")
