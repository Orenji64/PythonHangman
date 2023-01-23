import urllib.request
import random
import webbrowser

response = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
plainlist = response.read().decode()
words = plainlist.splitlines()
wordHistory=[]

def clear():print("\n"*100)

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

def display(fails,word):
    #clear()
    print(man(fails))
    print("Word: "+''.join(displayWord)+"\nFails: "+str(fails))

def win():
    clear()
    print("Success")
    input()

while True:
    while True:
        currentWord=random.choice(words)
        if len(currentWord)>3: break
    wordHistory.append(currentWord)
    wordLetters=[*currentWord]

    displayWord=list("_"*len(currentWord))
    fails=0

    while fails<8:
        success=False
        # Display current status
        display(fails,displayWord)
        # Ask for a letter or word
        attempt=input("Guess a letter or word: ")
        if len(attempt)==1:
            # Check if letter is in the word and update displayWord
            if attempt in displayWord:
                print("Already guessed")
            for i in range(0,len(wordLetters)):
                if wordLetters[i]==attempt:displayWord[i]=attempt;success=True
        else:
            # Check if word guess is correct
            if attempt==currentWord:
                win();success=True
        if success==False:fails+=1
        # Check if the word has been completed
        if ''.join(displayWord)==currentWord:print("success");win()

    input()
