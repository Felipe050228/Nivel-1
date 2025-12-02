class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        if idade >= 18 :
            self.ver_de_idade = "(você ja é maior de idade)"
        elif idade < 18 :
            self.ver_de_idade = "(você ainda é menor de idade)"

pessoa1 = Pessoa("Maria", 30)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade} {pessoa1.ver_de_idade}")

pessoa2 = Pessoa("João", 15)
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade} {pessoa2.ver_de_idade}")
 
pessoa3 = Pessoa("Felipe", 17)
print(f"Nome: {pessoa3.nome}, Idade: {pessoa3.idade} {pessoa3.ver_de_idade}")