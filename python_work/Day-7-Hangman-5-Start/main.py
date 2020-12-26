
import replit
import random
import hangman_words
import hangman_art
start = hangman_art.logo

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    replit.clear()

    if guess in chosen_word:
      print(f"you guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
      
    if guess not in chosen_word:
        print(f"you not gussed right {guess}" )
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])