import time
from math import sqrt, log

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b, inteira=False):
    if b == 0:
        print('O denominador não pode ser 0!')
        return
    if not inteira:
        return a / b
    return a // b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    return sqrt(a)

def logaritmo(a, b=2.71828):
    return log(a, b)
    

name = input('Digite seu nome: ')
name = name.title()
print()

hist_op = {}
i = 1

while True:
    print()
    print(f'{name}, escolha uma das opções abaixo para realizar uma operação:\n')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potenciação')
    print('6 - Radiciação')
    print('7 - Logaritmo')
    print('8 - Histórico de operações')
    print('9 - Apagar histórico de operações')
    print('0 - Sair do programa\n')
    escolha = input('Digite sua escolha: ')
    print()
    
    if escolha == '0':
        break
    
    elif escolha == '8':
        if not hist_op:
            print('O histórico está vazio.')
        for key, value in hist_op.items():
            print(f'{key}: {value}')
        continue
    
    elif escolha == '9':
        hist_op.clear()
        i = 1
        continue
    
    num1 = float(input('Escolha o primeiro número da operação: '))
    if escolha != '6':
        num2 = float(input('Escolha o segundo número da operação: '))
    
    print()

    
    if escolha == '1':
        print(f'{name}, o resultado da operação é {num1} + {num2} = {add(num1, num2)}')
        hist_op.update({i : f'Adição - {num1} + {num2} = {add(num1, num2)}'})
        i += 1
        
    elif escolha == '2':
        print(f'{name}, o resultado da operação é {num1} - {num2} = {subtract(num1, num2)}')
        hist_op.update({i : f'Subtração - {num1} - {num2} = {subtract(num1, num2)}'})
        i += 1
        
    elif escolha == '3':
        print(f'{name}, o resultado da operação é {num1} * {num2} = {multiply(num1, num2)}')
        hist_op.update({i : f'Multiplicação - {num1} * {num2} = {multiply(num1, num2)}'})
        i += 1
        
    elif escolha == '4' and num2 != 0:
        escolha2 = input('A divisão é inteira? (S/N): ')
        if escolha2.lower() == 'n':
            print(f'{name}, o resultado da operação é {num1} / {num2} = {divide(num1, num2)}')
            hist_op.update({i : f'Divisão não inteira - {num1} / {num2} = {divide(num1, num2)}'})
        else:
            print(f'{name}, o resultado da operação é {num1} / {num2} = {divide(num1, num2, True)}, com resto {num1 % num2}')
            hist_op.update({i : f'Divisão inteira - {num1} / {num2} = {divide(num1, num2)}, com resto {num1 % num2}'})
        i += 1
    
    elif escolha == '5':
        print(f'{name}, o resultado da operação é {num1} elevado a {num2} = {potencia(num1, num2)}')
        hist_op.update({i : f'Potenciação - {num1} ^ {num2} = {potencia(num1, num2)}'})
        i += 1
        
    elif escolha == '6':
        print(f'{name}, o resultado da operação é raiz quadrada de {num1}  = {raiz_quadrada(num1)}')
        hist_op.update({i : f'Raiz quadrada - raiz de {num1} = {raiz_quadrada(num1)}'})
        i += 1
        
    elif escolha == '7':
        print(f'{name}, o resultado da operação é log de {num1} na base {num2} = {logaritmo(num1, num2)}')
        hist_op.update({i : f'Logaritmo - log de {num1} na base {num2} = {logaritmo(num1, num2)}'})
        i += 1
        
    else:
        print('Digite uma opção válida!')
    
    time.sleep(1.5)
        
print(f'Até a próxima, {name}!')
time.sleep(1)
