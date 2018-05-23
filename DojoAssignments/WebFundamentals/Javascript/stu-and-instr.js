// Part I
function printStuName(students) {
  for(var i = 0; i < students.length; i++) {
    console.log(students[i]["first_name"] + " " + students[i]["last_name"]);
  }
}

var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

printStuName(students);


// Part II
function printStuAndInstrName(users) {
  for(var role in users) {
    console.log(role);
    for(var i = 1; i <= users[role].length; i++) {
      console.log(i + " - " + users[role][i-1]["first_name"] + " " + users[role][i-1]["last_name"] + " - " + (users[role][i-1]["first_name"]+users[role][i-1]["last_name"]).length);
    }
  }
}

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

 printStuAndInstrName(users);
