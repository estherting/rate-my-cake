function numOnly(arr) {
  var newArr = [];
  for(var i = 0; i < arr.length; i++) {
    if(typeof arr[i] === "number") {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}

console.log(numOnly([1, "apple", -3, "orange", 0.5]));
