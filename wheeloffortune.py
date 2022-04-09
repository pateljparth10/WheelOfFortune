import random


player_1_bank = 0
player_2_bank = 0
player_3_bank = 0
player_1_temp_bank =0
player_2_temp_bank =0
player_3_temp_bank =0
global turn_counter 
turn_counter = 0
current_bank = player_1_temp_bank
guess_list = []
word_list = []
vowel_list = ("a","e","i", "o", "u")

def end_turn():
    global turn_counter
    turn_counter += 1
    if turn_counter %3 == 0:
        current_bank = player_1_temp_bank
        print(f"Current Player is Player 1. Current Bank total is : {player_1_temp_bank}")
    elif turn_counter %3 == 1:
        current_bank = player_2_temp_bank
        print(f"Current Player is Player 2. Current Bank total is : {player_2_temp_bank}")
    elif turn_counter %3 == 2:
        current_bank = player_3_temp_bank
        print(f"Current Player is Player 3. Current Bank total is : {player_3_temp_bank}")
    else:
        print("This should not be shown.")



def get_word():
    valid_word = False
    while valid_word == False:
            f = open("C:\Repository\WheelOfFortune\words_alpha.txt","rt")
            word_from_file = f.readlines()
            value = random.randint(0, len(word_from_file))
            global word_guess 
            word_guess = word_from_file.pop(value).strip()
            f.close()
            if word_guess not in word_list:
                word_list.append(word_guess)
                global blank_word 
                blank_word = []
                for i in range(len(word_guess)):
                    blank_word.append("_")
                valid_word = True
    print(blank_word)



def check_vowel_function():
    check_vowel_loop = True
    while check_vowel_loop:
        guess = str(input("Please enter a vowel: "))
        if guess in vowel_list:
            if guess in guess_list:
                print(f"{guess} has already been chosen. The guessed words or letters are {guess_list}. That has ended your turn.")
                check_vowel_loop = False
                end_turn()
            else:
                if(word_guess.find(guess)== -1):
                    guess_list.append(guess)
                    print(guess + " was not in the word. You have lost your turn.")
                    check_vowel_loop = False
                    end_turn()
                else:
                    guess_list.append(guess)
                    for position,letter in enumerate(word_guess):
                        if (letter == guess):
                            blank_word[position] = guess
                    print(blank_word)
                    check_vowel_loop = False
        else:
            print("That is not a vowel. You lose your turn.")
            end_turn()
            check_vowel_loop = False

def check_consonant_function():
    check_consonant_loop = True
    while check_consonant_loop:
        guess = str(input("Please enter a consonant: "))
        if guess not in vowel_list:
            if guess in guess_list:
                print(f"{guess} has already been chosen. The guessed words or letters are {guess_list}. That has ended your turn.")
                check_consonant_loop = False
                end_turn()
            else:
                if(word_guess.find(guess)== -1):
                    guess_list.append(guess)
                    print(guess + " was not in the word. You have lost your turn.")
                    check_consonant_loop = False
                    end_turn()
                else:
                    guess_list.append(guess)
                    for position,letter in enumerate(word_guess):
                        if (letter == guess):
                            blank_word[position] = guess
                    print(blank_word)
                    check_consonant_loop = False
        else:
            print("That is not a consonant. You lose your turn.")
            end_turn()
            check_consonant_loop = False


get_word()
check_vowel_function()
check_consonant_function()