import mysql.connector
import os
def Clean():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para conectar ao banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",         
        password="Alekson2004!",       
        database="biblioteca"       
    )




# Classe para representar o usuário
class Usuario:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}"


# Função para cadastrar cliente
def cadastrar_cliente(cursor, conexao):
    print("=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    cpf = input("CPF (apenas números): ")
    email = input("E-mail: ")

    novo_usuario = Usuario(nome, cpf, email)

    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, cpf, email) VALUES (%s, %s, %s)",
            (novo_usuario.nome, novo_usuario.cpf, novo_usuario.email)
        )
        conexao.commit()
        print(f" Cliente cadastrado com sucesso! ID gerado: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f" Erro ao cadastrar cliente: {err}")




# Classe para representar os livro
class livros:
    def __init__(self, titulo, autor, ano, status):
        self.titulo = titulo
        self.autor =  autor
        self.ano  = ano
        self.status = status

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, status: {self.status}"


# Função para cadastrar livro
def cadastrar_livro(cursor, conexao):
    print("=== Cadastro de Livro ===")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    status = 'Disponivel'

        
    novo_livros = livros(titulo, autor, ano, status)

    try:
        cursor.execute(
            "INSERT INTO livros (titulo, autor, ano, status) VALUES (%s, %s, %s, %s)",
            (novo_livros.titulo, novo_livros.autor, novo_livros.ano, novo_livros.status)
        )
        conexao.commit()
        print(f" Livro cadastrado com sucesso! ID gerado: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f" Erro ao cadastrar livros: {err}")




# Classe para representar a lista de livros
def listar_livros(cursor):
    print("=== Lista de Livros ===")

    try:
        cursor.execute("""
            SELECT l.id, l.titulo, l.status, u.nome
            FROM livros l
            LEFT JOIN emprestimos e ON l.id = e.livro_id AND l.status = 'Indisponivel'
            LEFT JOIN usuarios u ON e.usuario_id = u.id;
        """)

        livros = cursor.fetchall()

        if not livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in livros:
            id_livro, titulo, status, nome_usuario = livro
            print(f" Título: {titulo}")
            print(f"    Status: {status}")
            if status == 'Indisponivel' and nome_usuario:
                print(f"    Emprestado para: {nome_usuario}")
            print("—" * 30)

    except mysql.connector.Error as err:
        print(f" Erro ao listar livros: {err}")




# Classe para representar quando pegou emprestado e previsão de entrega
class emprestimos:
    def __init__(self, livro_id, usuario_id, data_emprestimo, previsão_de_devolucao):
        self.livro_id = livro_id
        self.usuario_id = usuario_id
        self.data_emprestimo = data_emprestimo
        self.previsão_de_devolucao = previsão_de_devolucao

    def __str__(self):
        return f"livro_id: {self.livro_id}, usuario_id: {self.usuario_id}, data_emprestimo: {self.data_emprestimo}, previsão_de_devolucao: {self.previsão_de_devolucao}"


def registrar_emprestimo(cursor, conexao):
    print("=== Registrar Empréstimo ===")
    try:
        livro_id = int(input("ID do livro: "))
        usuario_id = int(input("ID do usuário: "))

        # Verificar se o livro está disponível
        cursor.execute("SELECT status FROM livros WHERE id = %s", (livro_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            print(" Livro não encontrado.")
            return
        elif resultado[0] != "Disponivel":
            print(" Livro indisponível para empréstimo.")
            return

        # Datas
        data_emprestimo = input("Em qual dia emprestou o livro? Exemplo(2025-12-25) :")
        previsão_de_devolucao = input("Previsão para a entrega do livro Exemplo(2025-12-25) :")

        # Inserir na tabela de empréstimos
        cursor.execute(
            "INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, previsão_de_devolucao) VALUES (%s, %s, %s, %s)",
            (livro_id, usuario_id, data_emprestimo, previsão_de_devolucao)
        )

        # Atualizar status do livro para "Indisponivel"
        cursor.execute(
            "UPDATE livros SET status = 'Indisponivel' WHERE id = %s",
            (livro_id,)
        )

        conexao.commit()
        print("✅ Empréstimo registrado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao registrar empréstimo: {e}")




def devolver_livro(cursor, conexao):
    print("=== Devolução de Livro ===")
    try:
        livro_id = int(input("ID do livro a ser devolvido: "))

        # Verificar se há empréstimo ativo para esse livro
        cursor.execute("""
            SELECT e.id, u.nome, l.titulo
            FROM emprestimos e
            JOIN usuarios u ON e.usuario_id = u.id
            JOIN livros l ON e.livro_id = l.id
            WHERE e.livro_id = %s AND e.data_devolucao IS NULL;
        """, (livro_id,))
        emprestimo = cursor.fetchone()

        if not emprestimo:
            print(" Nenhum empréstimo ativo encontrado para este livro.")
            return

        emprestimo_id, nome_usuario, titulo = emprestimo
        print(f"📖 Livro: {titulo}")
        print(f"👤 Emprestado para: {nome_usuario}")

        confirmacao = input("Deseja registrar a devolução? (s/n): ").strip().lower()
        if confirmacao != 's':
            print(" Devolução cancelada.")
            return

        # Atualiza a data de devolução no empréstimo
        data_hoje = input("Data da devolução: Exemplo: 2025-12-25 ")
        cursor.execute("""
            UPDATE emprestimos
            SET data_devolucao = %s
            WHERE id = %s;
        """, (data_hoje, emprestimo_id))

        # Atualiza o status do livro
        cursor.execute("""
            UPDATE livros
            SET status = 'Disponivel'
            WHERE id = %s;
        """, (livro_id,))

        conexao.commit()
        print(" Devolução registrada com sucesso!")

    except ValueError:
        print(" Entrada inválida. O ID deve ser um número inteiro.")
    except mysql.connector.Error as err:
        print(f" Erro ao registrar devolução: {err}")



# Menu principal
while True:
    print("\n1 - Cadastrar Cliente\n2 - Cadastrar livro\n3 - Livros cadastrados\n4 - Pegar emprestado\n5 - Data de entrega\n6 - Sair")
    escolha = input("-----------------------\n:")

    if escolha == '1':
        Clean()
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cadastrar_cliente(cursor, conexao)
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(f" Erro de conexão: {erro}")
            

    elif escolha == '2':
        Clean()
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cadastrar_livro(cursor, conexao)
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(f" Erro de conexão: {erro}")


    elif escolha == '3':
        Clean()
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            listar_livros(cursor)
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(f" Erro de conexão: {erro}")


    elif escolha == '4':
        Clean()
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            registrar_emprestimo(cursor, conexao)
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(f" Erro de conexão: {erro}")


    elif escolha == '5':
        Clean()
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            devolver_livro(cursor, conexao)
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(f" Erro de conexão: {erro}")




    else:
        break