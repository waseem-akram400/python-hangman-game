import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2
guess = input("Guess a letter: ").lower()

# TODO-3
if guess in chosen_word:
    print("Right")
else:
    print("Wrong")