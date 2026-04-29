import random
def compare(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "it's a tie"
    elif user_choice == "rock" and computer_choice == "paper":
        return "paper wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "rock wins"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "scissors wins"
    else:
        return "invalid input"

def play():
    user_choice = input("Enter rock, paper, or scissors: ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    result = compare(user_choice, computer_choice)
    print(result)
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        play()

if __name__ == "__main__":
    play() 
