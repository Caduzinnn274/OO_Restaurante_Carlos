class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Ativo'.ljust(20)}") 
        for restaurante in cls.restaurantes:
            nome_justificado = restaurante.nome.ljust(20)
            categoria_justificada = restaurante.categoria.ljust(20)
            ativo_justificado = restaurante.ativo.ljust(20)
            print(f"{nome_justificado} | {categoria_justificada} | {ativo_justificado}")

    @property
    def ativo(self):
        return "☒" if self._ativo else "☐"
    

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("pizza express", "Italiana")

Restaurante.listar_restaurantes()