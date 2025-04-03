import random

word_list = [...]


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):...

def play(word):
    print('Давай играть в угадайку!')
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    word_list = ['_' for c in word]
    print(f'Вам даётся {tries} попыток!')
    print(display_hangman(tries))
    print(*word_list,sep='')
    while not guessed:
        cur_letter = input('Введите букву или слово целиком!')
        cur_letter = cur_letter.upper()
        if cur_letter.isalpha():
            if cur_letter == word:
                print(f'Поздравляем, вы отгадали слово {word}!')
                guessed = True
            elif cur_letter in guessed_letters:
                print('Ты уже отгадал эту букву, попробуй ещё раз!')
            elif cur_letter in word:
                guessed_letters.append(cur_letter)
                for i in range(len(word_list)):
                    if cur_letter == word[i]:
                        word_list[i] = cur_letter
                print(*word_list,sep='')
            else:
                print('Такой буквы нет в слове, ты на шаг ближе к виселице!')
                tries -= 1
                print(display_hangman(tries))
                print(f'У тебя осталось {tries} попыток!')
                if tries == 0:
                    print(f'Ты покойник, загаданное слово было {word}!')
                    print('Конец игры!')
                    break
            if not '_' in word_list:
                guessed = True
                print(f'Вы отгадали слово {word}!')
        else:
            print('Введи букву!')

ans = ''
while ans == '':
    ans = input('Нажмите Enter для начала новой игры!')
    word = get_word(word_list)
    play(word)
