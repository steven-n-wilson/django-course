#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    # Class object atributes
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self.create_deck()

    def create_deck(self):
        deck = []

        for s in SUITE:
            for r in RANKS:
                deck.append(s+r)

        shuffle(deck)
        self.deck = deck

    def split_deck(self):
        middle_index = len(self.deck)/2
        return self.deck[:int(middle_index)], self.deck[int(middle_index):]

    def __str__(self):
        return str(self.deck)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, player_deck):
        self.player_deck = player_deck

    def add(self, card):
        self.player_deck.append(card)

    def remove(self):
        return self.player_deck.pop()

    def __str__(self):
        return str(self.player_deck)

    def __len__(self):
        return len(self.player_deck)


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand=[]):
        self.name = name
        self.hand = hand

    def check(self):
        if len(self.hand) == 52:
            print(f'{self.name()} Wins!')
            return False

        return True


def war(p1_war, p2_war):
    p1_count = 0
    p2_count = 0

    for p1, p2 in zip(p1_war, p2_war):
        if p1 > p2:
            p1_count += 1
        elif p1 < p2:
            p2_count += 1

    if p1_count > p2_count:
        return "p1"


def add_war_cards(player_hand):
    player_hand.add(p1_turn)
    player_hand.add(p2_turn)

    for i in p1_war:
        player_hand.add(i)

    for i in p2_war:
        player_hand.add(i)


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

setup = False
playing = True

while playing:

    if setup == False:
        my_deck = Deck()
        player1_deck, player2_deck = my_deck.split_deck()

        player1_hand = Hand(player1_deck)
        player2_hand = Hand(player2_deck)

        name = input("Enter your name to play: ")
        player1 = Player(name, player1_hand)
        player2 = Player("COMPUTER", player2_hand)
        setup = True

    p1_turn = player1_hand.remove()
    print(f"{player1.name}'s card is {p1_turn}")

    p2_turn = player2_hand.remove()
    print(f"{player2.name}'s card is {p2_turn}")

    try:

        if int(p1_turn[1:]) == int(p2_turn[1:]):
            print("\nWAR!")

            p1_war = [player1_hand.remove() for i in range(3)]
            print(f"{player1.name}'s cards are {p1_war}")

            p2_war = [player2_hand.remove() for i in range(3)]
            print(f"{player2.name}'s cards are {p2_war}")

            war_winner = war(p1_war, p2_war)

            if war_winner == "p1":
                add_war_cards(player1_hand)
                playing = player1.check()
                print(f"{player1.name} wins this war!")
            else:
                add_war_cards(player2_hand)
                playing = player2.check()
                print(f"{player2.name} wins this war!")

        elif int(p1_turn[1:]) > int(p2_turn[1:]):
            player1_hand.add(p2_turn)
            playing = player1.check()
            print(f"{player1.name} keeps cards!")
        else:
            player2_hand.add(p1_turn)
            playing = player2.check()
            print(f"{player2.name} keeps cards!")

    except:
        pass

    playing = False
