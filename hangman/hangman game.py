import random
from hangman_wordlist import word_list
from hangman_ascii_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)

display = []
for j in range(len(chosen_word)):
    display += "_"
print(" ".join(display))

d = 0
e = 7

while e > 0 and d == 0:
    c = 0
    guess = input("guess a letter->").lower()

    for a in chosen_word:
        if a == guess:
            display[c] = guess
        c += 1
    print("\n" * 30)
    print(' '.join(display))

    if e == 6 or e == 5 or e == 4 or e == 3 or e == 2 or e == 1 or e == 0:
        print(stages[e])
        if guess not in chosen_word:
            print("\n" * 30)

    if guess not in chosen_word:
        e -= 1
        print(f"you guessed {guess}, that is not in the word. You lose a life.")
        print(stages[e])
        if e == 0:
            print(f"The word was: {chosen_word}")
            print("you lose!")

    if "_" not in display:
        d = 1
        print("you win!")
