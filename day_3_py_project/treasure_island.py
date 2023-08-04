print("welcome to the treasure island!")
print("your mission is to find the treasure")
journey = input("you are at a cross road, where do you want to go? type 'left' or 'right': ")

if journey == "left":
    lake = input("you come to a lake. there is an island in the middle of the lake. type 'swim' to swim across or "
                 "type 'wait' to wait for a boat: ")
    if lake == "wait":
        island = input("you arrived in the island unharmed. there is a house with 3 doors. one red, one yellow, "
                       "one blue. type the color you chose: ")
        if island == "yellow":
            print("you win!")
        else:
            print("you enterd a home of beasts, game over!")
    else:
        print("can't breath, game over!")
else:
    print("you lost, game over!")