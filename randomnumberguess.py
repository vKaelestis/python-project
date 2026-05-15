import random


def compare(user_guess, computer_number):
    if user_guess == computer_number:
        return "Congratulations! You guessed the number!"
    elif user_guess < computer_number:
        return "Too low! Try again."
    else:
        return "Too high! Try again."

def play():
    computer_number = random.randint(1, 100)
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= user_guess <= 100:
                result = compare(user_guess, computer_number)
                print(result)
                if result.startswith("Congratulations"):
                    break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play()  

