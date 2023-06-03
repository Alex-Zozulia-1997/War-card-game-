
class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.current_card = ""
        self.ingame = True
    
    

    def move(self):
        try:
            move = self.cards[0]
            self.current_card = move
            print(move)
            self.cards.remove(self.cards[0])
            
            return move
        except IndexError:
            self.ingame = False
    
    def partake_in_the_war(self):
        try:
            cards = self.cards[0:3]
        except:
            cards =self.cards
        for i in cards:
            self.cards.remove(i)
        return cards