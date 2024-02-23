#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]
for i in range(len(chosen_word)):
    display.append("_")
print(display)
def guessfunc():
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            display[i]=guess
            
    print(display)  

while "_" in display:
    guessfunc()
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
