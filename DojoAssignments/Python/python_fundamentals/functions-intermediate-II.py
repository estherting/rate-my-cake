# Part I
def printVal(arr):
    for dict in arr:
        name = ""
        for value in dict.values():
            name += value + " "
        print name


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# printVal(students)


# Part II
def printUsers(users):
    for role in users:
        print role
        i = 1
        for name in users[role]:
            fullName = name['first_name']+name['last_name']
            print str(i) + " - " + name['first_name'] + " " + name['last_name'] + " - " + str(len(fullName))
            i += 1



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


print printUsers(users)
