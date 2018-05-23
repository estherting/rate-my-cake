var qrt = 200;
function quarterChance(qrt) {
  var coins = Math.floor(Math.random()*51) + 50;
  var winNum = 1;
  for(var i = 1; i <= qrt; i++) {
    var game = Math.floor(Math.random()*100) + 1;
    if(game == winNum) {
      break;
    }
  }
  var finalWinCoins = coins + (qrt - i);
  return finalWinCoins;
}

console.log(quarterChance(qrt));
