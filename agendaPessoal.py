agenda = {}
campos = ["nome", "telefone", "email", "datanasc"]

while True:
    ope = int(input("""
                   Agenda Pessoal
                1 - Salvar Contato
                2 - Alterar Contato
                3 - Buscar Contato
                4 - Apagar Contato
                5 - Lista Contatos

        Pressione 0 para sair.

    """))

    if ope == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        datanasc = input("Data de Nascimento: ")
        contato = [nome, telefone, email, datanasc]
        agenda[nome] = contato
        print(f"O contato de {nome} foi salvo com sucesso.")

    elif ope == 2:
        nome = input("Qual contato você quer alterar: ")
        if nome in agenda:
            print(agenda[nome])
            campo = input("Qual dado deseja alterar: ")
            if campo in campos:
                novo = input("Qual o novo valor: ")
                agenda[nome][campos.index(campo)] = novo
                print(f"O dado {campo} foi alterado.")
            else:
                print("Campo inválido!")
        else:
            print("Contato não encontrado!")

    elif ope == 3:
        nome = input("Qual contato deseja buscar: ")
        if nome in agenda:
            contato = agenda[nome]
            print(contato)
        else:
            print("Contato não encontrado!")

    elif ope == 4:
        nome = input("Qual contato deseja apagar: ")
        if nome in agenda:
            del agenda[nome]
            print(f"O contato de {nome} foi apagado com sucesso!")
        else:
            print("Contato não encontrado!")

    elif ope == 5:
        for contato in agenda.values():
            print(contato)

    elif ope == 0:
        break

    else:
        print("Opção Inválida!")
