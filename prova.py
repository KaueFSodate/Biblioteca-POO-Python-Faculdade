class Livro:
    livros = {}
    locacoes = {}

    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo

    def incluir_livro(self):
        livro = Livro(self.id, self.titulo)
        self.livros[self.id] = livro
        print(f"O livro '{self.titulo}' foi cadastrado com sucesso!")

    def editar_livro(self):
        novo_titulo = input(f"Digite o novo título para o livro '{self.titulo}': ")
        self.titulo = novo_titulo
        print("Livro alterado com sucesso!")

    def excluir_livro(self):
        del Livro.livros[self.id]
        print(f"O livro '{self.titulo}' foi excluído com sucesso!")

    @staticmethod
    def consultar_livro():
        if len(Livro.livros) == 0:
            print("Não há livros cadastrados.")
        else:
            print("Livros cadastrados:")
            for id, livro in Livro.livros.items():
                print(f"{id}: {livro.titulo}")

    def locar_livro(self):
        if self.id in Livro.locacoes:
            print("Livro já está locado.")
        else:
            Livro.locacoes[self.id] = True
            print(f"O livro '{self.titulo}' foi locado com sucesso!")

    def devolver_livro(self):
        if self.id not in Livro.locacoes:
            print("Livro não está locado.")
        else:
            del Livro.locacoes[self.id]
            print(f"O livro '{self.titulo}' foi devolvido com sucesso!")

    def consultar_por_livro(self):
        print(f"ID: {self.id} - Título: {self.titulo}")


class Cliente:
    clientes = {}

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def cadastrar_cliente(self):
        cliente = Cliente(self.id, self.nome)
        self.clientes[self.id] = cliente
        print(f"O cliente '{self.nome}' foi cadastrado com sucesso!")

    def alterar_cliente(self):
        novo_nome = input(f"Digite o novo nome para o cliente '{self.nome}': ")
        self.nome = novo_nome
        print("Cliente alterado com sucesso!")

    def excluir_cliente(self):
        del Cliente.clientes[self.id]
        print(f"O cliente '{self.nome}' foi excluído com sucesso!")

    @staticmethod
    def consultar_cliente():
        if len(Cliente.clientes) == 0:
            print("Não há clientes cadastrados.")
        else:
            print("Clientes cadastrados:")
            for id, cliente in Cliente.clientes.items():
                print(f"{id}: {cliente.nome}")

    def consultar_por_cliente(self):
        print(f"ID: {self.id} - Nome: {self.nome}")


def livros_menu():
    while True:
        print("\n==== MENU DE LIVROS ====")
        print("1. Listar livros")
        print("2. Cadastrar livro")
        print("3. Alterar livro")
        print("4. Excluir livro")
        print("5. Alocar livro")
        print("6. Devolver livro")
        print("7. Consultar por livro")
        print("8. Voltar")

        opcao = int(input("Digite uma opção: "))

        if opcao not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("Opção inválida!")
        elif opcao == 8:
            print("Voltando ao menu principal...")
            break
        elif opcao == 2:
            id = input("Digite o ID do livro: ")
            titulo = input("Digite o título do livro: ")
            livro = Livro(id, titulo)
            livro.incluir_livro()
        elif opcao == 1:
            Livro.consultar_livro()
        else:
            id = input("Digite o ID do livro: ")
            if id not in Livro.livros:
                    print("Livro não encontrado.")
            else:
                livro = Livro.livros[id]
                if opcao == 3:
                    livro.editar_livro()
                elif opcao == 4:
                    livro.excluir_livro()
                elif opcao == 5:
                    livro.locar_livro()
                elif opcao == 6:
                    livro.devolver_livro()
                elif opcao == 7:
                    livro.consultar_por_livro()


def clientes_menu():
    while True:
        print("\n==== MENU DE CLIENTES ====")
        print("1. Listar clientes")
        print("2. Cadastrar cliente")
        print("3. Alterar cliente")
        print("4. Excluir cliente")
        print("5. Consultar por cliente")
        print("6. Voltar")

        opcao = int(input("Digite uma opção: "))

        if opcao not in [1, 2, 3, 4, 5, 6]:
            print("Opção inválida!")
        elif opcao == 6:
            print("Voltando ao menu principal...")
            break
        elif opcao == 2:
            id = input("Digite o ID do cliente: ")
            nome = input("Digite o nome do cliente: ")
            cliente = Cliente(id, nome)
            cliente.cadastrar_cliente()
        elif opcao == 1:
            Cliente.consultar_cliente()
        else:
            id = input("Digite o ID do cliente: ")
            if id not in Cliente.clientes:
                print("Cliente não encontrado.")
            else:
                cliente = Cliente.clientes[id]
                if opcao == 3:
                    cliente.alterar_cliente()
                elif opcao == 4:
                    cliente.excluir_cliente()
                elif opcao == 5:
                    cliente.consultar_por_cliente()


def menu():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Livros")
        print("2. Clientes")
        print("3. Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao not in [1, 2, 3]:
            print("Opção inválida!")
        elif opcao == 3:
            print("Obrigado!")
            break
        elif opcao == 1:
            livros_menu()
        elif opcao == 2:
            clientes_menu()


menu()
