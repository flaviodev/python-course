print("---------------------------------------------------------------")
print("Welcome to divination game")
print("---------------------------------------------------------------")

total_of_attempts = 3
used_remaining_attempts = total_of_attempts
current_attempt = 1
secret_number = 42

for used_remaining_attempts in range(1, used_remaining_attempts +1):
    print("Current attempt: {} of {}".format(current_attempt, total_of_attempts))
    str_hint = input("Type you number: ")
    print("You typed: ", str_hint)

    try:
        hint = int(str_hint)
    except:
        print("You must type a number!")
        exit()

    you_are_right = hint == secret_number
    hint_greater_than = hint > secret_number
    hint_less_than = hint < secret_number

    if(you_are_right):
        print("You're right!")
        exit()
    elif(hint_greater_than):
        print("The hint is greater than secret number!")
    elif(hint_less_than):
        print("The hint is less than secret number!")    

    current_attempt+=1

print("Game over")