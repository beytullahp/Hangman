import random
with open("words.txt", "r") as file:
    allText = file.read()
    wordsToGuess = list(map(str, allText.split()))
hangman_drawing = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
letters = []
lines = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
game = True
while game:
    mistakes = 0
    word = random.choice(wordsToGuess)
    for i in range(15):
        lines[i] = "_"
    letters.clear()
    play = True
    while play:
        correct = 0
        check = 0
        print(hangman_drawing[mistakes])
        print(*lines[0:len(word)])
        print("Guess a letter:")
        print("Guessed letters:", letters)
        guess = input()
        guess = guess[0].lower()
        if guess in letters:
            print("\nYou have already guessed that letter.")
            continue
        elif not guess.isalpha():
            print("\nPlease input a letter.")
            continue
        else:
            letters.append(guess)
        for i in range(len(word)):
            if guess == word[i]:
                lines[i] = guess
                correct += 1
        if correct == 0:
            mistakes += 1
        if mistakes == 6:
            print(hangman_drawing[mistakes])
            print("You lost. The word was \"{}\". Enter \"y\" to play again:".format(word))
            x = input()
            if x != "y":
                game = False
            play = False
        for i in range(len(word)):
            if lines[i] != "_":
                check += 1
        if check == len(word):
            print(hangman_drawing[mistakes])
            print(*lines[0:len(word)])
            print("You win! Enter \"y\" to play again:")
            x = input()
            if x != "y":
                game = False
            play = False
print("\nThanks for playing!")
