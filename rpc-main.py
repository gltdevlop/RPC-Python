import random

print("Let's play Rock Paper Scissors !")


ai_guess = random.randint(1, 3)
choices = {1: "Paper", 2: "Rock", 3: "Scissors"}
player_guess = input("Enter 1 if you chosse Paper \nEnter 2 if you choose Rock \nEnter 3 if you choose scissors"
                     "\nYour guess : ")

player_guess_int = int(player_guess)

try:
    player_guess_int = int(player_guess)

    if player_guess_int < 1 or player_guess_int > 3:
        print("Invalid choice! Please enter 1, 2, or 3.")
    else:
        print(f"You chose: {choices[player_guess_int]}")

        if player_guess_int == ai_guess:
            print("Tie!")
        elif (player_guess_int == 1 and ai_guess == 3):
            print("AI won! You chose Paper and AI chose Scissors.")
        elif (player_guess_int == 2 and ai_guess == 1):
            print("AI won! You chose Rock and AI chose Paper.")
        elif (player_guess_int == 3 and ai_guess == 2):
            print("AI won! You chose Scissors and AI chose Rock.")
        else:
            print("You won! You chose {choices[player_guess_int]} and AI chose {choices[ai_guess]}.")

except ValueError:
    print("Please enter a valid number.")
