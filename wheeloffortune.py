import random


player_1_bank = 0
player_2_bank = 0
player_3_bank = 0
player_1_temp_bank =100
player_2_temp_bank =500
player_3_temp_bank =1000
turn_counter = 0
current_bank = player_2_temp_bank
guess_list = []
word_list = []
vowel_list = ("a","e","i", "o", "u")

def end_turn():
    global turn_counter
    global current_bank
    turn_counter += 1
    if turn_counter %3 == 0:
        current_bank = player_1_temp_bank
        print(f"Current Player is Player 1. Current Bank total is : ${player_1_temp_bank}")
    elif turn_counter %3 == 1:
        current_bank = player_2_temp_bank
        print(f"Current Player is Player 2. Current Bank total is : ${player_2_temp_bank}")
    elif turn_counter %3 == 2:
        current_bank = player_3_temp_bank
        print(f"Current Player is Player 3. Current Bank total is : ${player_3_temp_bank}")
    else:
        print("This should not be shown.")

def wheel_spin():
    wheel = ["Bankrupt","Lose a Turn",100,150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700,
    750, 800, 850, 900]
    spin = random.randint(0, len(wheel)-1)
    return wheel[spin]


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
    global player_1_temp_bank
    global player_2_temp_bank
    global player_3_temp_bank
    global turn_counter
    while check_consonant_loop:
        spin = wheel_spin()
        global current_bank
        if spin == "Bankrupt":
            print("You landed on Bankrupt! You lose your money and your turn.")
            current_bank = 0
            if turn_counter %3 == 0:
                player_1_temp_bank = current_bank
            elif turn_counter %3 ==1:
                player_2_temp_bank = current_bank
            elif turn_counter %3 == 2:
                player_3_temp_bank = current_bank
            end_turn()
            check_consonant_loop = False
        elif spin == "Lose a Turn":
            print("You landed on Lose a Turn! Your turn ends.")
            end_turn()
            check_consonant_loop = False
        else:
            print(f"You landed on ${spin}")
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
                        letters = 0
                        for position,letter in enumerate(word_guess):
                            if (letter == guess):
                                blank_word[position] = guess
                                letters += 1
                        print(blank_word)
                        current_bank += spin * letters
                        print(f"Your current bank total is: ${current_bank}")
                        check_consonant_loop = False
            else:
                print("That is not a consonant. You lose your turn.")
                end_turn()
                check_consonant_loop = False


def guess_the_word():
    global turn_counter
    global player_1_bank
    global player_2_bank
    global player_3_bank
    global current_bank
    global player_1_temp_bank
    global player_2_temp_bank
    global player_3_temp_bank
    word_user_guesses = input("Enter your guess for the word: ")
    if word_user_guesses == word_guess:
        print("Congratulations! That is correct!")
        if turn_counter %3 == 0:
           player_1_bank += current_bank
        elif turn_counter %3 == 1:
            player_2_bank += current_bank
        elif turn_counter %3 == 2:
            player_3_bank += current_bank
        player_1_temp_bank = 0
        player_2_temp_bank = 0
        player_3_temp_bank = 0
        print(f"Player 1 bank: ${player_1_bank}")
        print(f"Player 2 bank: ${player_2_bank}")
        print(f"Player 3 bank: ${player_3_bank}")
        return False

    else:
        print("That is not correct. You lose your turn.")
        end_turn()
        return True

def buy_vowel():
    global current_bank
    if current_bank < 250:
        print("You do not have enough money in your bank account to buy a vowel!")
    else:
        check_vowel_function()
        current_bank -= 250
        print(f"Your current total in your bank is: ${current_bank}")

def final_round():
    global player_1_bank
    global player_2_bank
    global player_3_bank
    final_round_bank = 0
    final_round_player_winning = 10000
    if player_1_bank > player_2_bank and player_1_bank > player_3_bank:
        print("Congratulation Player 1! You are in the final round.")
        final_round_bank = player_1_bank
    elif player_2_bank > player_1_bank and player_2_bank > player_3_bank:
        print("Congratulation Player 2! You are in the final round.")
        final_round_bank = player_2_bank
    elif player_3_bank > player_1_bank and player_3_bank > player_2_bank:
        print("Congratulation Player 3! You are in the final round.")  
        final_round_bank = player_3_bank
    get_word()
    print("We are giving you the letters R, S, T, L, N, E")
    final_round_guess = "r"
    for position,letter in enumerate(word_guess):
        if (letter == final_round_guess):
            blank_word[position] = final_round_guess
    final_round_guess = "s"
    for position,letter in enumerate(word_guess):
        if (letter == final_round_guess):
            blank_word[position] = final_round_guess
    final_round_guess = "t"
    for position,letter in enumerate(word_guess):
        if (letter == final_round_guess):
            blank_word[position] = final_round_guess
    final_round_guess = "l"
    for position,letter in enumerate(word_guess):
        if (letter == final_round_guess):
            blank_word[position] = final_round_guess
    final_round_guess = "n"
    for position,letter in enumerate(word_guess):
        if (letter == final_round_guess):
            blank_word[position] = final_round_guess
    final_round_guess = "e"
    for position,letter in enumerate(word_guess):
        if (letter == final_round_guess):
            blank_word[position] = final_round_guess
    print(blank_word)
    print(word_guess)
    print("Please choose 3 consonants and 1 vowel.")
    consonant_guess_1 = input("Please choose your first consonant: ")
    for position,letter in enumerate(word_guess):
        if (letter == consonant_guess_1):
            blank_word[position] = consonant_guess_1
    
    consonant_guess_2 = input("Please choose your second consonant: ")
    for position,letter in enumerate(word_guess):
        if (letter == consonant_guess_2):
            blank_word[position] = consonant_guess_2

    consonant_guess_3 = input("Please choose your third consonant: ")
    for position,letter in enumerate(word_guess):
        if (letter == consonant_guess_3):
            blank_word[position] = consonant_guess_3

    vowel_guess = input("Please choose your vowel: ")
    for position,letter in enumerate(word_guess):
        if (letter == vowel_guess):
            blank_word[position] = vowel_guess
    print(blank_word)
    print("You have one guess to win the final round.")
    final_guess = input("What is your guess? ")
    if final_guess == word_guess:
        final_round_bank += final_round_player_winning
        print(f"Congratulation! That is correct you win ${final_round_player_winning}")
        print(f"You won a total of ${final_round_bank}")
    else:
        print(f"Unfortunately, that is incorrect, but you won a total of ${final_round_bank}")
    


final_round()

# wheel_of_fortune_menu_loop_round_1 = True
# get_word()
# print(word_guess)
# while wheel_of_fortune_menu_loop_round_1:
#     print("ROUND 1")
#     print("Please choose one of the following: ")
#     print("1. Spin the wheel and guess a consonant.")
#     print("2. Buy a vowel for $250")
#     print("3. Guess the word")
#     choice = input("What will you be doing? [1] [2] or [3] ")
#     if choice == "1":
#         check_consonant_function()
#     elif choice == "2":
#         buy_vowel()
#     elif choice == "3":
#         wheel_of_fortune_menu_loop_round_1 = guess_the_word()
#     else:
#         print("That is not a valid choice.")
    
# get_word()
# print(word_guess)
# wheel_of_fortune_menu_loop_round_2 = True
# while wheel_of_fortune_menu_loop_round_2:
#     print("ROUND 2")
#     print("Please choose one of the following: ")
#     print("1. Spin the wheel and guess a consonant.")
#     print("2. Buy a vowel for $250")
#     print("3. Guess the word")
#     choice = input("What will you be doing? [1] [2] or [3] ")
#     if choice == "1":
#         check_consonant_function()
#     elif choice == "2":
#         buy_vowel()
#     elif choice == "3":
#         wheel_of_fortune_menu_loop_round_2 = guess_the_word()
#     else:
#         print("That is not a valid choice.")



