import sys
import time

## Menu
def menu():

    print('\nOPERAÇÕES')
    print('*'*80)

    print('\n1 - Equação de segundo grau\n2 - Velocidade média\n3 - Consumo de veiculo\n4 - SAIR\n')

    while True:
        try:
            opcao = int(input('Digite o numero da operação desejada: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            if opcao == 1:
                equacao()
            elif opcao == 2:
                vel_media()
            elif opcao == 3:
                consumo_comb()
            elif opcao == 4:
                print('Saindo do programa...')
                time.sleep(2)
                sys.exit()
            else:
                print('\nDigite uma opção valida.\n')
                opcao = int(input('Digite o numero da operação desejada: '))
        except ValueError:
            print('\n')

## Voltar ou sair do programa
def voltar():

    back = int(input('\nDeseja realizar outra operação.\n1 - SIM\n2 - NÃO\n\nDigite uma opção: '))

    while True:
        try:
            #back = int(input('Digite uma opção: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            if back == 1:
                print('Carregando...')
                time.sleep(2)
                menu()
            elif back == 2:
                print('Saindo do programa...')
                time.sleep(2)
                sys.exit()
            else:
                print('\nEsta não é uma opção valida.\n')
                #back = int(input('Digite uma opção: '))
        except ValueError:
            print('\nDigite uma opção valida.\n')

## Equação de segundo grau
def equacao():

    while True:
        try:
            a = float(input('\nDigite o primeiro termo da equação: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            b = float(input('digite o segundo termo da equação: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            c = float(input('digite o terceiro termo da equação: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    delta = pow(int(b),2)-4*int(a)*int(c)
    raiz_delta = pow(delta,0.5)

    x1 = -(int(b))+raiz_delta
    try:
        x1 = x1/(2*int(a))
    except ZeroDivisionError as err:
        print('\nERRO: {}'.format(err))


    x2 = -(int(b))-raiz_delta
    try:
        x2 = x2/(2*int(a))
    except ZeroDivisionError as err:
        print('\nERRO: {}'.format(err))

    print('\nA equação tem como raizes os números {} e {}'.format(x1,x2))

    voltar()

## Velocidade média
def vel_media():

    while True:
        try:
            velocidade = float(input('\nDigite a velocidade média em Metros por Segundo (m/s): '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            distancia = float(input('\nDigite a distancia em Metros (m): '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            tempo = float(input('\nDigite o tempo em Segundos (s): '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    print()

    try:
        if velocidade == 0:
            formula = distancia / tempo
            print('A velocidade média é {}m/s\n'.format(formula))
            conversao = int(input('Deseja converter para Quilometros por Hora (K/h)? \n digite 1 para sim ou 2 para não: '))
            if conversao == 1:
                km = formula * 3.6
                print('\nA velocidade média é {}K/m'.format(km))
                voltar()
            else:
                voltar()
        elif distancia == 0:
            formula = velocidade * tempo
            print('A distancia percorrida foi de {} metros.\n'.format(formula))
            conversao = int(input('Deseja converter para Quilometros (Km)? \n digite 1 para sim ou 2 para não: '))
            if conversao == 1:
                km = formula / 1000
                print('\nA distancia percorrida foi de {}Km.'.format(km))
                voltar()
            else:
                voltar()
        elif tempo == 0:
            formula = distancia / velocidade
            print('O tempo foi de {} Segundos.\n'.format(formula))
            conversao = int(input('Deseja converter para Horas? \n digite 1 para sim ou 2 para não: '))
            if conversao == 1:
                km = formula / 3600
                print('\nO tempo foi de {} Horas.'.format(km))
                voltar()
            else:
                voltar()
        else:
            print('\nPelo menos um fator deve ser igual a zero\n')
            print('1 - Inserir dados novamente\n2 - Voltar ao menu principal\n3 - SAIR')
            opcao = int(input('Digite uma opção: '))
            while True:
                try:
                    #opcao = int(input('Digite o numero da operação desejada: '))
                    break
                except ValueError:
                    print('\nNão foi digitado um numero\n')

            while True:
                try:
                    if opcao == 1:
                        vel_media()
                    elif opcao == 2:
                        menu()
                    elif opcao == 3:
                        time.sleep(2)
                        sys.exit()
                    else:
                        print('\nDigite uma opção valida.\n')
                        #opcao = int(input('Digite o numero da operação desejada: '))
                except ValueError:
                    print('\n')
    except ZeroDivisionError as err:
        print('\nERRO: {}\n'.format(err))
        print('1 - Inserir dados novamente\n2 - Voltar ao menu principal\n3 - SAIR')
        opcao = int(input('Digite uma opção: '))
        while True:
            try:
                # opcao = int(input('Digite o numero da operação desejada: '))
                break
            except ValueError:
                print('\nNão foi digitado um numero\n')

        while True:
            try:
                if opcao == 1:
                    vel_media()
                elif opcao == 2:
                    menu()
                elif opcao == 3:
                    time.sleep(2)
                    sys.exit()
                else:
                    print('\nDigite uma opção valida.\n')
                    # opcao = int(input('Digite o numero da operação desejada: '))
            except ValueError:
                print('\n')

## consumo de combustivel
def consumo_comb():

    while True:
        try:
            distancia = float(input('\nDigite a distancia em quilometros (Km) que sera percorrida: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            preco_comb = float(input('\nDigite o valor do litro do combustivel utilizado: '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    while True:
        try:
            consumo = float(input('\nDigite o consumo do carro em quilometros por litros (Km/L): '))
            break
        except ValueError:
            print('\nNão foi digitado um numero\n')

    try:
        if distancia != 0 and preco_comb != 0 and consumo != 0:
            formula = (distancia / consumo) * preco_comb
            print('\nO valor gasto sera de R${}\n'.format(formula))
            decisao = int(input('Deseja realizar um novo calculo? \n digite 1 para sim ou 2 para não: '))
            if decisao == 1:
                consumo_comb()
            else:
                menu()
        elif distancia == 0:
            while True:
                try:
                    total_gasto = float(input('\nInforme o valor total gasto com combustivel: '))
                    break
                except ValueError:
                    print('\nNão foi digitado um numero\n')
            formula = (total_gasto / preco_comb) * consumo
            print('\nA distancia percorrida foi de {}Km\n'.format(formula))
            decisao = int(input('Deseja realizar um novo calculo? \n digite 1 para sim ou 2 para não: '))
            if decisao == 1:
                consumo_comb()
            else:
                menu()
        elif preco_comb == 0:
            while True:
                try:
                    total_gasto = float(input('\nInforme o valor total gasto com combustivel: '))
                    break
                except ValueError:
                    print('\nNão foi digitado um numero\n')
            formula = (total_gasto / distancia) * consumo
            print('\nO valor do combustivel é R${} por litro.\n'.format(formula))
            decisao = int(input('Deseja realizar um novo calculo? \n digite 1 para sim ou 2 para não: '))
            if decisao == 1:
                consumo_comb()
            else:
                menu()
        elif consumo == 0:
            while True:
                try:
                    total_gasto = float(input('\nInforme o valor total gasto com combustivel: '))
                    break
                except ValueError:
                    print('\nNão foi digitado um numero\n')
            formula = (distancia / total_gasto) * preco_comb
            print('\nO consumo do carro é de {}Km/L.\n'.format(formula))
            decisao = int(input('Deseja realizar um novo calculo? \n digite 1 para sim ou 2 para não: '))
            if decisao == 1:
                consumo_comb()
            else:
                menu()
        else:
            print('\nPelo menos um fator deve ser igual a zero\n')
            print('1 - Inserir dados novamente\n2 - Voltar ao menu principal\n3 - SAIR')
            opcao = int(input('Digite uma opção: '))
            while True:
                try:
                    #opcao = int(input('Digite o numero da operação desejada: '))
                    break
                except ValueError:
                    print('\nNão foi digitado um numero\n')

            while True:
                try:
                    if opcao == 1:
                        consumo_comb()
                    elif opcao == 2:
                        menu()
                    elif opcao == 3:
                        time.sleep(2)
                        sys.exit()
                    else:
                        print('\nDigite uma opção valida.\n')
                        #opcao = int(input('Digite o numero da operação desejada: '))
                except ValueError:
                    print('\n')
    except ZeroDivisionError as err:
        print('\nERRO: {}\n'.format(err))
        print('1 - Inserir dados novamente\n2 - Voltar ao menu principal\n3 - SAIR')
        opcao = int(input('Digite uma opção: '))
        while True:
            try:
                # opcao = int(input('Digite o numero da operação desejada: '))
                break
            except ValueError:
                print('\nNão foi digitado um numero\n')

        while True:
            try:
                if opcao == 1:
                    consumo_comb()
                elif opcao == 2:
                    menu()
                elif opcao == 3:
                    time.sleep(2)
                    sys.exit()
                else:
                    print('\nDigite uma opção valida.\n')
                    # opcao = int(input('Digite o numero da operação desejada: '))
            except ValueError:
                print('\n')