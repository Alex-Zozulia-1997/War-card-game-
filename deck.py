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
        deck_of_cards.extend(["Joker Red","Joker Black"])

        
        random.shuffle(deck_of_cards)
        self.deck = deck_of_cards

    def distribute_the_cards(self, players_count=5):
    # Creating the players
        players = []
        for i in range(players_count):
            name = f"Player_{i+1}"
            player = Player(name)
            players.append(player)

        # Distributing the cards
        player_index = 0
        for card in self.deck:
            player = players[player_index]
            player.cards.append(card)
            player_index = (player_index + 1) % players_count

        return players
      
        
d = Deck()
