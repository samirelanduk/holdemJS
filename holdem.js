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


function Player(name, chips) {
    this.name = name;
    this.cards = [];
    this.game = null;
    this.chips = chips;

    this.joinGame = function(game) {
        game.players.push(this);
        this.game = game;
    }

    this.nextPlayer = function() {
        playerIndex = this.game.players.findIndex(x => x == this);
        if (playerIndex == this.game.players.length - 1) {
            return this.game.players[0];
        } else {
            return this.game.players[playerIndex + 1];
        }
    }

    this.bet = function(amount) {
        this.chips -= amount;
        this.game.pot += amount;
    }
}

function Game(deck, sb, bb) {
    this.deck = deck;
    this.sb = sb;
    this.bb = bb;
    this.players = [];
    this.dealer = null;
    this.pot = 0;

    this.assignDealer = function() {
        var i = Math.floor(Math.random() * (this.players.length));
        this.dealer = this.players[i];
    }

    this.smallBlind = function() {
        return this.dealer.nextPlayer();
    }

    this.bigBlind = function() {
        return this.smallBlind().nextPlayer();
    }

    this.dealCards = function() {
        for (var p = 0; p < this.players.length; p++) {
            this.players[p].cards.push(this.deck.cards.pop())
        }
    }
    
}