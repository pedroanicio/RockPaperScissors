import random
import string
from words import words



def get_valid_word(words):
    word = random.choice(words)  # escolhe uma palavra aleatória da lista
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()  # retorna a palavra em maiusculo

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #  letras na palavra
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letras que o usuário vai digitar
    lives = 6

    while len(word_letters)>0 and lives > 0:
        # letras usadas
        print('You have: ', lives, ' lives left and you have used these letters: ', ', '.join(used_letters))

        # mostrar as letras acertadas  
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1 
            if(lives == 5):
               print("O")
            if(lives == 4):
               print("O\nI")
            if(lives == 3):
                print(" O\n/I")
            if(lives == 2):                       # Tentativa de fazer o bonequinho da forca
                print(" O\n/I/")          
            if(lives == 1):
                print(" O\n/I/\n/")
            if(lives == 0):
                print(" O\n/I/\n//")    
                
                print("Letter is not in the word.") 

        elif user_letter in used_letters:
            print('You have already used this letter. Try again.')

        else:
            print("Wrong character. Try again.")
            

    #  finaliza quando len(word_letters) == 0  ou as vidas acabem
    if lives == 0:
        print('you died. The word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()