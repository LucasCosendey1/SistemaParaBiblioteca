import tkinter as tk
from tkinter import messagebox

def cadastrar_cliente():
    def salvar_cliente():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        email = email_entry.get()
        endereco = endereco_entry.get()

        if not cpf.isdigit():
            messagebox.showerror("Erro", "CPF deve conter apenas números.")
            return

        if int(cpf) in cliente:
            messagebox.showerror("Erro", "CPF já cadastrado.")
        else:
            cliente[int(cpf)] = {
                "Nome": nome,
                "Endereço": endereco,
                "E-mail": email
            }
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso.")
            cadastro_cliente.destroy()

    cadastro_cliente = tk.Toplevel()
    cadastro_cliente.title("Cadastrar Cliente")

    tk.Label(cadastro_cliente, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    nome_entry = tk.Entry(cadastro_cliente)
    nome_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(cadastro_cliente, text="CPF:").grid(row=1, column=0, padx=10, pady=5)
    cpf_entry = tk.Entry(cadastro_cliente)
    cpf_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(cadastro_cliente, text="E-mail:").grid(row=2, column=0, padx=10, pady=5)
    email_entry = tk.Entry(cadastro_cliente)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(cadastro_cliente, text="Endereço:").grid(row=3, column=0, padx=10, pady=5)
    endereco_entry = tk.Entry(cadastro_cliente)
    endereco_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(cadastro_cliente, text="Salvar", command=salvar_cliente).grid(row=4, column=0, columnspan=2, pady=10)

def cadastrar_livro():
    def salvar_livro():
        livro = livro_entry.get()
        valor = valor_entry.get()
        codigo = codigo_entry.get()
        quantidade = quantidade_entry.get()

        if not valor.replace('.', '', 1).isdigit() or not quantidade.isdigit():
            messagebox.showerror("Erro", "Valor e Quantidade devem ser numéricos.")
            return

        NomeDoLivro.append(livro)
        CodigoDoLivro.append(int(codigo))

        QuantidadeDeLivro.append(int(quantidade))
        CodigoDoLivro.append(int(codigo))
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso.")
        cadastro_livro.destroy()

    cadastro_livro = tk.Toplevel()
    cadastro_livro.title("Cadastrar Livro")

    tk.Label(cadastro_livro, text="Nome do Livro:").grid(row=0, column=0, padx=10, pady=5)
    livro_entry = tk.Entry(cadastro_livro)
    livro_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(cadastro_livro, text="Valor da Diária:").grid(row=1, column=0, padx=10, pady=5)
    valor_entry = tk.Entry(cadastro_livro)
    valor_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(cadastro_livro, text="Quantidade:").grid(row=2, column=0, padx=10, pady=5)
    quantidade_entry = tk.Entry(cadastro_livro)
    quantidade_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(cadastro_livro, text="Código:").grid(row=3, column=0, padx=10, pady=5)
    codigo_entry = tk.Entry(cadastro_livro)
    codigo_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(cadastro_livro, text="Salvar", command=salvar_livro).grid(row=4, column=0, columnspan=2, pady=10)

def listar_livros():
    lista_livros = tk.Toplevel()
    lista_livros.title("Lista de Livros")

    for i, livro in enumerate(NomeDoLivro):
        tk.Label(lista_livros, text=f"{CodigoDoLivro[i]} - {livro} ({QuantidadeDeLivro[i]} disponíveis)").pack(anchor="w", padx=10)

def comprar_livro():
    def verificar_codigo():
        codigo = codigo_entry.get()
        if not codigo.isdigit():
            messagebox.showerror("Erro", "O código deve ser numérico.")
            return

        codigo = int(codigo)
        if codigo in CodigoDoLivro:
            indice = CodigoDoLivro.index(codigo)
            nome_livro = NomeDoLivro[indice]
            quantidade_disponivel = QuantidadeDeLivro[indice]
            PreçoDoLivro = ValorDoLivro[indice]

            # Atualiza o rótulo na mesma janela
            livro_label.config(text=f"Livro: {nome_livro}\nQuantidade: {quantidade_disponivel}\n R${PreçoDoLivro}")

            if quantidade_disponivel > 0:
                cpf_label.grid(row=3, column=0, padx=10, pady=5)
                cpf_entry.grid(row=3, column=1, padx=10, pady=5)
                confirmar_cpf_btn.grid(row=4, column=0, columnspan=2, pady=10)
            else:
                messagebox.showerror("Erro", "Este livro está fora de estoque.")
        else:
            messagebox.showerror("Erro", "Código não encontrado.")

    def verificar_cpf():
        cpf = cpf_entry.get()
        if not cpf.isdigit():
            messagebox.showerror("Erro", "O CPF deve conter apenas números.")
            return

        cpf = int(cpf)
        if cpf in cliente:
            dados_usuario = cliente[cpf]
            nome = dados_usuario["Nome"]
            endereco = dados_usuario["Endereço"]
            email = dados_usuario["E-mail"]

            resposta = messagebox.askyesno(
                "Confirmação de Dados",
                f"Nome: {nome}\nEndereço: {endereco}\nE-mail: {email}\n\nOs dados estão corretos?"
            )

            if resposta:
                indice = CodigoDoLivro.index(int(codigo_entry.get()))
                QuantidadeDeLivro[indice] -= 1
                messagebox.showinfo(
                    "Sucesso",
                    f"O livro '{NomeDoLivro[indice]}' foi separado!\nVá ao balcão para efetuar o pagamento."
                )
                compra_livro.destroy()
        else:
            messagebox.showerror("Erro", "CPF não encontrado. Cadastre-se antes de comprar um livro.")

    compra_livro = tk.Toplevel()
    compra_livro.title("Comprar Livro")

    tk.Label(compra_livro, text="Digite o código do livro:").grid(row=0, column=0, padx=10, pady=5)
    codigo_entry = tk.Entry(compra_livro)
    codigo_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(compra_livro, text="Buscar", command=verificar_codigo).grid(row=1, column=0, columnspan=2, pady=10)

    # Rótulos para exibir o nome do livro e quantidade diretamente na janela
    livro_label = tk.Label(compra_livro, text="", font=("Arial", 10, "bold"))
    livro_label.grid(row=2, column=0, columnspan=2, pady=5)

    quantidade_label = tk.Label(compra_livro, text="", font=("Arial", 10))
    quantidade_label.grid(row=3, column=0, columnspan=2, pady=5)

    cpf_label = tk.Label(compra_livro, text="Digite seu CPF:")
    cpf_entry = tk.Entry(compra_livro)
    confirmar_cpf_btn = tk.Button(compra_livro, text="Confirmar CPF", command=verificar_cpf)

# Dados iniciais
cliente = {}
NomeDoLivro = ["O senhor dos anéis", "Game of Thrones", "Pai rico, pai pobre", "O pequeno príncipe", "Os segredos da mente milionária", "Watchmen", "Romeu e Julieta", "A revolução dos bichos",
 "Guerra e paz", "1984", "O capital", "Como ser um conservador", "Dom Casmurro", "Harry Potter", "Moby Dick", "Os miseráveis", "Crônicas de Nárnia"]
ValorDoLivro = [125, 102, 95, 41, 25, 150, 24, 31, 15, 38, 27, 52, 15, 82, 33, 97, 125]
QuantidadeDeLivro = [15, 9, 5, 12, 6, 7, 4, 7, 3, 4, 2, 4, 3, 12, 5, 3, 10]
CodigoDoLivro = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]

# Interface principal
root = tk.Tk()
root.title("Sistema de Biblioteca")

tk.Button(root, text="Cadastrar Cliente", command=cadastrar_cliente).pack(pady=5)
tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro).pack(pady=5)
tk.Button(root, text="Listar Livros", command=listar_livros).pack(pady=5)
tk.Button(root, text="Comprar Livro", command=comprar_livro).pack(pady=5)
tk.Button(root, text="Sair", command=root.quit).pack(pady=5)

root.mainloop()
