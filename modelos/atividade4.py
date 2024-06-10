# #Atividade 1# #Atividade 1
# class Pessoa:
#     pessoas = []

#     def __init__(self, nome, idade, profissao):
#         self.nome = nome.title()
#         self.idade = idade.upper()
#         self.profissao = profissao.upper()

#         Pessoa.pessoas.append(self)

#     def __str__(self):
#         return f"{self.nome} | {self.idade} | {self.profissao}"

#     @classmethod
#     def listar_pessoas(cls):
#         print(f"{'Nome da Pessoa'.ljust(20)} | {'Idade'.ljust(20)} | {'Profissão'.ljust(20)}") 
#         for pessoa in cls.pessoas:
#             nome_justificado = pessoa.nome.ljust(20)
#             idade_justificada = pessoa.idade.ljust(20)
#             profissao_justificado = pessoa.profissao.ljust(20)
#             print(f"{nome_justificado} | {idade_justificada} | {profissao_justificado}")

#     def Aniversario(self):
#         self.idade += 1
#     @property
#     def Saudacao(self):
#         return(f"Saudações {self.profissao} {self.nome}")
    
        




# pessoa_1 = Pessoa('Carlos','17', 'Mecânico')
# pessoa_2 = Pessoa('Cristiano','16', 'Engenheiro')
# print(pessoa_1.Saudacao)
# print(pessoa_2.Saudacao)


# Pessoa.listar_pessoas()




#Atividade 2

class Conta:
  contas = []

  def __init__(self, titular,saldo):
        self.titular = titular.title()
        self.saldo = saldo.upper()
        Conta.contas.append(self)

  def __str__(self):
         return f"{self.titular} | {self.saldo}"


  @classmethod
  def listar_conta(cls):
        print(f"{'Nome do titular'.ljust(20)} | {'Saldo'.ljust(20)} ") 
        for conta in cls.contas:
                titular_justificado = conta.titular.ljust(20)
                saldo_justificada = conta.saldo.ljust(20)
        print(f"{titular_justificado} | {saldo_justificada} ")


conta_1 = Conta('Carlos','200,00' )
conta_2 = Conta('Cristiano','160,00' )


Conta.listar_conta()



   


