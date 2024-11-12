# simple python story game to get used to conditional statements as well as logical operators.


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
first_crossroad = input("\tType ""left"" or ""right""\n")

if first_crossroad == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake_checkpoint = input("\tType ""wait"" to wait for a boat. Type ""swim"" to swim across\n")
    if lake_checkpoint == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        three_doors = input("\tone red, one yellow and one blue. Which colour do you choose?\n")
        if three_doors == "yellow":
            print("You Win!")
        elif three_doors == "red":
            print("Burned by fire. Game over")
        elif three_doors == "blue":
            print("Eaten by beasts. Game over")
        else:
            print("Game over")
    else:
        print("Attacked by a trout. Game over")
else:
    print("You fell into a hole. Game over.")