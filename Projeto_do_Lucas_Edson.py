#Objetivo: O usuário do projeto poderá cadastrar e remover livros, além de definir preços para o aluguel dos livros. 
# Serão cadastrados o nome, CPF e endereço do cliente que alugou o livro, assim como a data em
# que foi alugado e a data prevista para devolução.
import os
def Clean():
    os.system('cls' if os.name == 'nt' else 'clear')

cliente = {}
NomeDoLivro = ["O senhor dos aneis", "Game of Thrones", "Pai rico, pai pobre", "O pequeno príncipe", "Os segredos da mente milionária", "Watchmen", "Romeu e Julieta", "A revolução dos bixos",
 "Guerra e paz", "1934", "O capital", "Como ser um conservados", "Dom Casmurro", "Harry Potter", "Moby Dick", "Os miseráveis", "Crônicas de Nárnia"]
ValorDoLivro = [125, 102, 95, 41, 25, 150, 24, 31, 15, 38, 27, 52, 15, 82, 33, 97, 125]
QuantidadeDeLivro = [15, 9, 5, 12, 6, 7, 4, 7, 3, 4, 2, 4, 3, 12, 5, 3, 10]
while True:
    try:
        opcao = int(input("_______________________\n1 - Cadastrar Cliente\n2 - Cadastrar/Atualizar livro\n3 - Pesquisar livro\n4 - Pegar emprestado/comprar livro \n5 - Para excluir um livro\n6 - Sair\n-----------------------\n:"))
        if opcao == 1: 
            Clean()
                                                                #CADASTRANDO O CLIENTE NO SISTEMA

            nome = input("Digite o nome do cliente: ")
            CPF = int(input("Digite o CPF do novo cliente: "))
                                                                #VERIFICANDO SE O CPF JÁ FOI CADASTRADO

            if CPF in cliente:
                print("CPF já cadastrado")
            else:
                email = (input("Digite o endereço de email do novo cliente: "))
                cidade = input("Digite a cidade do cliente: ")
                bairro = input("Digite o bairro do cliente: ")
                rua_e_número = input("Digite a rua e o número da casa do cliente: ")
                cliente[CPF] = {
                    "Nome": nome,
                    "Cidade": cidade,
                    "Bairro": bairro,
                    "Rua": rua_e_número,
                    "E-mail": email
                }
     

        elif opcao == 2:
            Clean()
                                                                            #CADASTRANDO O LIVRO
            achei = True
            Livro = input("Digite o nome do livro que deseja cadastrar ou atualizar: ") 
            for i in range(len(NomeDoLivro)):
                if Livro == NomeDoLivro[i]:
                    achei = False
                    escolha = int(input("Esse livro já está cadastrado no sistema! O que desejas fazer? \n1 - (repor o estoque)\n2 - (atualizar o valor)\n "))
                    while escolha == 1 or escolha == 2:
                                                                            #REPONDO O ESTOQUE
                        if escolha == 1:
                            Quantidade = int(input(f"Quanto de copias de '{Livro}' desejas repor no estoque? "))
                            QuantidadeDeLivro[i] += Quantidade
                            print("Quantidade de copias atualizada com sucesso")
                            break
                                                                            #AUTERANDO O VALOR
                        elif escolha == 2:
                            Valor = float(input("Quanto é o novo valor do livro? R$"))
                            ValorDoLivro[i] = Valor
                            break
                                                                            #CADASTRANDO UM LIVRO NOVO
            if achei == True:
                Valor = float(input(f"Quanto vai custar '{Livro}'? R$"))
                Quantidade = int(input(f"Quantas copias '{Livro}' a biblioteca tem? "))
                NomeDoLivro.append(Livro)
                QuantidadeDeLivro.append(Quantidade)
                ValorDoLivro.append(Valor)
                print("Livro cadastrado")
     
        elif opcao == 3:
            Clean()
                                                                            #PROCURANDO LIVRO
            i = 0
            print("                                                                              LIVROS CADASTRADOS")
            for i in range(len(NomeDoLivro)):
                print(f"{NomeDoLivro[i]} | copias: {QuantidadeDeLivro[i]}")
            escolha = int(input("\nDeseja procurar por um livro?\n(1 - Sim | 2 - Não)\n: "))
            while escolha != 1 and escolha != 2:
                escolha = int(input("Deseja procurar por um livro?\n(1 - Sim | 2 - Não)\n: "))
            if escolha == 1:
                procurarLivro = input("\nDigite o nome do livro que desejas procurar: ")    
                for i in range(len(NomeDoLivro)):
                    if procurarLivro == NomeDoLivro[i]:
                        Clean()
                        print(f"O livro '{NomeDoLivro[i]}' foi encontrado e a biblioteca ainda tem {QuantidadeDeLivro[i]} copias")    
                        break
                else:
                    print("O livro não foi encontrado ou não está cadastrado no sistema")
            elif escolha == 2:
                Clean()

                
        elif opcao == 4:
            Clean()
            achei = True
            comprar_alugar = int(input("Você deseja Pegar emprestado ou comprar?\n (1 - Pegar emprestado | 2 - Comprar)\n"))
            while comprar_alugar != 1 and comprar_alugar != 2:
                Clean()
                comprar_alugar = int(input("Você deseja Pegar emprestado ou comprar?\n (1 - Pegar emprestado | 2 - Comprar)\n"))

                                                                    #PROCURANDO LIVRO
            procurarLivro = input("Digite o nome do livro que desejas procurar: " )
            for i in range(len(NomeDoLivro)):                                                     
                if procurarLivro == NomeDoLivro[i] and comprar_alugar == 1 and QuantidadeDeLivro[i] > 0:
                    Clean()
                    comprar_alugar = int(input(f"O livro {NomeDoLivro[i]} tem {QuantidadeDeLivro[i]} copias. O cliente tem 12 dias para devolver o livro. Após esse período, será aplicada uma multa diária de R${ValorDoLivro[i] / 20:.2f}. \n Deseja pegar este livro emprestado?\n (1 - Sim | 2 - Não)\n: ")) 
                        #Enquanto o usuário não informar se quer comprar ou alugar, o sistema continuara perguntando se ele quer comprar ou não
                    while comprar_alugar != 1 and comprar_alugar != 2:
                        comprar_alugar = int(input("Você deseja pegar este livro emprestado?\n (1 - Sim | 2 - Não) \n"))  
                    #Cancelar
                    achei = False
                    if comprar_alugar == 1:
                        procurar_cliente = int(input("Digite o CPF do cliente sem pontos e traço ou aperte 3 para cancelar: "))
                        if procurar_cliente == 3:
                            break
                                                                    #PROCURANDO O CLIENTE
                        elif procurar_cliente in cliente:                                   
                            dados = cliente[procurar_cliente]
                            print(f"Cliente encontrado com sucesso\n--------------------\nCPF: {CPF}\nNome: {dados["Nome"]}\nCidade: {dados["Cidade"]}\nBairro: {dados["Bairro"]}\nRua: {dados["Rua"]} \nE-mail: {dados["E-mail"]}\n--------------------")
                            comprar_alugar = int(input("Você confirma esses dados?\n (1 - Sim | 2 - Não)\n:"))
                            while comprar_alugar != 1 and comprar_alugar != 2:
                                Clean()
                                comprar_alugar = int(input("Você confirma esses dados?\n (1 - Sim | 2 - Não)\n:"))
                            if comprar_alugar == 1:
                                QuantidadeDeLivro[i] = QuantidadeDeLivro[i] - 1
                                Clean()
                                print("O livro foi separado, vá até o caixa efetuar o pagamento e pegar o livro")
                            else:
                                break
                        
                elif procurarLivro == NomeDoLivro[i] and comprar_alugar == 2 and QuantidadeDeLivro[i] > 0:
                    Clean()
                    comprar_alugar = int(input(f"O livro {NomeDoLivro[i]} tem {QuantidadeDeLivro[i]} custa R${ValorDoLivro[i]}\n Deseja comprar este livro?\n (1 - Sim | 2 - Não)\n:")) 
                    while comprar_alugar != 1 and comprar_alugar != 2:
                        comprar_alugar = int(input("Você deseja comprar este livro?\n (1 - Sim | 2 - Não)\n:"))  
                    achei = False
                    if comprar_alugar == 1:
                        procurar_cliente = int(input("Digite o CPF do cliente sem pontos e traço ou aperte 3 para cancelar: "))
                        if procurar_cliente == 3:
                            break    
                        #Comprando o livro   
                        
                        elif comprar_alugar == 1:
                            while comprar_alugar != 1 and comprar_alugar != 2:
                                procurar_cliente = int(input("Digite o seu CPF sem pontos e traço: "))
                            if procurar_cliente in cliente:
                                dados = cliente[procurar_cliente]
                                                                            #PROCURANDO O CLIENTE

                                print(f"Cliente encontrado com sucesso\n--------------------\nCPF: {CPF}\nNome: {dados["Nome"]}\nCidade: {dados["Cidade"]}\nBairro: {dados["Bairro"]}\nRua: {dados["Rua"]} \nE-mail: {dados["E-mail"]}\n--------------------")
                                comprar_alugar = int(input("Você confirma esses dados?\n (1 - Sim | 2 - Não)\n:"))
                                while comprar_alugar != 1 and comprar_alugar != 2:
                                    Clean()
                                    comprar_alugar = int(input("Você confirma esses dados?\n (1 - Sim | 2 - Não)\n:"))
                                if comprar_alugar == 1:
                                    QuantidadeDeLivro[i] = QuantidadeDeLivro[i] - 1
                                    Clean()
                                    print("O livro foi separado, vá até o caixa efetuar o pagamento e pegar o livro")
                                else:
                                    break
                
                elif QuantidadeDeLivro[i] <= 0:
                    Clean()
                    print(f"Todas as copias de {NomeDoLivro[i]} foram alugadas ou vendidas")
                    achei = False
                    break
            if achei == True:
                print("Livro não encontrado") 

        elif opcao == 5:
            Clean()
            ExcluirLivro = input("Qual livro desejas excluir? ")
            for i in range(len(NomeDoLivro)):
                if ExcluirLivro == NomeDoLivro[i]:
                    EscolhApagar = int(input(f"Tem certeza que deseja excluir o livro '{ExcluirLivro}' do sistema?\n (1 - SIM | 2 - NÃO)\n"))
                    if EscolhApagar == 1:
                        NomeDoLivro.pop(i)
                        QuantidadeDeLivro.pop(i)
                        ValorDoLivro.pop(i)
                        Clean()
                        print(f"O livro {ExcluirLivro} foi removido do sistema")
                        break
                    else:
                        print("Livro não encontrado ou não cadastrado")
                        break
        else:
            break
            
    except ValueError:
        Clean()
        print("ERRO: Você inseriu um ou mais valores inválidos.")     
