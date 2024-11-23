import random
import string
import os
import time
score = 0

while True:
    try:
        stop = int(input("What score would you like to play to?"))
        break
    except ValueError:
        print("That's not a valid integer. Please try again.")

start_time = time.time()
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




        