import random



def hangman():
    
word_list = ["вирус", "программа", "компьютер", "хакер", "взлом"]
    
random_number = random.randint(0, 4)
 
word = word_list[random_number]
    
wrong_guesses = 0
    
stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    
remaining_letters = list(word)

    letter_board = ["__"] * len(word)

    win = False

    print('Добро пожаловать на казнь')

    while wrong_guesses < len(stages) - 1:

        print('\n')

        guess = input("Введите букву: ")

        if guess in remaining_letters:

            character_index = remaining_letters.index(guess)

            letter_board[character_index] = guess

            remaining_letters[character_index] = '$'

        else:

            wrong_guesses += 1

        print((' '.join(letter_board)))

        print('\n'.join(stages[0: wrong_guesses + 1]))

        if '__' not in letter_board:

            print('Вы выиграли! Было загадано слово:')

            print(' '.join(letter_board))

            win = True

            break

    if not win:

        print('\n'.join(stages[0: wrong_guesses]))

        print('Вы проиграли! Было загадано слово: {}'.format(word))

hangman()
