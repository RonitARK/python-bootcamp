
import random as random

chance = 3

for i in range(chance,0,-1):
    num = int(input("Enter your guessed number (1-10): "))
    guess = random.randint(1,10)
    if num == guess:
        print("You guessed the number🥳")
        break
    else:
        print(f"You guessed {num} but it was {guess}🥺😭")
    chance -= 1

if chance == 0:
    print("Sorry, you are out of guesses💔")