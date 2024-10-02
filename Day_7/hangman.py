import random 
from Day_7.hangman_words import hangman_words
from Day_7.hangman_art import hangman_pics, logo
#randomly picks a word from word_list
#user guesses a letter --> lower case
#if certain letter in word --> replace blank spaces with letter
# if not --> start building the hangman
#games ends if the hangman is complete OR no more blank spaces


random_word = random.choice(hangman_words)
# print(random_word)

print(logo)

blank_space_word = ''
for _ in range(len(random_word)):
    blank_space_word += '_'
print(f"Word to guess: {blank_space_word} \n")


game_over = False
correct_letters = []

user_lives = 6

while not game_over:

    print(f'*********************** {user_lives}/6 LIVES LEFT *********************** \n')

    guessed_letter = input('Guess a letter: ').lower() 
    display_word = ''

    if guessed_letter in correct_letters:
        print(f"You've already guessed {guessed_letter}")

    for letter in random_word:
        if letter == guessed_letter:
            display_word += guessed_letter
            correct_letters.append(guessed_letter)     
        elif letter in correct_letters:
            display_word += letter
        else:
            display_word += '_'
    print(display_word)
    
    if guessed_letter not in random_word:
        user_lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life \n")
        if user_lives == 0:
            game_over = True
            print(f'***********************IT WAS {random_word}! YOU LOSE!***********************')


    if '_' not in display_word:
        game_over = True
        print('***********************YOU WIN!***********************')

    print(hangman_pics[user_lives])

