#!/usr/bin/python3
""" Docstrings """


from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clear current dice
        for i in range(3): #make 3 rolls
            self.dice.append(randint(1,6)) # 1 to 6 inclusive

    def get_dice(self): # return the dice rolls
        return self.dice

def main(): # code called at runtime
    
    ## create our player objects
    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    # determin which player won
    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("player 1 wins")
    else:
        print("Player 2 wins")

if __name__ == "__main__":
    main()

