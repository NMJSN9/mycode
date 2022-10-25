#!/usr/bin/python3
""" Docstrings """

from cheatdice import *

def main():
    
    better = Cheat_Better()
    loaded_dice = Cheat_Loaded_Dice()

    better_score = 0
    loaded_dice_score = 0
    
    # how manygames we want to run
    number_of_games = 100000
    game_number = 0

    print("Simulation RUnning!")
    print("================")

    while game_number < number_of_games:
        better.roll()
        loaded_dice.roll()
        better.cheat()
        loaded_dice.cheat()

        if sum(better.get_dice()) == sum(loaded_dice.get_dice()):
            pass
        elif sum(better.get_dice()) > sum(loaded_dice.get_dice()):
            #print(:Dice wapper wins!:)
            better_score += 1 
        else: 
            #print("Loaded dice wins!")
            loaded_dice_score += 1
        game_number += 1

# the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"better won: {better_score}")
    print(f"Loaded dice won: {loaded_dice_score}")

    # determine the winner
    if better_score == loaded_dice_score:
        print("Game was drawn")
    elif better_score > loaded_dice_score:
        print("better won most games")
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()

