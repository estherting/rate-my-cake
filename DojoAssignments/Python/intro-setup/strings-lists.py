# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')
newWords = words[:18] + "month" + words[18+3:]
print newWords

# Min and Max
list = [1, 3, -6, 7, 9]
print (min(list), max(list))

# Fist and Last
list = ["first", 3, "hello", -3, "last"]
print (list[0], list[len(list)-1])
newList = [list[0], list[len(list)-1]]
print newList

# New List
list = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
list = sorted(list)
list1half = list[:len(list)/2]
list2half = list[len(list)/2:]
# Mutating-methods on lists tend to return None, not the modified list
# .insert() mutates list2half without returning anything
list2half.insert(0, list1half)
print list2half
