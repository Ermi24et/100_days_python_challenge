import random
print("welcome to the rock, paper, and scissors game!")
rock = '''
    ________
---'   _____)
       (______)
       (_____)
       (____)
--'___ (___)
'''
paper = '''
    ---------
---'    _____)___
           ______)
            ________)
            _______)
---'___________)
'''

scissors = '''
    _________
___'     ____)___
        __________)
        ____________)
___     _____}
   '____)
'''

gestures = [rock, paper, scissors]
choice_of_player = int(input("what do you chose? type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
print(gestures[choice_of_player])
choice_of_computer = random.randint(0, 2)
print("choice of compuuter:")
print(gestures[choice_of_computer])
if 3 <= choice_of_player < 0:
    print("Invalid number try again!")
elif choice_of_player == 0 and choice_of_computer == 2:
    print("You win!")
elif choice_of_computer == 0 and choice_of_player == 2:
    print("You lost!")
elif choice_of_computer > choice_of_player:
    print("You lost!")
elif choice_of_computer == choice_of_player:
    print("It is draw!")

