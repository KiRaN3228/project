from random import *

def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    else:
        return False

def guess():
    print('Добро пожаловать в числовую угадайку')
    print('Если хотите прекратить игру досрочно, в любой момент напишите "нет"')
    print('Вам необходимо угадать число от 1 до N')
    maxnum = input('Введите число N: ')
    if maxnum == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return
    else:
        maxnum = int(maxnum)
    moneta = randint(1, maxnum)
    flag = True
    count = 1
    while flag:
        n = input(f'Угадайте число от 1 до {maxnum}: ')
        if n == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return

        if is_valid(n):
            n = int(n)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {maxnum}?')

        if n > moneta:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count+= 1
        elif n == moneta:
            print('Вы угадали, поздравляем!')
            print(f'Тебе понадобилось {count} попыток')

            vopros = input('Хотитие сыграть еще раз? (да/нет) ')
            if vopros == 'да':
                guess()
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            flag = False
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1

guess()