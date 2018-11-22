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

if(secret_number == hint):
    print("You're right!")
elif(hint > secret_number):
    print("The hint is grater than secret number!")
else:
    print("The hint is less than secret number!")    
