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

            (TM | BP      , 'j'),
            (TM | BP | OT , '='),
            (TM | BR      , '-'),
            (TM | BR | IT , '_'),
            (TM | BR | OT , '%'),
            (TM | BI      , ','),
            (TM | BI | IT  ,'.'),
            (TM | BI | OT , '~'),

            (TI | TM       , 'y'),
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
            word_list = [
    "able", "acid", "aged", "air", "arms", "bark", "ball", "band", "base", "bath", 
    "bear", "beat", "bell", "belt", "bird", "boat", "bold", "bomb", "bond", "book", 
    "boot", "boss", "both", "bowl", "busy", "call", "calm", "card", "care", "carp", 
    "cast", "cash", "cell", "chip", "chop", "class", "clip", "club", "coat", "code", 
    "cool", "core", "cost", "crab", "crop", "cure", "dark", "dawn", "dear", "deal", 
    "dust", "doll", "dogs", "dive", "dome", "door", "draw", "drop", "dust", "duty",
    "east", "echo", "else", "even", "ever", "evil", "exam", "face", "fact", "fair",
    "fast", "fear", "feet", "fell", "file", "find", "fire", "fish", "five", "flat",
    "flow", "fold", "food", "foot", "form", "fort", "from", "full", "fund", "game",
    "gain", "gate", "give", "goal", "gold", "good", "grip", "grow", "gulf", "hair",
    "half", "hand", "hard", "hare", "have", "hear", "heat", "help", "here", "hide",
    "high", "hill", "hint", "hire", "hole", "holy", "hook", "hope", "horn", "hour",
    "hush", "idea", "idle", "inch", "into", "iron", "isle", "item", "jack", "jane",
    "jars", "jean", "join", "joke", "jour", "jump", "just", "keen", "keep", "kill",
    "king", "kiss", "kite", "knee", "knob", "knot", "land", "last", "late", "lava",
    "lawn", "lead", "left", "lend", "less", "life", "like", "line", "link", "lion",
    "list", "live", "load", "lock", "long", "look", "lost", "loud", "luck", "made",
    "mail", "make", "mall", "map", "mask", "mass", "mate", "math", "mead", "meal",
    "mean", "meat", "mine", "mint", "mock", "mode", "more", "move", "much", "must",
    "name", "near", "neck", "need", "nest", "note", "noun", "only", "open", "oral",
    "over", "pace", "pack", "pale", "palm", "park", "part", "pass", "path", "pause",
    "peak", "peer", "pick", "pipe", "plan", "play", "plow", "plug", "poll", "pool",
    "poor", "port", "post", "pull", "pure", "push", "race", "rack", "rage", "rail",
    "rain", "rake", "rare", "rate", "read", "reef", "rest", "ride", "ring", "risk",
    "roll", "roof", "room", "root", "rose", "rude", "rush", "salt", "same", "sand",
    "save", "seas", "seat", "sell", "send", "sent", "serve", "sett", "sew", "show",
    "sick", "side", "sign", "sink", "site", "skin", "skip", "slip", "slow", "slot",
    "snow", "soft", "sole", "song", "soon", "sort", "soul", "spin", "spot", "stab",
    "star", "step", "stop", "store", "stow", "stun", "sure", "swim", "take", "talk",
    "task", "team", "tear", "tell", "term", "test", "than", "that", "then", "they",
    "thin", "this", "thus", "time", "tone", "tool", "tore", "tour", "town", "trap",
    "tree", "trip", "true", "turn", "tune", "unit", "used", "user", "vary", "veal",
    "very", "vote", "vows", "wait", "wake", "wall", "want", "warn", "warp", "wash",
    "weak", "weal", "wear", "week", "weep", "well", "west", "what", "when", "whip",
    "whom", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wipe", "wish",
    "with", "wood", "word", "work", "worn", "wrap", "yarn", "yell", "yes", "yoga",
    "zone", "zoom"
]
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









        