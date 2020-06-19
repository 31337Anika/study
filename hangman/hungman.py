import random



HANGMAN = ("""
------
|   |
|
|
|
|
|
|
|
---------
""",
"""
------
|   |
|   O   |
|
|
|
|
|
|
---------
""",
"""
------
|   |
|   O   |   -+-
|
|
|
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-
|
|
|
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|
|
|
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|   |
|
|
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|   |
|   |
|
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|   |
|   |
|  |
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|   |
|   |
|  | |
|
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|   |
|   |
|  | |
|  |
|
|
---------
""",
"""
------
|   |
|   O   |   /-+-/
|   |
|   |
|  | |
|  | |
|
|
---------
""")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("TELEPORT","SEX","MAGIC","SPACE","AMERICA","MOUNTANS","INTERPRETATOR","LAPTOP","NEUROSCIENCE","BELARUS")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("welcome to the HANGMAN! GOOD LUCK")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nyou already suggested this letters:\n",used)
    print("\nguessed in the word looks like:\n",so_far)
    guess = input("\n\nEnter a letter:")
    guess = guess.upper()
    while guess in used:
        print("you already suggested this letters",guess)
        guess = input("\n\nEnter the letter:")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\n\nYes! Letter",guess,"is in the word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nUnfortunally here is not letter",guess)
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou are hangman!")
else:
    print("\nYou guessed!")
print("\nHere was a word",word)
