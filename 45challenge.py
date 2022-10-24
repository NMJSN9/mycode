#!/usr/bin/python3
""" Looping with for"""


    # farm list with dictionary inside
farms = [{"name": "NE Farm", 
    "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}, 
    {"name": "W Farm", 
    "agriculture": ["pigs", "chickens", "llamas"]},
    {"name": "SE Farm", 
    "agriculture": ["chickens", "carrots", "celery"]}]
    
    #printing animal from NE farm
def loopaloop():
    for amalNE in farms[0].values():
        print(amalNE)
#loopaloop()

"""
NE_animals= farms[0]["agriculture"]

for x in NE_animals:
    print(x) """

def askmeFarm():
    inputFarm = "default"
    while True:
        inputFarm = input("type either NE Farm, W Farm, or SE Farm\n")
        if inputFarm == "NE Farm":
            inputFarm = 0
            break
        elif inputFarm == "W Farm":
            inputFarm = 1
            break
        elif inputFarm == "SE Farm":
            inputFarm = 2
            break
        else:
            print("please enter the exact name, try again")
            continue
    resultFarm = farms[inputFarm]["agriculture"]
    for i in resultFarm:
        print(i)

askmeFarm()
