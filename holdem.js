var HOLDEM = true;
var VERSION = 0.1;

var deck = [];
for (var rank = 1; rank <= 13; rank++) {
  for (var i = 0; i <= 3; i++) {
    deck.push([rank, ["H", "D", "S", "C"][i]]);
  }
}
console.log(deck);
