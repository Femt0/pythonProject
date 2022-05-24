from random import randint


def is_valid():
    return 1 <= int(n) <= 100


secret_number = randint(1, 100)
counter = 0
s = ''
print('''Добро пожаловать в игру "Угадайка".
Доступные команды: start, stop, help, hint''')
while True:
    s = input('Введите команду: ')
    if s == 'help':
        print('''start - начинает игру
stop - заканчивает игру
help - информация о всех коммандах
hint - дает подсказку
hint и stop доступны только во время игры''')
    elif s == 'stop':

        print('Команда доступна только во время игры')
    elif s == 'hint':
        print('Команда доступна только во время игры')
    elif s == 'start':
        print('Начинаю игру...')
        break
    else:
        print('Неизвестная команда')

while True:
    n = input('Угадайте число от 1 до 100: ')
    if n == 'stop':
        print('Игра закончена')
        break
    elif n == 'hint':
        if secret_number < 6:
            print(f'Число в диапозоне от 1 до 10')
        elif secret_number > 95:
            print('Число в диапозоене от 90 до 100')
        else:
            print(f'Число в диапозоне от {secret_number - 5} до {secret_number + 5}')
    elif is_valid():
        counter += 1
        if secret_number == int(n):
            print('Вы угадали, поздравляем!')
            print(f'Вы сделали попыток - {counter}')
            choice = input('Хотите сыграть еще?(да, нет) ')
            if choice.lower() == 'да':
                secret_number = randint(1, 100)
                counter = 0
                continue
            else:
                print('Завершаю игру...')
                break

        elif int(n) < secret_number:
            print('Слишком мало, попробуйте еще раз')
        elif int(n) > secret_number:
            print('Слишком много, попробуйте еще раз')
    else:
        print('Введите число от 1 до 100')
