from time import sleep
def calculadora_en():
    print('                       ==============')
    print('\033[1;35mCALCULATOR\033[m'.center(70))
    print('                       ==============')
    print('\033[1;97mOPTIONS: | +, -, *, /, % |\033[m'.center(68))
    print(''.center(65))
    print(
        '\033[1;97mType \033[1;94m\'C\'\033[m \033[1;97mto ENTER or\033[1m \033[1;31m\'L\'\033[m \033[1;97mto LEAVE\033[m'.center(
            105))
    print()
    while True:
        choice = input('                      > ').upper().strip()
        while True:
            if not choice.isalpha() or choice != 'L' and choice != 'C':
                print()
                print('\033[1;31mERROR\033[m. \033[;1;97mTYPE C or L\033[1m'.center(75))
                print()
            break
        if choice.upper().strip().startswith('L'):
            print()
            print('\033[4;97mFinishing...\033[m'.center(65))
            print()
            for f in range(3, 0, -1):
                f = '            *'
                print(f, end='\033[1;97m*\033[m')
                sleep(0.8)
            print()
            print()
            print('Software finished.'.center(55))
            sleep(2)
            exit()
        if choice.upper().strip().startswith('C'):
            while True:
                print()
                print('                 ====================')
                print('\033[1mType the expression\033[m.'.center(62))
                print('                 ====================')
                print()
                exp = input('                      > ').replace(',', '.')
                print()
                print(f'\033[1;97mRESULT: {eval(exp)}\033[m'.center(62))
                print()
                while True:
                    novo = input('          Wanna calculate again? (Y/N): ').strip().upper()
                    print()
                    if novo == 'N':
                        print()
                        print('\033[1;97mFinishing...\033[m'.center(65))
                        print()
                        for f in range(3, 0, -1):
                            f = '*'.center(55)
                            print(f)
                            sleep(0.8)
                        print()
                        print('Software finished.'.center(55))
                        sleep(2)
                        exit()
                    else:
                        break
def calculadora_pt():
    print('                       ==============')
    print('\033[1;35mOPERAÇÕES\033[m'.center(72))
    print('                       ==============')
    print('\033[1;97mOPÇÕES: | +, -, *, /, % |\033[m'.center(68))
    print(''.center(65))
    print('\033[1;97mDigite \033[1;94m\'C\'\033[m \033[1;97mpara CONTINUAR ou\033[1m \033[1;31m\'S\'\033[m \033[1;97mpara SAIR\033[m'.center(105))
    print()
    while True:
        choice = input('                      > ').upper().strip()
        while True:
            if not choice.isalpha() or choice != 'S' and choice != 'C':
                print()
                print('\033[1;31mERRO\033[m. \033[;1;97mDigite C ou S\033[1m'.center(75))
                print()
            break
        if choice.upper().strip().startswith ('S'): #Aqui, se ele der o input 'S' na escolha entre continuar o programa ou sair, o programa finaliza com uma contagem e um exit()
            sleep (0.2)
            print()
            print('\033[4;97mFinalizando...\033[m'.center(65))
            print()
            for f in range (3, 0, -1):
                f = '            *'
                print(f, end='\033[1;97m*\033[m')
                sleep (0.8)
            print()
            print()
            print('Programa finalizado.'.center(55))
            sleep(2)
            exit()
        if choice.upper().strip().startswith ('C'):
            while True:
                print()
                print('                 ====================')
                print('\033[1mDigite a expressão\033[m.'.center(62))
                print('                 ====================')
                print()
                exp = input('                      > ').replace(',', '.')
                print()
                print(f'\033[1;97mRESULTADO: {eval(exp)}\033[m'.center(62))
                print()
                while True:
                    novo = input('          Deseja calcular de novo? (S/N): ').strip().upper()
                    print()
                    if novo == 'N':             #Aqui, se o user der o input N, o programa finaliza com um 'exit()' após uma contagem de aviso.
                        print()
                        print('\033[1;97mFinalizando...\033[m'.center(65))
                        print()
                        for f in range (3, 0, -1):
                            f = '*'.center(55)
                            print(f)
                            sleep(0.8)
                        print()
                        print('Programa finalizado.'.center(55))
                        sleep(2)
                        exit()
                    else:                     #Aqui, se u usuário der qualquer outro input diferente de 'N', o 'break' sai do loop e volta para ao input 'exp'.
                        break
print()
print('Select a language'.center(60))
print()
print('\033[1;32mPortuguês [1]\033[m | \033[1;34mEnglish [2]\033[m'.center(80))
print()
while True:
    language = input('                > ')
    if not language in ['1', '2']:
        print('            ————————————————————————')
        print('\033[1;91mERROR\033[m. Input a valid option.'.center(60))
        print('            ————————————————————————')
    else:
        break
if language == '1':
    calculadora_pt()
elif language == '2':
    calculadora_en()