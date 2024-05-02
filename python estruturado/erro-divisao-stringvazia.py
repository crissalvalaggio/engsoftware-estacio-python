def exercicio2():
    resultado = 1

    while True:
        try:
            numero = input('Insira um número: ')
            if not numero:
                print('Por favor, insira um número!')
                continue
            numero = int(numero)

            divisor = input('Insira um número para dividir: ')
            if not divisor:
                print('Por favor, insira um divisor:')
                continue
            divisor = int(divisor)

            resultado = numero / divisor

            print(f'A divisão é: {resultado}')
            break
        except ZeroDivisionError:
            print('Erro: Divisão por zero! Digite outro número!')
        except ValueError:
            print('Por favor, insira um número válido!')

exercicio2()
