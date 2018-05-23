def printMultTable():
    for i in range(0, 13):
        row = ""
        if i == 0:
            row += "x "
        else:
            row += str(i)+" "
        for j in range(1, 13):
            if i == 0:
                row += str(j) + " "
            else:
                row += str(i*j) + " "
        print row

printMultTable()
