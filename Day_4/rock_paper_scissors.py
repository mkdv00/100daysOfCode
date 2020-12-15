import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def main():
    game_images = [rock, paper, scissors]

    # User choice
    player_choiсe = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'\n"))
    print(f"Your choice: {game_images[player_choiсe]}")

    # Computer choice
    computer_choiсe = random.randint(0, 2)
    print(f"The choice of the computer: {game_images[computer_choiсe]}")

    # Checking winnings
    # rock of the player and paper of the computer.
    if player_choiсe == 0 and computer_choiсe == 1:
        print("You lose.")
    # rock of the computer and paper of the player
    elif computer_choiсe == 0 and player_choiсe == 1:
        print("You win.")
    # paper of the player and scissors of the computer
    elif player_choiсe == 1 and computer_choiсe == 2:
        print("You lose.")
    # paper of the computer and scissors of the player
    elif computer_choiсe == 1 and player_choiсe == 2:
        print("You win.")
    # rock of the computer and scissors of the player
    elif computer_choiсe == 0 and player_choiсe == 2:
        print("You lose.")
    # rock of the player and scissors of the computer
    elif player_choiсe == 0 and computer_choiсe == 2:
        print("You win.")
    else:
        print("You have a draw.")


if __name__ == "__main__":
    main()
