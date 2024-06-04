# Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.
import os
import time

#Calcular função da area do trapezio
def calcular_trapezio(base_menor, base_maior, h):
    a = ((base_menor+base_maior)*h)/2
    return a


#Calcular Círculo
def calcular_circulo(r):
   a = 3.14*r**2
   return a

#Calcular area do Triagulo
def calcular_triagulo(b, a):
    area= (a*b)/2
    return area

#Exibir o Menu
def Menu():
    print("1. Calcular a Area de um circulo")
    print("2. Calcular a Area de um Triâgulo")
    print("3. Calcular a Area de um trapezio")
    print("4. Sair do programa")
    
    
while True:
    Menu()
    opcao = input("\nESCOLHA UMA DAS OPÇÕES LISTADAS ACIMA: ")
    print("Carregando opção...")
    time.sleep(3)
    os.system('cls')
        
    match opcao:
        case '1':
            print('Área do círculo: a = π*r2')
            r = int(input('Informe o valor do raio: '))
            print(f'Area do círculo é: {calcular_circulo(r)}.')
            continue
        case '2':
            print('Área do triagulo: a = (b*a)/2')
            b = int(input('Informe o valor da base: '))
            a = int(input('Informe o valor da altura: '))
            print(f'Area do triagulo é: {calcular_triagulo(b,a)}.')
            continue
        case '3':
            print('Área do trapezio é: a= ((b+B)*h)/2')
            base_menor = int(input('Informe o valor da base menor'))
            base_maior = int(input('Informe o valor da base maior'))
            h = int(input('Informe o valor da altura do trapezio: '))
            print(f'Area do trapézio: {calcular_trapezio(base_menor,base_maior,h)}.')
            continue
        case '4':
            break
        case _:
            print('Opção inválida...')
            continue     
      

# Executar o menu
if __name__ == "__main__":
    Menu()

    

