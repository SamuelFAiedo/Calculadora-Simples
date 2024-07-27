import os

def titulo():
    print("CALCULADORA\n")

def exibir_opcao():
    subtitulo("Escolha qual operação deseja fazer:")
    print("1. Soma:")
    print("2. Subtração:")
    print("3. Multiplicação:")
    print("4. Divisão:")
    print("5. Sair")

def escolher_opcao():
    opcao_escolhida = int(input("Digite a opção escolhida:"))
    try:
        if opcao_escolhida == 1:
            soma()
        elif opcao_escolhida == 2:
            subtracao()
        elif opcao_escolhida == 3:
            multiplicacao()
        elif opcao_escolhida == 4:
            divisao()
        elif opcao_escolhida == 5:
            encerrar_app()
        else: opcao_invalida()
    except:
        opcao_invalida()

def soma():
    os.system("cls")
    subtitulo("Adicione os números que deseja somar:")
    num1 = float(input("Digite o primeiro número que deseja somar: "))
    num2 = float(input("Digite o segudo número que deseja somar: "))
    resultado_soma = num1 + num2
    print(f"O resultado da soma é: {resultado_soma}\n")
    voltar()

def subtracao():
    os.system("cls")
    subtitulo("Adicione os números que deseja subtrair:")
    num1 = float(input("Digite o primeiro número que deseja subtrair: "))
    num2 = float(input("Digite o segundo número que deseja subtrair: "))
    resultado_sub = num1 - num2
    print(f"O resultado da subtração é: {resultado_sub}\n")
    voltar()

def multiplicacao():
    os.system("cls")
    subtitulo("Adicione os números que deseja multiplicar:")
    num1 = float(input("Digite o primeiro número que deseja multiplicar: "))
    num2 = float(input("Digite o segudo número que deseja multiplicar: "))
    resultado_multi = num1 * num2
    print(f"O resultado da multiplicação é: {resultado_multi}\n")
    voltar()

def divisao():
    os.system("cls")
    subtitulo("Adicione os números que deseja dividir:")
    num1 = float(input("Digite o primeiro número que deseja dividir: "))
    num2 = float(input("Digite o segudo número que deseja dividir: "))
    resultado_div = num1 / num2
    print(f"O resultado da soma é: {resultado_div}\n")
    voltar()

def encerrar_app():
    os.system("cls")
    print("Obrigado por utilizar nossa aplicação! Encerrando App")

def subtitulo(texto):
    os.system("cls")
    linha = "-" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print(" ")

def voltar():
    input("\nPara voltar ao menu inicial digite uma tecla e aperte enter:")
    main()

def opcao_invalida():
    print("Opção incorreta! Tente novamente:")
    voltar()

def main():
    os.system("cls")
    titulo()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()