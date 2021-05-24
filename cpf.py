"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

while True:
    cpffinal = input('Digite um cpf: ')
    if not cpffinal.isnumeric():
        print('Não é um número, digite novamente')
    else:
        break

cpfaux = cpffinal[:-2]

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

    if len(cpfaux) == len(cpffinal):
        if cpffinal == cpfaux:
            print('O cpf informado é válido ')
            break
        else:
            print('O cpf informado é não é válido')
            break
