import cnpj
from random import randint

print("--Verificador de CNPJ--")
print("Informe todos os 13 números do CNPJ para verificar sua validade")
print("Sua validade não quer dizer que o mesmo existe, mas sim, que é matematicamente válido")

print("Opção 1 : Digitar um CNPJ para ser verificado")
print("Opção 2 : Gerar um CNPJ aleatoriamente ")
print("Opção 3 : Sair do programa ")

while True:
    option = input("Digite a opção escolhida: ")

    if option == '1':
        aux = input('Digite um CNPJ: ')
        cnpj.valida(aux, option)
    elif option == '2':
        cpfaux = str((randint(10000000000000, 99999999999999)))
        print(f"O CNPJ gerado automaticamente foi {cpfaux}")
        cnpj.valida(cpfaux, option)
    elif option == '3':
        break
    else:
        print("Opção inválida")
