opcao = 1
contatos = []

while opcao:
    opcao = int(input(
        """
            Digite uma opção:
                1 - Listar Contatos:
                2 - Adicionar um contato:
                3 - Editar um contato:
                4 - Apagar um contato:
                0 - Sair
        """
    ))

    match opcao:
        case 1:
            for c in contatos:
                print("Nome: ", c['Nome'])
                print("Telefone: ", c["Telefone"])
        case 2:
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            contatos.append({"Nome": nome, "Telefone": telefone})
        case 3:
            nome = input("Digite o nome: ")
            
            for c in contatos:
                if c["Nome"] == nome:
                    telefone = input("Digite o telefone: ")
                    c["Telefone"] = telefone
        case 4:
            nome = input("Digite o nome:")
            for c in contatos:
                if c["Nome"] == nome:
                    contatos.remove(c)