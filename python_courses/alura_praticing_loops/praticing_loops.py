#Exercise 1 : 

clients = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

for client in clients:
    print(client)

#Exercise 2 :
i = 0
message = "Bem-vindo ao Buscante!"
while i < 5:
    print(message)
    i += 1

# Exercise 3 :
valores = [10, 20, 30, 40, 50]

soma = 0
for valor in valores:
    soma += valor

print(f"A soma total dos valores é: {soma}")

# Exercise 4 :

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos: 
    if projeto == None:
        print("Projeto ausente")
    else:
        print(f"Projeto: {projeto}")

# Exercise 5 :
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}" )
        break

# Exercise 6 :
estoque = 5
while estoque > 0:
    print(f"venda realizada, restam {estoque} produtos")
    estoque =-1

print("Estoque esgotado")

#Exercise 7:

for numero in range (10, 0, -1):
    if numero % 2 == 0:
        print(f"Faltam apenas {numero} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {numero} segundos restantes.")
print("Aproveite a promoção agora!")

#Exercise 8:

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] > 0:
        print (f"Livro disponível: {livro["nome"]}")
        

#Exercise 9:
while True:
    user = input("Digite seu nome: ")
    password = input("Digite sua senha: ")

    if len(user) < 5: 
        print("O nome de usuário deve ter no mínimo 5 caracteres.")
        continue
    if len(password) < 8:
        print("A senha deve ter no mínimo 8 caracteres.")
        continue

    print("Usuário cadastrado com sucesso!")
    break