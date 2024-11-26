import random
import string
import os
import time

#CLEAR SCREEN ----
def clearScreen(cheat,random_string):
    os.system('clear')
    if cheat == 3:
        TP = 1 << 0
        TR = 1 << 1
        TM = 1 << 2
        TI = 1 << 3
        BP = 1 << 4
        BR = 1 << 5
        BM = 1 << 6
        BI = 1 << 7
        IT = 1 << 8
        OT = 1 << 9

        CHORDS = [
            (TP      ,'r'),
            (TR      ,'s'),
            (TM      ,'n'),
            (TI      ,'i'),
            (BP      ,'a'),
            (BR      ,'o'),
            (BM      ,'t'),
            (BI      ,'e'),

            (TP | OT       ,'>'),
            (TR | OT       ,'}'),
            (TM | OT       ,']'),
            (TI | OT       ,')'),
            (BP | OT       ,'<'),
            (BR | OT       ,'{'),
            (BM | OT       ,'['),
            (BI | OT       ,'('),

            (TP | TR      , 'b'),
            (TP | TI      , 'g'),
            (TP | TM      , 'z'),
            (TP | BM      , 'x'),
            (TP | BM | OT , '^'),
            (TP | BI      , 'm'),
            (TP | BI | OT , '$'),
            (TP | BR      , ';'),
            (TP | BR | IT , ':'),
            (TP | BR | OT , 'X'), #Empty

            (TR | TM      , 'p'),
            (TR | TI      , 'f'),
            (TR | BI      , 'v'),
            (TR | BI | OT , '*'),
            (TR | BM      , '/'),
            (TR | BM | IT , '\\'),
            (TR | BM | OT , '|'),
            (TR | BP      , "'"),
            #(TR | BP | IT , '"'),
            #(TR | BP | OT , "`"),

            (TM | TP      , 'y'),
            (TM | BP      , 'j'),
            (TM | BP | OT , '='),
            (TM | BR      , '-'),
            (TM | BR | IT , '_'),
            (TM | BR | OT , '%'),
            (TM | BI      , ','),
            (TM | BI | IT  ,'.'),
            (TM | BI | OT , '~'),

            (TI | BR       , 'k'),
            (TI | BR | OT  , '+'),
            (TI | BP       , 'w'),
            (TI | BP | OT  , '&'),
            (TI | BM       , '?'),
            (TI | BM | IT  , '!'),
            (TI | BM | OT  , 'X'), #empty

            (BP | BR      , 'l'),
            (BM | BI      , 'h'),
            (BR | BM      , 'u'),
            (BP | BM      , 'q'),
            (BP | BI      , 'd'),
            (BR | BI      , 'c')

        ]

        def draw_chord(chord):
            k = lambda chord, key: "X" if chord & key != 0 else "-"
            print('{} {} {} {}   {} {} {} {}\n'
                  '{} {} {} {}   {} {} {} {}\n'
                  '   {} {}   {} {}\n'
            .format(k(chord,TP), k(chord,TR), k(chord,TM), k(chord,TI), k(chord,TI), k(chord,TM), k(chord,TR), k(chord,TP), 
                    k(chord,BP), k(chord,BR), k(chord,BM), k(chord,BI), k(chord,BI), k(chord,BM), k(chord,BR), k(chord,BP),
                                              k(chord,IT), k(chord,OT), k(chord,OT), k(chord,IT)))        
        for i in range(len(random_string)):
            for (chord, key) in CHORDS:
                if key == random_string[i]:
                    draw_chord(chord)


def mainGame(gameChoice,cheat):
    def genString():
        if game == 1:
            random_str = random.choice(string.ascii_letters)
            random_str = random_str.lower()
            return random_str
        if game == 2:
            word_list = ['<', '>', '{', '}', '[', ']', '(', ')', '#', '@', '^', '+', '*', '=', '$', '&', '\\', '/', '|', '-', '_', '%', ':', ';', '?', '!', '.', ',', '~', "'", '"', '`']
            random_str = random.choice(word_list)
            return random_str
        if game == 3:
            word_list = ["time", "love", "game", "word", "free", "fire", "song", "home", 
         "tree", "life", "moon", "star", "hope", "good", "fast", "snow", 
         "wind", "blue", "rain", "dark", "wild", "calm", "warm", "kind", 
         "easy", "hard", "open", "deep", "soft", "true", "just", "pure", 
         "safe", "bold", "even", "fair", "luck", "wise", "rich", "newt"]
            random_str = random.choice(word_list)
            return random_str
        if game ==  4:
            random_str = random.randint(0, 100)
            random_str = str(random_str)
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
        print(f"   SCORE= {score}")
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
                print(f"   SCORE = {score}")
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
    print("Which game would you like to play?\n")
    game = int(input("(1)Char Game\n(2)Sym Game\n(3)Word Game\n(4)Number Game\n"))
    if game not in {1, 2, 3, 4}:
        print("Invalid game!")
    else:
        break
while True:
    print("Would you like cheats?")
    cheat = int(input("(1)No (2)Home Row (3)Combos\n"))
    if cheat not in {1, 2, 3}:
         print("Invalid!")
    else:
        break
mainGame(game,cheat)









        