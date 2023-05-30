from deck import Deck

class Table():
    def __init__(self):
        deck = Deck()
        self.deck = deck.deck
        self.players = deck.distribute_the_cards()
        self.game_on = True

    def turn(self):
        turn_cards = []
        for i in self.players:
            card = (i.move(), i.name)
            turn_cards.append(card)

        print(turn_cards)
        return turn_cards

    def check_the_highest_card(self,list):
        card_ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        highest_card = 0
        for card in list:  
            rank = card_ranks[card[0].split()[0]]
            print(rank)
            if rank > highest_card:
                highest_card = rank
                winning_card = card
        
        list_of_winners_of_the_turn = []
        for card in list:
            if winning_card[0].split()[0] == card[0].split()[0]:
                list_of_winners_of_the_turn.append(card)
                print(f'{list_of_winners_of_the_turn} this is the list')
        #if len(list_of_winners_of_the_turn) < 1

        print(list_of_winners_of_the_turn[0][1])
        return list_of_winners_of_the_turn[0][1]

    def award(self,winning_player):
        table_cards =[]
        for i in tstack:
            table_cards.append(i[0])
        for i in self.players:
            print(i.name)
            if i.name == winning_player:
                i.cards.extend(table_cards)
                print("yes")
                print(i.cards)
                #seems to work, but need to delete the card from the player's hand as it goes to the move
            


        


    


            

            
            
        



t = Table()
tstack = t.turn()
print(f"this is tstack {tstack}")
t.award(t.check_the_highest_card(tstack))