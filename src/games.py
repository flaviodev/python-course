import divination
import hangman

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

divination_game = game == 1
hangman_game = game == 2

if(divination_game):
    divination.play()
elif(hangman_game):
    hangman.play()
