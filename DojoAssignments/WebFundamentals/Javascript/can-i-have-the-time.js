function haveTime(hr, min, per) {
  per = per.toUpperCase();
  if(per == "AM") {
    var period = " in the morning";
  }
  else if (per == "PM") {
    var period = " in the evening";
  }
  if(min < 30) {
    console.log("It's just after " + hr + period);
  } else {
    if(hr === 12) {
      hr = 0;
    }
    console.log("It's almost " + (hr+1) + period);
  }
}
