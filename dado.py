import random


run = True

while run:
    jogar = str(input('Deseja rodar o dado [S/N]?')).strip().upper()
    if jogar == 'S':
        #Seleçaõ de dado
        print('=' * 30)
        print('>>> 1d6')
        print('>>> 1d12')
        print('>>> 1d16')
        print('>>> 1d20')
        print('=' * 30)
        escolha1 = str(input('Escolha um dos dados acima: ')).strip().lower()
        print('=' * 30)

        #Casos de dados
        if escolha1 == '1d6':
            dado = random.randint(1,6)
            print('=' * 30)
            print('RODANDO O DADO')
            print(f'Voce tirou o numero {dado}')
            print('=' * 30)

        elif escolha1 == '1d12':
            dado = random.randint(1,12)
            print('=' * 30)
            print('RODANDO O DADO')
            print(f'Voce tirou o numero {dado}')
            print('=' * 30)

        elif escolha1 == '1d16':
            dado = random.randint(1,16)
            print('=' * 30)
            print('RODANDO O DADO')
            print(f'Voce tirou o numero {dado}')
            print('=' * 30)

        elif escolha1 == '1d20':
            dado = random.randint(1,20)
            print('=' * 30)
            print('RODANDO O DADO')
            print(f'Voce tirou o numero {dado}')
            print('=' * 30)
        #Caso de erro na seleção de dados
        else:
            print('=' * 30)
            print('VALOR NÃO RECONHECIDO | TENTE NOVAMENTE')
            print('=' * 30)
    #Caso o usuario não queira mais usar o dado
    elif jogar == 'N':
        print('=' * 30)
        print('OBRIGADO POR USAR NOSSO DADO')
        print('=' * 30)
        break
    #Caso de erro na seleção de jogo
    else:
        print('=' * 30)
        print('ERRO INFORMAÇÃO NÃO RECONHECIDA')
        print('=' * 30)