#Day 1 
#If-else Assignment 
""""Create ston epaper scissor game
"""
player1 = input("Enter player1's value:")
player2= input("Enter player2's value:")


#Condition for paper to Win

if (player1=="stone" and player2 == "paper"):
    print("Paper Winner")

elif (player1=="paper" and player2=="stone"):
    print("Paper Winner")

#---------------------------------------------------
# Conditions for Stone to Win

if (player1=="stone" and player2 == "scissor"):
    print("stone Winner")

elif (player1=="scissor" and player2=="stone"):
    print("stone Winner")

#---------------------------------------------------
#Conditions for Scissor to won

if (player1=="scissor" and player2 == "paper"):
    print( player1,"Winner")

elif (player1=="paper" and player2=="scissor"):
    print(player2,"Winner")

elif (player1==player2):
    print("Draw Match")

print("Thanks for playing! :>")