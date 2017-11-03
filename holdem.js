var HOLDEM = true;
var VERSION = 0.1;

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

function Deck() {
    this.cards = [];
    for (var rank = 2; rank <= 14; rank++) {
        for (var i = 0; i <= 3; i++) {
            this.cards.push(new Card(["H", "D", "S", "C"][i], rank));
        }
    }

    this.shuffle = function() {
        for (var i = this.cards.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = this.cards[i];
            this.cards[i] = this.cards[j];
            this.cards[j] = temp;
        }
    }
}


function Player(name) {
    this.name = name;
    this.cards = [];
}

function Game(deck) {
    this.deck = deck;
    this.players = [];
}