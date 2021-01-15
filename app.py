from random import shuffle
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create card Objects
                create_card = Card(suit, rank)
                self.all_cards.append(create_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def remove_last(self):
        return self.all_cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} Cards"

    def remove(self):
        return self.all_cards.pop(0)

    def add(self, new_card):
        if type(new_card) == list:
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add(new_deck.remove_last())
    player_two.add(new_deck.remove_last())


game_on = True
round_number = 0

while game_on:
    round_number += 1
    print(f"Round {round_number}")
    print(len(player_one.all_cards), len(player_two.all_cards))

    if len(player_one.all_cards) == 0:
        print("Player one has lost, Player two win")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player two has lost, Player one win")
        game_on = False
        break

    # Start a new game
    player_one_cards = []
    player_one_cards.append(player_one.remove())

    player_two_cards = []
    player_two_cards.append(player_two.remove())

    war_on = True
    while war_on:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add(player_one_cards)
            player_one.add(player_two_cards)
            war_on = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add(player_one_cards)
            player_two.add(player_two_cards)
            war_on = False
        else:
            print("war started")
            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("Player two wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player one wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove())
                    player_two_cards.append(player_two.remove())


print(player_one, player_two)
