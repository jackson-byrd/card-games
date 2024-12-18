class Suit:

    def __init__(self, color, shape):
        self.color=color
        self.shape=shape

    def print(self):
        print("The color is " + self.color)
        print("The shape is " + self.shape)

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:

    def addCard(self, card_to_be_added):
        self.append(card_to_be_added)

    def shuffle(self):
        pass

    def cut(self):
        pass

    def deal(self):
        pass

    def __init__(self, num_of_cards, num_of_suits, suit_arr, value_arr):
        self.num_of_cards = num_of_cards
        self.num_of_suits = num_of_suits
        self.num_cards_per_suit = self.num_of_cards / self.num_of_suits
        self.suits_arr = suit_arr
        self.value_arr = value_arr
        
        for card in range(0, self.num_of_cards):
            for card_with_suit in range(0, self.num_cards_per_suit):
                for suit in self.suits_arr:
                    for value in self.value_arr:
                        temp_suit = Suit(suit_arr[suit].color, suit_arr[suit].shape)
                        temp_val = value
                        self.addCard(Card(temp_suit, temp_val))
