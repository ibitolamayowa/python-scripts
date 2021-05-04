#! python3

import random
import time


Name = input('What is your name? ')
print('Hello there ' + Name + ', Let\'s play a quick guessing game' )
print("Guess a number between 1-10 with only 5 trials")
print("Ready")
time.sleep(0.5)
print("------")
time.sleep(1)
print("Set")
time.sleep(0.5)
print("------")
time.sleep(1)
print("Go!!!")


num = random.randint(1,10)

i = 0
while i < 5:
    i = i + 1
    val = int(input("What is your guess No. " + str(i) + " : "))

    if val == num:
        print("Correct! You got it " + Name + ", and it took you " + str(i) + " guesse(s)")
        break
    elif val > num:
        print("Too High! Try a lesser number")
    else:
        print("Too Low! Try a Greater Number")

if val == num:
    print("Nice Job!")
else:
    print('Trials Exhausted! The correct value is ' + str(num))

print("Closing Program in 3...  ")
time.sleep(1)
print("                   2...  ")
time.sleep(1)
print("                   1...  ")
time.sleep(1)