import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")

correct_answer=random.randint(1,100)
def easy_number_guess_game():    
    end_the_game=False
    i=10
    while not end_the_game:
        player_answer=int(input("You have " + str(i)+ " attempts to guess the number."))
        if player_answer > correct_answer:
            if i==1:
                print(f"Nevermind you are just unlucky. Correct answer is {correct_answer}")
                end_the_game=True
            else:
                print("Too high.\n Guess again.")
                i-=1
        elif player_answer < correct_answer:
            if i==1:
                print(f"Nevermind you are just unlucky. Correct answer is {correct_answer}")
                end_the_game=True
            else:
                print("Too low.\n Guess again.")
                i-=1
        elif player_answer==correct_answer:
            print("Congradulation! You win!!")
            end_the_game=True
def hard_number_guess_game():    
    end_the_game=False
    i=5
    while not end_the_game:
        player_answer=int(input("You have "+ str(i)+ " attempts to guess the number."))
        if player_answer > correct_answer:
            if i==1:
                print(f"Nevermind you are just unlucky. Correct answer is {correct_answer}")
                end_the_game=True
            else:
                print("Too high.\n Guess again.")
                i-=1
        elif player_answer < correct_answer:
            if i==1:
                print(f"Nevermind you are just unlucky. Correct answer is {correct_answer}")
                end_the_game=True
            else:
                print("Too low.\n Guess again.")
                i-=1
        elif player_answer==correct_answer:
            print("Congradulation! You win!!")
            end_the_game=True

if difficulty=="easy":
    easy_number_guess_game()
elif difficulty=="hard":
    hard_number_guess_game()