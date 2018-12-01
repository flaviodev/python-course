import random

print("---------------------------------------------------------------")
print("Welcome to divination game")
print("---------------------------------------------------------------")

secret_number = random.randrange(1,101) # range 1 to 100
score = 1000


while(1):
    try:
        print("What is the level of difficulty?")
        print("(1) Easy (2) Medium (3) Hard")
        str_level = input("Choice a level: ")
        level = int(str_level)
        if(level >= 1 and level <= 3):
            break
        else:
            raise Exception()
    except:
        print("You must type a valid level!")
        continue

easy = level == 1
medium = level == 2
hard = level == 3

if(easy):
    print("Level: Easy")
    total_of_attempts = 20
elif(medium):
    print("Level: Medium")
    total_of_attempts = 10
elif(hard):
    print("Level: Hard")
    total_of_attempts = 5

for current_attempt in range(1, total_of_attempts +1):
    print("Current attempt: {} of {}".format(current_attempt, total_of_attempts))
    str_hint = input("Type you number: ")
    print("You typed: ", str_hint)

    try:
        hint = int(str_hint)
    except:
        print("You must type a number!")
        continue

    if(hint < 1 or hint > 100):
        print("You must type a number between 1 and 100!")
        continue        

    you_are_right = hint == secret_number
    hint_greater_than = hint > secret_number
    hint_less_than = hint < secret_number

    if(you_are_right):
        print("You're right!")
        print("Your score is ", score)
        break
    else:
        if(hint_greater_than):
            print("The hint is greater than secret number!")
        elif(hint_less_than):
            print("The hint is less than secret number!")    
        error_penalty = abs(secret_number - hint)
        score = score - error_penalty

print("Game over. The secret number was: ", secret_number)