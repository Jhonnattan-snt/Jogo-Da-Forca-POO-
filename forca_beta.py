import random

palavras = ['POLICIAL', 'MORANGO', 'PROGRAMADOR', 'GOIABA', 'CANTOR']
palavra = random.choice(palavras)
descobertas = ['_'] * len(palavra)
erros = 0

while erros < 6 and '_' in descobertas:
    print(' '.join(descobertas))
    letra = input('Palavra: ').upper()
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                descobertas[i] = letra
    else:
        erros += 1

print(' '.join(descobertas))
if '_' not in descobertas:
    print('Parabéns você ganhou')
else:
    print(f'Você perdeu, a palavra correta era {palavra}')
