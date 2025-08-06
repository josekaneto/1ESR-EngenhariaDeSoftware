tarefas = [];

while True:
    print("----Organizador de Tarefas----")
    print('1 - Adicionar Tarefa')
    print('2 - Remover Tarefa')
    print('3 - Listar Tarefas')
    print('4 - Sair')

    escolha = input("Digite sua opção: ")

    match escolha:
        case "1":
            tarefa_titulo = input("Digite o título da sua tarefa: ")
            print("----Menu de prioridade----")
            print("1 - Alta")
            print("2 - Média")
            print("3 - Baixa")
            print("4 - Sem prioridade")

            prioridade_escolha = input("Digite sua opção: ")

            match prioridade_escolha:
                case "1":
                    tarefa_prioridade = "Alta"
                case '2':
                    tarefa_prioridade = "Média"
                case '3':
                    tarefa_prioridade = "Baixa"
                case _:
                    tarefa_prioridade = ""

            print("----Menu de conclusão----")
            print("1 - Foi concluida")
            print("2 - Não Foi concluida")

            conclusao_escolha = input("Digite sua opção: ")

            match conclusao_escolha:
                case "1":
                    tarefa_conclusao = "Concluida"
                case "2":
                    tarefa_conclusao = "Pendente"
                case _:
                    tarefa_conclusao = "Pendente"

            tarefa = {"Titulo": tarefa_titulo, "Prioridade": tarefa_prioridade, "Status": tarefa_conclusao}
            tarefas.append(tarefa)

        case "2":
            tarefa_deletar = input("Digite o nome da tarefa que deseja deletar: ")

            for tarefa in tarefas:
                if tarefa["Titulo"] == tarefa_deletar:
                    tarefas.remove(tarefa)
                    print("Tarefa deletada com sucesso")

        case "3":
            print("----Todas as tarefas----")
            print(tarefas)

        case "4":
            break