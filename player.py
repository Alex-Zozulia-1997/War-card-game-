
class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []

    def move(self):
        move = self.cards[0]
        print(move)
        return move