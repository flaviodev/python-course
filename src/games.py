import random

print("---------------------------------------------------------------")
print("Choose the game")
print("---------------------------------------------------------------")

while(1):
    try:
        print("Which game do you want to play?")
        print("(1) Divination (2) Hangman")
        str_game = input("Choose a game: ")
        game = int(str_game)
        if(game >= 1 and game <= 2):
            break
        else:
            raise Exception()
    except:
        print("You must type a valid game!")
        continue

divination = game == 1
hangman = game == 2

if(divination):
    print("Divination")
elif(hangman):
    print("hangman")
