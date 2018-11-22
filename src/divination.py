print("---------------------------------------------------------------")
print("Welcome to divination game")
print("---------------------------------------------------------------")

secret_number = 42
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
elif(hint_greater_than):
    print("The hint is greater than secret number!")
elif(hint_less_than):
    print("The hint is less than secret number!")    
