import random

password = int(input('Digite a sua senha de 4 dígitos númericos: '))
    
guess = 0
while (guess != password):
    guess = random.randint(0,9999)
    print(guess)
print('A sua senha é: ' + str(password))