
def play(): 
    print("---------------------------------------------------------------")
    print("Welcome to hangman game")
    print("---------------------------------------------------------------")

    secret_word = 'banana'

    lost = False
    win = False

    total_of_attempts = 10

    while(not lost and not win): 
        hint = input('What is the letter?')
        hint = hint.strip().upper()
        
        index = 0
        for letter in secret_word.upper():
            if(hint == letter):
                print('Letter \'{}\' found on position {}'.format(letter,index))
            index = index + 1
            

if(__name__ == "__main__"):
    play()