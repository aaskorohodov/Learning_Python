import random


class Card:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        '''Сравнение <'''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __gt__(self, other):
        '''Сравнение >'''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 > t2

    def __eq__(self, other):
        '''Сравнение =='''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 == t2


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, players, cards):
        player_list = []
        for i in range(1, players + 1):
            exec(f'player{i} = Hand()')
            exec(f'player{i}.hand_name()')
            exec(f'self.move_cards(player{i}, cards)')
            exec(f'player_list.append(player{i}.name)')
        return player_list


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def hand_name(self):
        names = ['Tim', 'Bob', 'Jack', 'Smith', 'Adam', 'Pit', 'Dou', 'Tif']
        self.name = random.choice(names)


deck = Deck()
print(deck.deal_hands(2, 5))
