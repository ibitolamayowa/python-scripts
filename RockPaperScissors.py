import random
import time


def winner():
    if CompScore == 3:
        print("\nComputer scored 3 points \nComputer Wins!")
        return True

    elif PlayerScore == 3:
        print("\n" + name + " scored 3 points \n" + name + " Wins!")
        return True

    else:
        return False


def score():
    print("Your score: " + str(PlayerScore))
    print("Computer's Score: " + str(CompScore))


print("Rock, Paper, Scissors Game")
print("First to 3 wins!")
time.sleep(0.5)
print("-------------------------------------Ready--------------------------------------")
time.sleep(0.5)
print("--------------------------------------Set----------------------------------------")
time.sleep(0.5)
print("--------------------------------------Go!--------------------------------------")

options = ['rock', 'paper', 'scissors']

PlayerScore = 0
CompScore = 0

name = input("Name: ")
print("Welcome " + name)

while True:
    if winner() is True:
        break

    index = random.randint(0, 2)
    CompChoice = options[index]

    PlayerChoice = input("Input Rock Paper or scissors: ")
    PlayerChoice = str(PlayerChoice)
    PlayerChoice = PlayerChoice.lower()

    print("You chose: " + PlayerChoice)
    print("Computer chose: " + CompChoice)

    if CompChoice == PlayerChoice:
        print("It's a tie")

    elif PlayerChoice == 'rock' and CompChoice != 'paper':
        print("Player won.. ")
        print("Computer lost...")
        PlayerScore += 1
        score()
        winner()

    elif PlayerChoice == 'scissors' and (CompChoice == 'paper'):
        print("Player won.. ")
        print("Computer lost...")
        PlayerScore += 1
        score()
        winner()

    elif PlayerChoice == 'paper' and (CompChoice == 'rock'):
        print("Player won.. ")
        print("Computer lost...")
        PlayerScore += 1
        score()
        winner()

    elif CompChoice == 'rock' and PlayerChoice != 'rock':
        print("Computer won.. ")
        print("Player lost...")
        CompScore += 1
        score()
        winner()

    elif CompChoice == 'scissors' and (PlayerChoice != 'rock' or PlayerChoice != 'scissors'):
        print("Computer won.. ")
        print("Player lost...")
        CompScore += 1
        score()
        winner()

    elif CompChoice == 'paper' and PlayerChoice == 'rock':
        print("Computer won.. ")
        print("Player lost...")
        CompScore += 1
        score()
        winner()

    else:
        print("Something is wrong")
