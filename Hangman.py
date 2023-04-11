import random
import time

# TODO:  something need to have in the code below
# max number of guesses per user 
# add a timer restriction of 30 seconds per user to guess a word
# player should be able to input guesses
# always use from time and the specific function
# try to make
def welcome():

    name = input("""
                ================================================================
                Welcome Guest to the Hangman Game! Please Enter your name:  
                """).capitalize()
    
    #Use a decision making process to accept only alphabets as name
    if name.isalpha() == True:
        print(
                """\n                        >>> Hi!""",name,"""I'm glad to have you here! <<<\n \n 
                Game will start in a second. Thanks for playing.
                ==========================================================
                Good Luck! Have fun playing""")
    else:
        print('Please enter your name using letter only')
        name = input('Enter a game name here:  ')
        print('Hi!',name,'Please go through the rules of the game below')
        print("Use Alphabet only for you name.\n Avoid  using numbers. Thank You!")

hang = ["""
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
welcome()

def get_random_word():
    words = ['boracay', 'vigan', 'palawan', 'bicol', 'manila', 'batangas', 'cebu', 'ifugao',
             'siargao', 'bohol'] # random word in list format

    word = random.choice(words)# selecting word from the variable words
    return word # it will be returned to get_random_word


def board_display(hang, missed_letters, correct_letters, the_secret):
    print(hang[len(missed_letters)])# printing hangman 
    print('Missed Letters:', end=' ') # print the misspelled letters
    
    for letter in missed_letters:
        print(letter, end=' ')
    print("\n")
    print(f'Total of guesses!  {(len(hang)-1)}' )
    
    blanks = '_' * len(the_secret) # it will print the _ or blank lines

    for i in range(len(the_secret)):  # replace blanks with correctly guessed letters
        if the_secret[i] in correct_letters:
            blanks = blanks[:i] + the_secret[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def get_guess(already_guessed):
    time_start = time.time()
    while True:
        guess = input('Guess a letter: ').lower()
        if time.time() - time_start <= max_time:
            if len(guess) != 1: #checking if  user put more than one letter
                print('Please enter a single letter.')
            elif guess in already_guessed: # checking if user guesed the letter that passing int the argument
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz': # checking if user didn't put the letter
                print('Please enter a LETTER.')
            else:
                return guess
        else:
            print("Sorry, time is ended")
        

def play_again():
    play_again =  input("\nDo you want to play again? ").lower().startswith('y')
    return play_again

#Variables
max_time = 30
missed_letters = ''
correct_letters = ''
the_secret = get_random_word()
game_done = False

while True:
    board_display(hang, missed_letters, correct_letters, the_secret) #calling the those variables here
    guess = get_guess(missed_letters + correct_letters)
    if guess in the_secret:
        correct_letters = correct_letters + guess
        found_all_letters = True
        #check if the letters are stored in correct_letters, if not if well set to false
        for i in range(len(the_secret)):
            if the_secret[i] not in correct_letters:
                found_all_letters = False
                break
        #if all letters are correct it will print the correct and game is over
        if found_all_letters:
            print('\nYes! The secret word is "' +
                  the_secret + '"! You have won!')
            game_done = True
    else:
        missed_letters = missed_letters + guess
        # it will print at the end of the game if all guesses are incorrect
        if len(missed_letters) == len(hang) - 1: #max number of guesses based on length of the hangman
            board_display(hang, missed_letters,
                         correct_letters, the_secret)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' +
                  str(len(correct_letters)) + ' correct guesses, the word was "' + the_secret + '"')
            game_done = True
    #if the game is finished and user input y to continue as they want to play it again
    if game_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_done = False
            the_secret = get_random_word()
        else:
            break