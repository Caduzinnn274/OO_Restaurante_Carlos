class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
   
        self._ativo = ativo

    @property
    def ativo(self):
        return"✔️" if self._ativo else "✖️"
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Status: {self.ativo}, "

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza= Restaurante('Pizzaria_Express', 'Italiana')

Restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)

