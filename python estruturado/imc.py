peso   = eval(input('Qual seu peso?'))
altura = eval(input('Qual a sua altura?'))

IMC = peso / (altura*altura) #pode usar também altura**

print ('seu peso é:', IMC)

if IMC > 25:
    print("Você está com sobrepeso!")
else: 
    print('Você não está com sobrepeso!')

OU esse com definição da função:

def main():
    while True:
        try:
            peso   = float(input('Qual seu peso?'))
            altura = float(input('Qual a sua altura?'))

            IMC = peso / (altura*altura) #pode usar também altura**

            print ('seu peso é:', IMC)

            if IMC > 25:
                print("Você está com sobrepeso!")
            else: 
                print('Você não está com sobrepeso!')
            break
        except ValueError:
            print("Erro: Você deve inserir apenas números para o peso e a altura.")

main()