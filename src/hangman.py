import random

def play(): 
    print("---------------------------------------------------------------")
    print("Welcome to hangman game")
    print("---------------------------------------------------------------")

    file = open('words.txt','r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    random_position = random.randrange(0,len(words))

    secret_word = words[random_position].upper()
    successful_letters = []

    for letter in secret_word:
        if(letter==' '):
            successful_letters.append(' ')
        else:
            successful_letters.append('_')

    lost = False
    win = False

    wrong_attempts = 0
    max_wrong_attempts = 6

    while(not lost and not win):
        print_successful_letters = '' 
        for letter in successful_letters:
            print_successful_letters = print_successful_letters + letter + ' '    
        print(print_successful_letters)

        hint = input('What is the letter?')
        hint = hint.strip().upper()
        
        if(hint in secret_word):
            index = 0
            for letter in secret_word:
                if(hint == letter):
                    successful_letters[index] = letter
                index = index + 1
        else: 
            wrong_attempts = wrong_attempts + 1

        win = '_' not in successful_letters
        lost = wrong_attempts == max_wrong_attempts

    if(win):
        print('You hit the secret word:', secret_word)
    else:
        print('You lost the secret word:', secret_word)

if(__name__ == "__main__"):
    play()