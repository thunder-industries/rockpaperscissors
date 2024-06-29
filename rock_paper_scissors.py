import random

user_score = 0
comp_score = 0

options =["rock", "paper", "scissors"]

while True:
    user_input = input ("Type Rock/ Paper/ Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_no =random.randint(0, 2)

    comp_guess = options[random_no]
    print("Computer picked ", comp_guess + ".")

    if user_input == "rock" and comp_guess == "scissors":
        print("You won!")
        user_score += 1
       
    elif user_input == "Paper" and comp_guess == "rock":
        print("You won!")
        user_score += 1
        
    elif user_input == "scissors" and comp_guess == "paper":
        print("You won!")
        user_score += 1
       
    else:
        print('You lost!')
        comp_score += 1
print("user wins", user_score, "times")
print("comp wins", comp_score, "times")
print("Good Game!")

