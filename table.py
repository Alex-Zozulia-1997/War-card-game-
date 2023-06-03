from deck import Deck

class Table():
    def __init__(self):
        deck = Deck()
        self.deck = deck.deck
        self.players = deck.distribute_the_cards()
        self.active_players = list(self.players)
        self.game_on = True
        self.turn_cards = []

    def turn(self):
        for i in self.players:
            if i.ingame == False:
                try:
                    self.active_players.remove(i)
                except:
                    continue
        print(self.active_players)
        for i in self.active_players:
           self.turn_cards.append(i.move())

    # Determine the winner and clear the turn_cards list
        winner = self.check_the_highest_card(self.active_players)
        self.award(winner)
        self.turn_cards = []

        return self.active_players


    def check_the_highest_card(self, player_list):
        card_ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
            "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13,
            "Ace": 14, "Joker": 15
        }
        highest_card_rank = 0
        list_of_winners = []

        for player in player_list:
            try:
                rank = card_ranks[player.current_card.split()[0]]
                if rank > highest_card_rank:
                    highest_card_rank = rank
                    list_of_winners = [player]
                elif rank == highest_card_rank:
                    list_of_winners.append(player)
            except AttributeError:
                continue

        while len(list_of_winners) > 1:
            self.turn_cards.extend([player.move() for player in list_of_winners])
            highest_card_rank = 0
            new_list_of_winners = []

            for player in list_of_winners:
                try:
                    rank = card_ranks[player.current_card.split()[0]]
                    if rank > highest_card_rank:
                        highest_card_rank = rank
                        new_list_of_winners = [player]
                    elif rank == highest_card_rank:
                        new_list_of_winners.append(player)
                except AttributeError:
                    continue

            list_of_winners = new_list_of_winners

        return list_of_winners[0] if list_of_winners else None


    def award(self, winning_player):
        for i in self.active_players:
            if i.name == winning_player.name:
                i.cards.extend(self.turn_cards)
                
        self.turn_cards = []
               
    def game(self):
        while len(self.active_players) > 1:
            try:
                self.award(self.check_the_highest_card(self.turn()))
            
                if len(self.active_players) == 2:
                    if len(self.active_players[1].cards) > len(self.active_players[0].cards):
                        name = self.active_players[1].name
                        print(f'{name} is the Winner')
                    elif len(self.active_players[1].cards) < len(self.active_players[0].cards):
                        name = self.active_players[0].name
                        print(f'{name} is the Winner')
                    else: 
                        print(f"{self.active_players[0].name} and {self.active_players[0].name} drew this game")
                    
                    break
            except:
                pass

