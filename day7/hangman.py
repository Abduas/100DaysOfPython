import hangman_art
import hangman_words
import random
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
end_of_game=False
lives=6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display=[]
for i in range(len(chosen_word)):
    display.append("_")
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you have already guessed {guess}")
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=guess
    else:
        lives=lives-1
        print(f"your guess is "{guess}" which is wrong")
        print(hangman_art.stages[lives])
        if lives==0:
            end_of_game=True
            print("you lose").
    print(f"{' '.join(display)}")
            
      

    if "_" not in display:
        end_of_game=True
        print("you won")
    
    
    