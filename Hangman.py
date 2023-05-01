import urllib.request
import random
import webbrowser
import os

response = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
plainlist = response.read().decode()
words = plainlist.splitlines()
wordHistory=[]

def clear():print("\n"*100);os.system('cls')

def man(f):
    frames= [
        "\n\n\n\n\n\n\n________",
        "\n│\n│\n│\n│\n│\n│\n│_______",
        "_____\n│\n│\n│\n│\n│\n│\n│_______",
        "_____\n│   │\n│   ☺\n│\n│\n│\n│\n│_______",
        "_____\n│   │\n│   ☺\n│   |\n│   |\n│\n│\n│_______",
        "_____\n│   │\n│   ☺\n│  /|\n│ / |\n│\n│\n│_______",
        "_____\n│   │\n│   ☺\n│  /|\\\n│ / | \\\n│\n│\n│_______",
        "_____\n│   │\n│   ☺\n│  /|\\\n│ / | \\\n│  /\n│ /\n│_______",
        "_____\n│   │\n│   ☺\n│  /|\\\n│ / | \\\n│  / \\\n│ /   \\\n│_______"
    ]
    return frames[f]

def display(fails,letters,word):
    clear()
    print(man(fails)+"\n")
    print("Word: "+''.join(displayWord))
    print("Fails: ",end='')
    for i in letters:print(i.upper(),end=', ')
    print("\n")

def win(currentWord):
    clear()
    print("Success! The word was "+currentWord)
    input()
def lose(ans):
    #clear()
    print("You lost. The word was "+ans)
    input()

while True:
    while True:
        currentWord=random.choice(words).lower()
        if len(currentWord)>3: break
    wordHistory.append(currentWord)
    wordLetters=[*currentWord]

    displayWord=list("_"*len(currentWord))
    failedLetters=[]
    fails=0

    while fails<8:
        success=False
        # Display current status
        display(fails,failedLetters,displayWord)
        # Ask for a letter or word
        attempt=input("Guess a letter or word: ").lower()
        if len(attempt)==1:
            # Check if letter is in the word and update displayWord
            if (attempt in failedLetters) or (attempt in displayWord):
                print("Already guessed")
            for i in range(0,len(wordLetters)):
                if wordLetters[i]==attempt:displayWord[i]=attempt;success=True
        else:
            # Check if word guess is correct
            if attempt==currentWord:
                win();success=True
        if success==False:fails+=1;failedLetters.append(attempt)
        # Check if the word has been completed
        if ''.join(displayWord)==currentWord:win();success=True
    if won==True:win()
    else: lose(currentWord)
    input()
input()
