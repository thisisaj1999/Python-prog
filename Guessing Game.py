from random import randint

print("\n1"
      "Welcome to the 'Guessing World'")


# Rules
def how_to_play():
    print("\nHere's the Rules : ")
    print("\r 1. You have asked for a number.")
    print("\r 2. If it's correct number then you WON the game.")
    print("\r 3. If the number is less than 1 OR greater than 100 it will be OUT OF BONDS.")
    print("\r 4. For the 1st time if the number you guessed is 10 numbers closer to the correct answer then it will "
          "respond 'WARM'.")
    print("\r 5. For the 2nd time or other, If the number is more closer with compare to the last number it will show "
          "Warmer, otherwise it shows Colder\n")
    game_menu()


# Game
def new_game():
    # Print started
    print("Let's go")

    # List which store the previous tries
    box = [0]

    # Random number generate
    num = randint(0, 100)

    # While loop
    while True:

        # Input from the user
        guess = int(input("\nEnter the Number between 1 to 100 : "))

        # To check the input is less than 1 or greater than 100
        if guess < 1 or guess > 100:
            print("Out of Bounds, Please try again!")
            continue

        # To check the input is correct or not, if correct "You Won"
        if guess == num:
            print(f"Congratulations! You Won with {len(box)} number of tries")
            play_again()
            break

        # For store the inputs is list
        box.append(guess)

        # Incorrect input replies
        if box[-2]:
            if abs(num - guess) <= abs(num - box[-2]):
                print("Warmer")
            else:
                print("Colder")

        else:
            if abs(num - guess) <= 10:
                print("Warm")
            else:
                print("Cold")


# play again
def play_again():
    print("\nDo you want to Play Again ?")
    print("\r 1. Start")
    print("\r 2. Main Menu")
    a = int(input("Enter the corresponding number to Proceed : "))

    if a == 1:
        print("\nStarting New Game...")
        new_game()
    elif a == 2:
        print("\nLoading Main Menu...")
        game_menu()


# Game Menu
def game_menu():
    print("\nMain Menu : ")
    print("\r 1. New Game")
    print("\r 2. How to Play")
    print("\r 3. Exit")
    a = int(input("Enter the corresponding number to Proceed : "))

    for i in range(0, 3):
        if a == 1:
            print("\nStarting New Game...")
            new_game()
            break
        elif a == 2:
            print("\nInitializing How to Play...")
            how_to_play()
            break
        elif a == 3:
            print("\nExiting...")
            break


game_menu()
