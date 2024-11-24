import random
import string
import os
import time

#CHAR GAME -----
def charGame():
    while True:
        try:
            stop = int(input("What score would you like to play to?"))
            break
        except ValueError:
            print("That's not a valid integer. Please try again.")
    start_time = time.time()
    score = 0
    while score < stop:
        os.system('clear')
        print(f"TAIPO TYPE GAME -- SCORE = {score}")

        random_character = random.choice(string.ascii_letters)
        print(random_character)
        check = False
        while check == False:
            charIn = input()
            if charIn == random_character:
                check = True
                os.system('clear')
                score += 1
            else:
                os.system('clear')
                print(f"TAIPO TYPE GAME -- SCORE = {score}")
                print(random_character)
    end_time = time.time()
    elapsed_time = (end_time - start_time)/60
    print(f"Score: {score}")
    print(f"Time: {elapsed_time}")
    lpm = round(score / elapsed_time)
    print(f"LPM: {lpm}")

#ASCII GAME---
def asciiGame():
    while True:
        try:
            stop = int(input("What score would you like to play to?"))
            break
        except ValueError:
            print("That's not a valid integer. Please try again.")
    start_time = time.time()
    score = 0
    while score < stop:
        os.system('clear')
        print(f"TAIPO TYPE GAME -- SCORE = {score}")

        random_ascii = chr(random.randint(32, 126))
        print(random_ascii)
        check = False
        while check == False:
            charIn = input()
            if charIn == random_ascii:
                check = True
                os.system('clear')
                score += 1
            else:
                os.system('clear')
                print(f"TAIPO TYPE GAME -- SCORE = {score}")
                print(random_ascii)
    end_time = time.time()
    elapsed_time = (end_time - start_time)/60
    print(f"Score: {score}")
    print(f"Time: {elapsed_time}")
    lpm = round(score / elapsed_time)
    print(f"LPM: {lpm}")

#WORD GAME ----
def wordGame():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    while True:
        try:
            stop = int(input("What score would you like to play to?"))
            break
        except ValueError:
            print("That's not a valid integer. Please try again.")
    start_time = time.time()
    score = 0
    while score < stop:
        os.system('clear')
        print(f"TAIPO TYPE GAME -- SCORE = {score}")
        random_word = random.choice(word_list)
        print(random_word)
        check = False
        while check == False:
            charIn = input()
            if charIn == random_word:
                check = True
                os.system('clear')
                length = len(random_word)
                score = score + length
            else:
                os.system('clear')
                print(f"TAIPO TYPE GAME -- SCORE = {score}")
                print(random_word)
    end_time = time.time()
    elapsed_time = (end_time - start_time)/60
    print(f"Score: {score}")
    print(f"Time: {elapsed_time}")
    lpm = round(score / elapsed_time)
    print(f"LPM: {lpm}")

#Main -----
print("Which game would you like to play?")
game = 99
while game > 3:
        os.system('clear')
        game = int(input("(1)Char Game (2)ACII Game (3)Word Game"))
if game == 1:
    charGame()
if game == 2:
    asciiGame()
if game == 3:
    wordGame()







        