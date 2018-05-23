function birthdayCountDown(days) {
  while(days > 0) {
    if(days >= 30){
      console.log(days + " days until my birthday. Such a long time...:(");
    } else if(days >= 5) {
      console.log(days + " days until my birthday! :)");
    } else if(days >= 2){
      console.log(days + " DAYS UNTIL MY BIRTHDAY!!!");
    } else {
      console.log(days + " DAY UNTIL MY BIRTHDAY!!!");
    }
    days--;
  }
  console.log("HAPPY BIRTHDAY TO ME! HAPPY BIRTHDAY TO ME!!!!!!!!!!! WOOOOHOOOOOOO");
}

birthdayCountDown(32);
