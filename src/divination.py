print("---------------------------------------------------------------")
print("Welcome to divination game")
print("---------------------------------------------------------------")

total_of_attempts = 3
secret_number = 42

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
        break
    elif(hint_greater_than):
        print("The hint is greater than secret number!")
    elif(hint_less_than):
        print("The hint is less than secret number!")    


print("Game over")