import random

class Card( object ):
  def __init__(self, name, value, suit):
    self.value = value
    self.suit = suit
    self.name = name
    self.showing = False
  def __repr__(self):
    if self.showing:
      return str( self.name) + " of " + self.suit
    else:
      return "Card"

class StandardDeck(object):
  def __init__(self):
    self.cards = []
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = {"Two":2,
              "Three":3,
              "Four":4,
              "Five":5,
              "Six":6,
              "Seven":7,
              "Eight":8,
              "Nine":9,
              "Ten":10,
              "Jack":11,
              "Queen":12,
              "King":13,
              "Ace":14 }

    for name in values:
      for suit in suits:
        self.cards.append( Card(name, values[name], suit) )

  def __repr__(self):
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

  def shuffle(self, times=1 ):
    random.shuffle(self.cards)
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)


'''
deck = StandardDeck()
deck.shuffle()


randoCard = deck.deal()
randoCard

randoCard.showing = True
randoCard
'''
