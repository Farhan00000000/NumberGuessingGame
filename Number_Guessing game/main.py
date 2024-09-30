import random
from art import art

decision = False
while not decision:

    print(f"{art}\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    a_ran_num = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        print("You have 10 attempts remaining to guess the number.")

        n = 10

        for i in range(n):

            user = int(input("Make a guess: "))
            if i == 9:
                decision = True
                print(f"Too low.\nYou've run out of guesses, the answer was {a_ran_num}.\nYou lose.")
                break

            elif user == a_ran_num:

                print(f"You got it! The answer was {a_ran_num}. You win.")

                decision = True
                break

            elif user > a_ran_num:

                print(f"Too high.\nGuess again.\nYou have {9 - i} attempts remaining to guess the number.")

            elif user < a_ran_num:

                print(f"Too low.\nGuess again.\nYou have {9 - i} attempts remaining to guess the number.")

            else:
                print("Something went wrong")

    else:
        print("You have 5 attempts remaining to guess the number.")

        for i in range(5):

            user = int(input("Make a guess: "))
            if i == 4:
                decision = True
                print(f"Too low.\nYou've run out of guesses, the answer was {a_ran_num}.\nYou lose.")
                break

            elif user == a_ran_num:

                print(f"Yoy got it! The answer was {a_ran_num}. You win.")

                decision = True
                break
            elif user > a_ran_num:

                print(f"Too high.\nGuess again.\nYou have {4 - i} attempts remaining to guess the number.")

            elif user < a_ran_num:

                print(f"Too low.\nGuess again.\nYou have {4 - i} attempts remaining to guess the number.")


            else:
                print("Something went wrong")

#
# from random import randint
# from art import art
# #
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS
#
# def game():
#   print(art)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}")
#
#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))
#
#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
#
# game()
#


# # Describe Problem
