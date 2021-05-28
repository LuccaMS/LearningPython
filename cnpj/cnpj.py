import re


def valida(cnpj, chosen):
    cnpj = clean(cnpj)
    if len(cnpj) < 12 or len(cnpj) > 14:
        print("O tamanho do cnpj não é compativel ")

    else:
        count = 0
        aux = list(cnpj[:-2])
        count = 0
        while True:
            vectoraux = []
            for indice, i in enumerate(aux):
                if count == 0:
                    if indice <= 3:
                        if indice == 0:
                            vectoraux.append(5)
                        if indice == 1:
                            vectoraux.append(4)
                        if indice == 2:
                            vectoraux.append(3)
                        if indice == 3:
                            vectoraux.append(2)
                    if indice >= 4:
                        if indice == 4:
                            vectoraux.append(9)
                        if indice == 5:
                            vectoraux.append(8)
                        if indice == 6:
                            vectoraux.append(7)
                        if indice == 7:
                            vectoraux.append(6)
                        if indice == 8:
                            vectoraux.append(5)
                        if indice == 9:
                            vectoraux.append(4)
                        if indice == 10:
                            vectoraux.append(3)
                        if indice == 11:
                            vectoraux.append(2)

                if count == 1:
                    if indice <= 4:
                        if indice == 0:
                            vectoraux.append(6)
                        if indice == 1:
                            vectoraux.append(5)
                        if indice == 2:
                            vectoraux.append(4)
                        if indice == 3:
                            vectoraux.append(3)
                        if indice == 4:
                            vectoraux.append(2)
                    if indice >= 5:
                        if indice == 5:
                            vectoraux.append(9)
                        if indice == 6:
                            vectoraux.append(8)
                        if indice == 7:
                            vectoraux.append(7)
                        if indice == 8:
                            vectoraux.append(6)
                        if indice == 9:
                            vectoraux.append(5)
                        if indice == 10:
                            vectoraux.append(4)
                        if indice == 11:
                            vectoraux.append(3)
                        if indice == 12:
                            vectoraux.append(2)

            valor = 0
            for x, y in zip(aux, vectoraux):
                valor += (int(x) * y)

            auxvalue = 11 - (valor % 11)
            if auxvalue <= 9:
                aux += str(auxvalue)
            else:
                aux += str(0)

            if len(aux) == 14:
                if chosen == '1':
                    aux = ''.join(aux)
                    if cnpj == aux:
                        print("O CNPJ informado é válido")
                        break
                    else:
                        print(f"O CNPJ informado é inválido, sua versão válida é {aux}")
                        break
                if chosen == '2':
                    print(f"O CNPJ válidado a partir do gerado automaticamente é {''.join(aux)}")
                    break

            count += 1


def clean(a):
    return re.sub(r'[^0-9]', '', a)
