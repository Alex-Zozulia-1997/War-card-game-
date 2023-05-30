import random
from collections import deque
from player import Player

class Deck():
    def __init__(self):
        self.suits =["Dimonds","Hearts","Spades","Clubs"]
        self.cards =["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        deck_of_cards = []
        for i in self.cards:
            for j in self.suits:
                card = f"{i} of {j}"
                deck_of_cards.append(card)
        random.shuffle(deck_of_cards)
        self.deck = deck_of_cards

    def distribute_the_cards(self,players_count=9):
        #creating the players
        players = []
        for i in range(players_count):
            name = f"Player_{i+1}"
            #name = input("What's the first players' name?")
            player = Player(name)
            players.append(player)
        players = deque(players)

# Access the instances
        for player in players:
            print(player.name)    
        for i in self.deck:
            pl = players[0]
            players.rotate()
            pl.cards.append(i)
            print(i)
        # for i in players:
        #     print(i.cards)
        #     print(len(i.cards))
        return players
            #think about how to rotate the players in the list, so each card is assigned to the new player

        
        
d = Deck()
#print(len(d.deck))
#print(d.deck)
#print(d.distribute_the_cards())