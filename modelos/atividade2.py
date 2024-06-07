##2) Atividade 1

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}'

Carro = Carro("Chevette", "Azul", 1987)
print(Carro)



#Atividade 2

class Restaurante:
    def __init__(self, nome, categoria, endereco, ativo=False, nota=4.5, capacidade=243):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.ativo = ativo
        self.nota = nota
        self.capacidade = capacidade

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Nota: {self.nota}, Capacidade: {self.capacidade}"

restaurante1 = Restaurante('Laçador', 'Espeto Corrido', 'Av. Ayrton Senna Da Silva, 2404 - Jardim Busmayer, Campo Largo - PR, 83606-390', capacidade=243)
print(restaurante1)

class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

cliente1 = Cliente('Allan', 'allan,ribinski@escola.pr.gov.br', '2050-0987', 'Itaqui de cima')
cliente2 = Cliente('Joao', 'schilian07@gmail.com', '4070-0870', 'Em frente ao posto')
cliente3 = Cliente('Gustavo', 'gustavo.shaikoski@escola.pr.gov.br', '4325-0654', 'Rondinha')

print(cliente1)
print(cliente2)
print(cliente3)