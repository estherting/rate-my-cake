def typeList(list):
    strCount = 0
    intCount = 0
    string = "String: "
    sum = 0
    for e in list:
        if isinstance(e, str):
            string += e + " "
            strCount+=1
        elif isinstance(e, int):
            sum += e
            intCount+=1
    if strCount > 0 and intCount > 0:
        print "The list you entered is of mixed type"
        print string
        print "Sum: " + str(sum)
    elif strCount > 0 and intCount == 0:
        print "The list you entered is of string type"
        print string
    elif intCount > 0 and strCount == 0:
        print "The list you entered is of integer type"
        print "Sum: " + str(sum)
    else:
        print "Your list is empty or contains only unrecognized elements"


# test conditions
list1 = []
list2 = [1, 4, "hello"]
list3 = [-1, 9, 0]
list4 = ["hey", "bonjour"]
list5 = [[1,2], 1, "hello"]

typeList(list1)
typeList(list2)
typeList(list3)
typeList(list4)
typeList(list5)
