import random

profissoes = ['POLICIAL', 'PROFESSOR', 'PROGRAMADOR', 'COZINHEIRO', 'FAXINEIRO', 'SEGURANCA', 'CANTOR', 'PEDREIRO', 'PINTOR', 'GARCOM']
paises = ['BRASIL', 'RUSSIA', 'EUA', 'CUBA', 'ESPANHA', 'MEXICO', 'JAPAO', 'ALEMANHA', 'ARGENTINA', 'URUGUAI']
frutas = ['MORANGO', 'GOIABA', 'MACA', 'UVA', 'LARANJA', 'BANANA', 'MANGA', 'CAJARANA', 'TANGERINA', 'MELANCIA']

jogador = str(input('Informe seu nome: '))
print('Bem-vindo ao jogo da forca, {}!'.format(jogador))

while True:
    categoria = str(input('Escolha entre jogar com paises, profissoes ou frutas: ')).upper()
    if categoria == 'PAISES':
        palavra = random.choice(paises)
    elif categoria == 'PROFISSOES':
        palavra = random.choice(profissoes)
    elif categoria == 'FRUTAS':
        palavra = random.choice(frutas)
    else:
        print('Você digitou algo incorreto, tente novamente.')
        continue  # Volta para o início do loop para tentar de novo

    descobertas = ['_'] * len(palavra)
    erros = 0
    letras_usadas = []

    while erros < 6 and '_' in descobertas:
        print('\n' + ' '.join(descobertas))
        print('Letras já usadas:', ' '.join(letras_usadas))
        print('Tentativas restantes: {}'.format(6 - erros))

        letra = input('Digite uma letra: ').upper()
        if not letra.isalpha() or len(letra) != 1:
            print('Digite apenas UMA letra válida.')
            continue
        if letra in letras_usadas:
            print('Você já tentou essa letra.')
            continue

        letras_usadas.append(letra)
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    descobertas[i] = letra
        else:
            erros += 1

    print('\n' + ' '.join(descobertas))
    if '_' not in descobertas:
        print('Parabéns, {}! Você ganhou!'.format(jogador))
    else:
        print('{} você perdeu, a palavra correta era "{}".'.format(jogador, palavra))
        print('Você usou as letras: {}'.format(', '.join(letras_usadas)))

    jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
    if jogar_novamente != 'sim':
        print('Obrigado por jogar! Até a próxima.')
        break
