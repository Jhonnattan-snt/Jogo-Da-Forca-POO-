import random

profissoes = ['POLICIAL', 'PROFESSOR', 'PROGRAMADOR', 'COZINHEIRO', 'FAXINEIRO', 'SEGURANCA', 'CANTOR', 'PEDREIRO', 'PINTOR', 'GARCOM']
paises = ['BRASIL', 'RUSSIA', 'EUA', 'CUBA', 'ESPANHA', 'MEXICO', 'JAPAO', 'ALEMANHA', 'ARGENTINA', 'URUGUAI']
frutas = ['MORANGO', 'GOIABA', 'MACA', 'UVA', 'LARANJA', 'BANANA', 'MANGA', 'CAJARANA', 'TANGERINA', 'MELANCIA']
animais = ['GATO', 'CACHORRO', 'PAPAGAIO', 'ONITORINCO', 'PEIXE', 'BALEIA', 'COELHO','RATO', 'PATO', 'GANSO']
cores = ['VERMELHO', 'LARANJA', 'VERDE', 'AZUL', 'ROSA', 'PRETO', 'BRANCO', 'AMARELO', 'DOURADO', 'CINZA']

print('Bem vindo ao jogo da forca!')
jogador = str(input('Nome: '))
 
#Loop do jogo
while True:

    #Escolha da categoria
    categoria = str(input('Escolha entre jogar com paises, profissoes, frutas, cores ou animais: ')).upper()
    if categoria == 'PAISES':
        palavra = random.choice(paises)
        print('Você escolheu Paises... inicializando...')
    elif categoria == 'PROFISSOES':
        palavra = random.choice(profissoes)
        print('Você escolheu Profissões... inicializando...')
    elif categoria == 'FRUTAS':
        palavra = random.choice(frutas)
        print('Você escolheu Frutas... inicializando...')
    elif categoria == 'ANIMAIS':
        palavra = random.choice(animais)
        print('Você escolheu ANIMAIS... inicializando...')
    elif categoria == 'CORES':
        palavra = random.choice(cores)
        print('Você escolheu CORES... inicializando...')
    else:
        print('Você digitou algo incorreto, tente novamente')
        continue

    # Inicio do jogo
    descobertas = ['_'] * len(palavra)
    erros = 0
    letras_usadas = []

     # Loop de tentativa de letras
    while erros < 6 and '_' in descobertas:
        #Forca
        if erros == 0:
            print ('''
                   +---+
                   |   |
                       |
                       |
                       |
                       |
                =========''')
        elif erros == 1:
            print ('''
                   +---+
                   |   |
                   0   |
                       |
                       |
                       |
                =========''')
        elif erros == 2:
            print ('''
                   +---+
                   |   |
                   0   |
                   |   |
                       |
                       |
                =========''')
        elif erros == 3:
            print ('''
                   +---+
                   |   |
                   0   |
                  -|-  |
                       |
                       |
                =========''')
        elif erros == 4:
            print ('''
                   +---+
                   |   |
                   0   |
                  -|-  |
                   |   |
                       |
                =========''')
        elif erros == 5:
            print ('''
                   +---+
                   |   |
                   0   |
                  -|-  |
                   |   |
                  /    |
                =========''')
        elif erros == 6:
            print ('''
                   +---+
                   |   |
                   0   |
                  -|-  |
                   |   |
                  / \  |
                =========''')


        print(' '.join(descobertas))
        print('Letras já usadas:', ' '.join(letras_usadas))
        print('Tentativas restantes: {}'.format(6 - erros))

        letra = input('Digite uma letra: ').upper()
        if not letra.isalpha() or len(letra) != 1:
            print('Digite apenas UMA/1 letra válida.')
            continue
        elif letra in letras_usadas:
            print('Você já usou essa letra.')
            continue
        
        letras_usadas.append(letra)
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    descobertas[i] = letra
        else:
            erros += 1
    
    # Finalização da rodada
    print(' '.join(descobertas))
    if '_' not in descobertas:
        print('Parabéns {}!, você ganhou!'.format(jogador))
    else:
        print ('''
               +---+
               |   |
               0   |
              -|-  |
               |   |
              / \  |
              =========''')
        print('{} Você perdeu, a palavra correta era {}'.format(jogador,palavra))
        print('Você usou as letras {}'.format(letras_usadas))
    print('Rodada completa')
    print(60 * ('-'))

    # Pergunta se o jogador deseja jogar novamente
    jogar_novamente = input('deseja jogar novamente? (sim/não): ').lower()
    if jogar_novamente != 'sim':
        print('Obrigado por jogar! Até a próxima.')
        break

