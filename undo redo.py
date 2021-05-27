if __name__ == '__main__':
    print("Opção 1 : Adicionar Tarefa")
    print("Opção 2 : Listar Tarefas")
    print("Opção 3 : Desfazer ")
    print("Opção 4 : Refazer ")
    print("Opção 5 : Sair do programa ")

    lista_tarefas = []
    lista_auxiliar = []

    while True:
        op = input("Digite uma opção: ")
        if not op.isnumeric():
            print("A opção digitada não é numerica, digite novamente ")
        else:
            if op == '1':
                aux = input("Digite uma tarefa: ")
                lista_tarefas.append(aux)
            elif op == '2':
                for i, x in enumerate(lista_tarefas):
                    print(f'Tarefa de número {i + 1} , conteúdo : {x}')
            elif op == '3':
                lista_auxiliar.append(lista_tarefas[-1])
                lista_tarefas.pop()
            elif op == '4':
                try:
                    last = lista_auxiliar.pop()
                    lista_tarefas.append(last)
                except IndexError:
                    print("Nenhum elemento foi excluido até o momento ou todos já foram recuperados")
            elif op == '5':
                break
            else:
                print("Opção inexistente")
