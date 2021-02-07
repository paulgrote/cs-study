import string

secret_word = "tact"

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            test_result = False
            break
        else:
            test_result = True
    
    return test_result



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + '_ '

    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ''

    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters = available_letters + letter

    return available_letters
    
    

def is_char_a_letter(user_input):
    '''
    user_input: string, a single character entered by the user.
    returns: boolean, True if the character entered by the user is a letter;
        False otherwise
    '''
    if user_input in string.ascii_lowercase or user_input in string.ascii_uppercase:
        valid_input = True
    else:
        valid_input = False

    return valid_input



def is_char_duplicate(user_input, letters_guessed):
    '''
    user_input: string, a single character entered by the user when prompted.
    letters_guessed: list of strings, letters which have been guessed so far
    returns: boolean, True if the character entered by the user has already been guessed;
        False otherwise
    '''
    if user_input in letters_guessed:
        is_duplicate = True
    else:
        is_duplicate = False
    
    return is_duplicate



def update_counters(warning_count, guesses_remaining):
  '''
  warning_count: int, the number of warnings remaining
  guesses_remaining: int, the number of guesses remaining
  returns: 
    warning_count: int, the number of warnings remaining
    guesses_remaining: int, the number of guesses remaining
  '''
  warning_count -= 1
  if warning_count == 0:
                print('You used up three warnings. You lose a guess!')
                guesses_remaining -= 1
                warning_count = 3
  print('Warnings remaining:', str(warning_count))
  
  return warning_count, guesses_remaining
  


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    results = []

    if len(my_word) != len(other_word):
      return False
    else:
      i = 0
      for letter in my_word:
        if letter == other_word[i] or letter == '_':
          results.append(True)
        else:
          results.append(False)
        i += 1
    
    print(results)
    if False in results:
      return False
    else:
      return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    print(word for word in wordlist if match_with_gaps(my_word, word) == True)

show_possible_matches('b_ tt_ r')  
  
  
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize variables
    guesses_remaining = 6
    warning_count = 3
    letters_guessed = []
    secret_word_length = len(secret_word)
    score = 0
    
    # Display inital state
    print('Welcome to hangman, ya dummy!',
          '\nI am thinking of a word that is', secret_word_length, 'letters long:',
          '\nYou have', warning_count, 'warnings left.',
          '\n------------'    
    )

    while guesses_remaining > 0:
        print('You have', str(guesses_remaining), 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))

        # Handle user input:
        user_input = input('Guess a letter: ') 
        
        # Conditions that occur depending on whether user enters vaild, invalid, or repeated char
        if is_char_a_letter(user_input) == False:
            print("That's not a letter, ya dummy!")
            warning_count, guesses_remaining = update_counters(warning_count, guesses_remaining)
            status = get_guessed_word(secret_word, letters_guessed)
            print('Status:', status)
        elif is_char_duplicate(user_input.lower(), letters_guessed) == True:
            print("You already guessed "+ user_input.lower() + "!")
            warning_count, guesses_remaining = update_counters(warning_count, guesses_remaining)
            status = get_guessed_word(secret_word, letters_guessed)
            print('Status:', status)
        else:
            letters_guessed.append(user_input.lower())
            status = get_guessed_word(secret_word, letters_guessed)
            if letters_guessed[-1] in secret_word:
                print('Good guess! Status:', status)
            else:
                print('Nope! Status:', status)
                guesses_remaining -= 1
            
        print('--------------')

        # Evaluate end condition
        if is_word_guessed(secret_word, letters_guessed) == True:
          score = guesses_remaining * secret_word_length
          print('Congratulations, you won!',
                '\nYour total score for this game is:', score
          )
          break
        elif guesses_remaining == 0:
          print('You blew it.',
                '\nThe word was:',secret_word
          )

hangman(secret_word)