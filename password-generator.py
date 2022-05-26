from random import choice


def generate_password(length, all_chars):
    password = ""
    for _ in range(length):
        password += choice(all_chars)
    return password


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
chars = ""
number_of_passwords = int(input("Сколько паролей вы хотите? "))
length_of_password = int(input("Какова должна быть длина пароля?(количество знаков) "))
answer1 = input(f"Включить в пароль цифры(да, нет)? {digits} ")
if answer1 == "да":
    chars += digits
answer2 = input(f"Включить в пароль буквы нижнего регистра(да, нет)? {lowercase_letters} ")
if answer2 == "да":
    chars += lowercase_letters
answer3 = input(f"Включить в пароль буквы верхнего регистра(да, нет)? {uppercase_letters} ")
if answer3 == "да":
    chars += uppercase_letters
answer4 = input(f"Включить в пароль символы(да, нет)? {punctuation} ")
if answer4 == "да":
    chars += punctuation

for i in range(number_of_passwords):
    print(generate_password(length_of_password, chars))
