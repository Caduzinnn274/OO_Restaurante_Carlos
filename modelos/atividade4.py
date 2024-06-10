#Atividade 1
class Pessoa:
    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome.title()
        self.idade = idade.upper()
        self.profissao = profissao.upper()

        Pessoa.pessoas.append(self)

    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.profissao}"

    @classmethod
    def listar_pessoas(cls):
        print(f"{'Nome da Pessoa'.ljust(20)} | {'Idade'.ljust(20)} | {'Profissão'.ljust(20)}") 
        for pessoa in cls.pessoas:
            nome_justificado = pessoa.nome.ljust(20)
            idade_justificada = pessoa.idade.ljust(20)
            profissao_justificado = pessoa.profissao.ljust(20)
            print(f"{nome_justificado} | {idade_justificada} | {profissao_justificado}")

    def Aniversario(self):
        self.idade += 1
    @property
    def Saudacao(self):
        return(f"Saudações {self.profissao} {self.nome}")
    
        




pessoa_1 = Pessoa('Carlos','17', 'Mecânico')
pessoa_2 = Pessoa('Cristiano','16', 'Engenheiro')



Pessoa.listar_pessoas()


