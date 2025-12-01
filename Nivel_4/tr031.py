class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Exemplo de uso:
pessoa1 = Pessoa("Maria", 30)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")

pessoa2 = Pessoa("João", 25)
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")
