import random

char = '0123456789abcdefghijklmnopqrstuvwxz'
char_list = list(char)
password = input('Digite a sua senha: ')
guess = ""

while (guess != password):
    guess = random.choices(char_list, k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)

print('Sua senha é: ' + guess)