#!/usr/bin/env python3
"""Alta3 Research | Joseph
   Bottles couting """

inputNum = int(input("type your desire beer bottles:\n"))


if inputNum >= 100:
    print("You can't afford more than 99 bottles")
else: 
    for num in range(0, inputNum):
        print(f"{inputNum-num} bottles of the beer on the wall!\n{inputNum-num} bottles of beer on the wall! {inputNum-num} bottles of beer! You take one down, pass it around!")
