from random import randint

print('Validador e gerador de cpf')
print('Opção 1 - Digitar 11 números do cpf para verificar a validade')
print('Opção 2 - Gerar um CPF aleatoriamente')

while True:
    option = input('Por favor, digite a sua opção: ')
    if not option.isnumeric():
        print('Por favor, digite um número válido')
    elif option != '1' and option != '2':
        print('Opção inválida, digite novamente')
    else:
        break

if option == '1':
    while True:
        cpffinal = input('Digite um cpf: ')
        if not cpffinal.isnumeric():
            print('Não é um número, digite novamente')

        if len(cpffinal) < 11:
            print('Por favor, digite um cpf com ao menos 11 números')
        else:
            cpfaux = cpffinal[:-2]
            break

if option == '2':
    cpfaux = str(randint(100000000, 999999999))

while True:

    valormultiplica = []
    vetorconta = []
    size = len(cpfaux)
    for r in range(size):
        valormultiplica.append(r + 2)

    teste = valormultiplica[::-1]

    cpfauxint = []
    for i in cpfaux:
        cpfauxint.append(int(i))

    for x, y in zip(cpfauxint, teste):
        vetorconta.append(x * y)

    valor = 0
    for x in vetorconta:
        valor += x

    aux = 11 - (valor % 11)

    if aux <= 9:
        cpfaux = cpfaux + str(aux)
    else:
        cpfaux = cpfaux + str(0)

    if len(cpfaux) == 11:
        if option == '1':
            if cpffinal == cpfaux:
                print('O cpf informado é válido ')
                break
            else:
                print('O cpf informado é não é válido')
                break
        if option == '2':
            print(f'O Cpf gerado foi {cpfaux}')
            break
