var HOLDEM = true;
var VERSION = 0.1;

var deck = [];
for (var rank = 1; rank <= 13; rank++) {
  for (var i = 0; i <= 3; i++) {
    deck.push([rank, ["H", "D", "S", "C"][i]]);
  }
}
console.log(deck);

function Card(suit, rank) {
    if (!(["S", "D", "H", "C"].includes(suit))) {
        throw "Suit must be S or D or H or C"
    }
    if (rank < 2 || rank > 14) {
        throw "rank must be between 2 and 14"
    }
    this.suit = suit;
    this.rank = rank;
}
