function reward() {
  var sum = 1;
  for(var i = 2; i <= 30; i++) {
    sum += sum*2;
    if(sum >= 10000*100) {
      console.log("Reached $10,000 at day " + i);
      break;
    }
  }
  console.log(sum/100);
}



reward();
