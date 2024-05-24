lista_tarefas = []


def Menu():
    while True:
        print("1. Adicionar Tarefa\n2.Visualizar Tarefas\n3.Editar Tarefa\n4.Apagar Tarefa\n5.Sair")
        opcao_user = input("Escolha uma opção: ")

        if opcao_user == "1":
            AdicionarTarefa()
        elif opcao_user == "2":
            VisualizarTarefas()
        elif opcao_user == "3":
            EditarTarefas()
        elif opcao_user == "4":
            ApagarTarefas()
        elif opcao_user == "5":
            print("Saindo...")
            quit()
        else:
            print("\nOpcao invalida\n")


def AdicionarTarefa():
    nome_tarefa = input("\nDigite o nome da tarefa: ")
    conteudo_tarefa = input("Digite o conteudo desta tarefa: ")
    data_tarefa = input("Digite a data: (ex: **/**/****)      :")

    if nome_tarefa in lista_tarefas:
        print("\nEste nome ja está sendo utilizado, tente novamente")
        AdicionarTarefa()
    else:
        lista_tarefas.append([nome_tarefa, conteudo_tarefa, data_tarefa])

    print("\nTarefa criada com sucesso!!!")
    print("Voltando ao menu...\n")
    Menu()


def VisualizarTarefas():
    if not lista_tarefas:
        print("\nNão há tarefas na lista!!!")
    else:
        for tarefa in lista_tarefas:
            print(
                f"\nNome: {tarefa[0]}, Conteúdo: {tarefa[1]}, Data: {tarefa[2]}")
    print("\n")


def EditarTarefas():
    if not lista_tarefas:
        print("\nNão há tarefas na lista!!!")
        print("Voltando ao menu...\n")
        return

    VisualizarTarefas()
    escolha = input("\nDigite o nome da tarefa que deseja editar: ")

    for tarefa in lista_tarefas:
        if tarefa[0] == escolha:
            print("\nTarefa encontrada!")
            novo_nome = input(
                "Digite o novo nome da tarefa (ou pressione Enter para manter o atual): ")
            novo_conteudo = input(
                "Digite o novo conteúdo da tarefa (ou pressione Enter para manter o atual): ")
            nova_data = input(
                "Digite a nova data (ou pressione Enter para manter a atual): ")

            if novo_nome:
                tarefa[0] = novo_nome
            if novo_conteudo:
                tarefa[1] = novo_conteudo
            if nova_data:
                tarefa[2] = nova_data

            print("\nTarefa editada com sucesso!!!")
            print("Voltando ao menu...\n")
            return

    print("\nTarefa não encontrada.")
    print("Voltando ao menu...\n")


def ApagarTarefas():
    if not lista_tarefas:
        print("\nNão há tarefas na lista!!!")
        print("Voltando ao menu...\n")
        return

    VisualizarTarefas()
    escolha = input("\nDigite o nome da tarefa que deseja apagar: ")

    for tarefa in lista_tarefas:
        if tarefa[0] == escolha:
            print("\nTarefa encontrada!")
            lista_tarefas.remove(tarefa)
            print("\nTarefa removida com sucesso!!")
            print("Voltando ao menu...\n")
            return

    print("\nTarefa não encontrada.")
    print("Voltando ao menu...\n")


Menu()
