QUnit.test("Card creation test", function( assert ) {
    card = new Card("D", 12);
    assert.equal(card.suit, "D");
    assert.equal(card.rank, 12);
});

QUnit.test("Card suit validation test", function( assert ) {
    assert.throws(function() {
        card = new Card("A", 12);
    })
});

QUnit.test("Card rank validation test", function( assert ) {
    assert.throws(function() {
        card = new Card("C", 1);
    })
    assert.throws(function() {
        card = new Card("C", 15);
    })
});