
def play(): 
    print("---------------------------------------------------------------")
    print("Welcome to hangman game")
    print("---------------------------------------------------------------")

    secret_word = 'banana'
    successful_letters = []

    for letter in secret_word:
        successful_letters.append('_')

    lost = False
    win = False

    total_of_attempts = 10

    while(not lost and not win):
        print_successful_letters = '' 
        for letter in successful_letters:
            print_successful_letters = print_successful_letters + letter + ' '    
        print(print_successful_letters)

        hint = input('What is the letter?')
        hint = hint.strip().upper()
        
        index = 0
        for letter in secret_word.upper():
            if(hint == letter):
                successful_letters[index] = letter
                print('Letter \'{}\' found on position {}'.format(letter,index))
            index = index + 1
            

if(__name__ == "__main__"):
    play()