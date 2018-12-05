import random

if(__name__ == "__main__"):
    play()

def play(): 
    lost = False
    won = False
    wrong_attempts = 0
    max_wrong_attempts = 7

    print_welcome()
    secret_word = get_secret_word()
    successful_letters = get_successful_letters(secret_word)

    while(not lost and not won):
        print_successful_letters(successful_letters)

        guess = get_guess()
        
        if(not evaluate_guess(guess,secret_word,successful_letters)):
            wrong_attempts = wrong_attempts + 1
            print_gallows(wrong_attempts)

        won = evaluate_won(successful_letters)
        lost = evaluate_lost(wrong_attempts, max_wrong_attempts)

    if(won):
        print_won_message()
    else:
        print_lost_message(secret_word)

def print_welcome():
    print("---------------------------------------------------------------")
    print("Welcome to hangman game")
    print("---------------------------------------------------------------")

def get_secret_word():
    file = open('words.txt','r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    random_position = random.randrange(0,len(words))

    return words[random_position].upper()
    
def get_successful_letters(secret_word):
    successful_letters = []

    for letter in secret_word:
        if(letter==' '):
            successful_letters.append(' ')
        else:
            successful_letters.append('_')
    
    return successful_letters

def print_successful_letters(successful_letters):
    print_successful_letters = '' 
    for letter in successful_letters:
        print_successful_letters = print_successful_letters + letter + ' '    
    print(print_successful_letters)

def get_guess():
    guess = input('What is the letter?')
    return guess.strip().upper()

def evaluate_guess(guess, secret_word, successful_letters):
    if(guess in secret_word):
        index = 0
        for letter in secret_word:
            if(guess == letter):
                successful_letters[index] = letter
            index = index + 1
        return True
    else: 
        return False    

def evaluate_won(successful_letters):
    return '_' not in successful_letters

def evaluate_lost(wrong_attempts, max_wrong_attempts):
    return wrong_attempts == max_wrong_attempts

def print_lost_message(secret_word):
    print(":( You lost!")
    print("The secret word was {}".format(secret_word))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")

def print_won_message():
    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_gallows(wrongs):
    print("  _______     ")
    print(" |/      |    ")

    if(wrongs == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(wrongs == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (wrongs == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
