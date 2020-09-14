from datetime import datetime as dt

"""
Queremos armazenar os seguintes dados:
* Nome
* Idade
* Altura
* Peso
* Tipo sanguíneo (se conhecido)
* Queixa no PS (se houver)
* Datas de consulta

Operações:
* Alterar idade
* Alterar peso
* Alterar queixa
* Adicionar uma data de consulta
"""

class Paciente:
    ##lista de atributos da classe (construtor)
    def __init__(self, nome, idade, altura, peso, queixa=None, tipoSanguineo=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.queixa = queixa
        self.tipoSansuineo = tipoSanguineo
        self.consultas = []
    

    def adiciona_consulta(self, dataConsulta):
        self.consultas.append(dataConsulta)

    def altera_idade(self, nova_idade):
        self.idade = nova_idade

    def altera_peso(self, novo_peso):
        self.peso = novo_peso
    
    def altera_queixa(self, nova_queixa):
        self.queixa = nova_queixa
