import csv

agenda = {}
campos = ["nome", "telefone", "email", "datanasc"]

def salvar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    datanasc = input("Data de Nascimento: ")
    contato = [nome, telefone, email, datanasc]
    agenda[nome] = contato
    print(f"O contato de {nome} foi salvo com sucesso.")

def alterar_contato():
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

def buscar_contato():
    nome = input("Qual contato deseja buscar: ")
    if nome in agenda:
        contato = agenda[nome]
        print(contato)
    else:
        print("Contato não encontrado!")

def apagar_contato():
    nome = input("Qual contato deseja apagar: ")
    if nome in agenda:
        del agenda[nome]
        print(f"O contato de {nome} foi apagado com sucesso!")
    else:
        print("Contato não encontrado!")

def listar_contatos():
    for contato in agenda.values():
        print(contato)

def salvar_agenda_csv():
    with open('agenda.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(campos)
        for contato in agenda.values():
            writer.writerow(contato)

def carregar_agenda_csv():
    try:
        with open('agenda.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            campos = next(reader)
            for linha in reader:
                agenda[linha[0]] = linha[1:]
    except FileNotFoundError:
        print("Arquivo da agenda não encontrado. Uma nova agenda será criada.")

def menu():
    print("""
                   Agenda Pessoal
                1 - Salvar Contato
                2 - Alterar Contato
                3 - Buscar Contato
                4 - Apagar Contato
                5 - Lista Contatos
                6 - Salvar Agenda em CSV
                7 - Carregar Agenda de CSV

        Pressione 0 para sair.
    """)

carregar_agenda_csv()

while True:
    menu()
    ope = int(input("Escolha uma opção: "))

    if ope == 1:
        salvar_contato()
    elif ope == 2:
        alterar_contato()
    elif ope == 3:
        buscar_contato()
    elif ope == 4:
        apagar_contato()
    elif ope == 5:
        listar_contatos()
    elif ope == 6:
        salvar_agenda_csv()
        print("Agenda salva em 'agenda.csv'.")
    elif ope == 7:
        carregar_agenda_csv()
        print("Agenda carregada de 'agenda.csv'.")
    elif ope == 0:
        salvar_agenda_csv()
        print("Agenda salva em 'agenda.csv'.")
        print("Programa encerrado.")
        break
    else:
        print("Opção Inválida!")
