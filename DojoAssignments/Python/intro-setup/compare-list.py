def compareList(l1, l2):
    if len(l1) != len(l2):
        print "The lists are not the same"
    else:
        i = 0
        while i < len(l1):
            if l1[i] == l2[i]:
                i += 1
            else:
                print "The lists are not the same"
                break
        if i == len(l1):
            print "The lists are the same!"

# Test conditions
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

compareList(list_one, list_two)
