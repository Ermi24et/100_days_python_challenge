import random
word_list = ["ardvark", "baboon", "camel", "beekeeper"]
chosen_word = random.choice(word_list)
stages = ["good bye buddy!", "ohhhhh!", "ohhhh!", "ohhh!", "ohh!", "oh!"]
display = []
for j in range(len(chosen_word)):
    display += "_"
lives = 6
end_of_game = False
while not end_of_game:
    guess = (input("guess the letter: ")).lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])
