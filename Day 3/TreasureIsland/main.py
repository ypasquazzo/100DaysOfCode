# Build the Treasure Island game using the logic detailed in this flow chart:
# https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

print("You have reached a crossroad.\n")
choice = input("Do you want to go (L)eft or (R)ight? ")
if choice == "L":
    print("You have reached the shore, the island is in sight!\n")
    choice = input("Do you want to (S)wim or (W)ait for a boat? ")
    if choice == "W":
        print("A boat safely took you to the island.\n")
        print("You see a building with 3 doors: a (R)ed, a (B)lue and a (Y)ellow.")
        choice = input("Which door do you open? ")
        if choice == "R":
            print("You are burned by the fire.\nGame Over!")
        elif choice == "B":
            print("You are eaten by a beast.\nFame Over!")
        elif choice == "Y":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("You are attacked by a trout. \nGame Over!")
else:
    print("You fall into a hole.\nGame Over!")
