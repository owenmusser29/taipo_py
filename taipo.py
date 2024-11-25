import random
import string
import os
import time

#CLEAR SCREEN ----
def clearScreen(cheat,random_string):
    os.system('clear')
    if cheat == 2:
        print("___________________")
        print("\033[1m|R S N I     I N S R|\033[0m")
        print("\033[1m|A O T E     E T O A|\033[0m")
    if cheat == 3:
        for i in range(len(random_string)):
            if random_string[i] == "a":
                print("|- - - -  A  - - - -|")
                print("|X - - -     - - - X|")
                print("")
            elif random_string[i] == "b":
                print("|X X - -  B  - - X X|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "c":
                print("|- - - -  C  - - - -|")
                print("|- X - X     X - X -|")
                print("")
            elif random_string[i] == "d":
                print("|- - - -  D  - - - -|")
                print("|X - - X     X - - X|")
                print("")
            elif random_string[i] == "e":
                print("|- - - -  E  - - - -|")
                print("|- - - X     X - - -|")
                print("")
            elif random_string[i] == "f":
                print("|- X - X  F  X - X -|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "g":
                print("|X - - X  G  X - - X|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "h":
                print("|- - - -  H  - - - -|")
                print("|- - X X     X X - -|")
                print("")
            elif random_string[i] == "i":
                print("|- - - X  I  X - - -|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "j":
                print("|- - X -  J  - X - -|")
                print("|X - - -     - - - X|")
                print("")
            elif random_string[i] == "k":
                print("|- - - X  K  X - - -|")
                print("|- X - -     - - X -|")
                print("")
            elif random_string[i] == "l":
                print("|- - - -  L  - - - -|")
                print("|X X - -     - - X X|")
                print("")
            elif random_string[i] == "m":
                print("|X - - -  M  - - - X|")
                print("|- - - X     X - - -|")
                print("")
            elif random_string[i] == "n":
                print("|- - X -  N  - X - -|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "o":
                print("|- - - -  O  - - - -|")
                print("|- X - -     - - X -|")
                print("")
            elif random_string[i] == "p":
                print("|- X X -  P  - X X -|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "q":
                print("|- - - -  Q  - - - -|")
                print("|X - X -     - X - X|")
                print("")
            elif random_string[i] == "r":
                print("|X - - -  R  - - - X|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "s":
                print("|- X - -  S  - - X -|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "t":
                print("|- - - -  T  - - - -|")
                print("|- - X -     - X - -|")
                print("")
            elif random_string[i] == "u":
                print("|- - - -  U  - - - -|")
                print("|- X X -     - X X -|")
                print("")
            elif random_string[i] == "v":
                print("|- X - -  V  - - X -|")
                print("|- - - X     X - - -|")
                print("")
            elif random_string[i] == "w":
                print("|- - - X  W  X - - -|")
                print("|X - - -     - - - X|")
                print("")
            elif random_string[i] == "x":
                print("|X - - -  X  - - - X|")
                print("|- - X -     - X - -|")
                print("")
            elif random_string[i] == "y":
                print("|- - X X  Y  X X - -|")
                print("|- - - -     - - - -|")
                print("")
            elif random_string[i] == "z":
                print("|X - X -  Z  - X - X|")
                print("|- - - -     - - - -|")
                print("")


    
    

#CHAR GAME -----
def mainGame(gameChoice,cheat):
    def genString():
        if game == 1:
            random_str = random.choice(string.ascii_letters)
            random_str = random_str.lower()
            return random_str
        if game == 2:
            random_str = chr(random.randint(32, 126))
            random_str = random_str.lower()
            return random_str
        if game == 3:
            word_list = ["time", "love", "game", "word", "free", "fire", "song", "home", 
         "tree", "life", "moon", "star", "hope", "good", "fast", "snow", 
         "wind", "blue", "rain", "dark", "wild", "calm", "warm", "kind", 
         "easy", "hard", "open", "deep", "soft", "true", "just", "pure", 
         "safe", "bold", "even", "fair", "luck", "wise", "rich", "newt"]
            random_str =  random.choice(word_list)
            return random_str

    while True:
        try:
            stop = int(input("What score would you like to play to?"))
            break
        except ValueError:
            print("Try again.")
    start_time = time.time()
    score = 0
    while score < stop:
        random_string = genString()
        points = len(random_string)
        clearScreen(cheat,random_string)
        print(f"TAIPO GAME--SCORE= {score}")
        print(random_string)
        check = False
        while check == False:
            charIn = input()
            if charIn == random_string:
                check = True
                clearScreen(cheat,random_string)
                score = score + points
            else:
                clearScreen(cheat,random_string)
                print(f"TAIPO TYPE GAME -- SCORE = {score}")
                print(random_string)
    end_time = time.time()
    elapsed_time = (end_time - start_time)/60
    print(f"Score: {score}")
    print(f"Time: {elapsed_time}")
    lpm = round(score / elapsed_time)
    print(f"LPM: {lpm}")

#Main ----
os.system('clear')
while True:
    print("Which game would you like to play?")
    game = int(input("(1)Char Game\n(2)ACII Game\n(3)Word Game\n(4)Number Game\n"))
    if game not in {1, 2, 3}:
        print("Invalid game!")
    else:
        break
while True:
    print("Would you like cheats?")
    cheat = int(input("(1)No (2)Home Row (3)Combos"))
    if cheat not in {1, 2, 3}:
         print("Invalid game!")
    else:
        break
mainGame(game,cheat)









        