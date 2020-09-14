from dados import Paciente as p
from datetime import datetime as dt

### Teste Criação Paciente e Adicionar consultas
data = dt.now().strftime('%Y-%m-%d %H:%M:%S')

novoPaciente = p('Fabiano', 30, 1.73, 80,'Atendimento em atraso no dia 05/09/2020')
p.adiciona_consulta(self=novoPaciente,dataConsulta=data)
p.adiciona_consulta(self=novoPaciente,dataConsulta=data)
p.adiciona_consulta(self=novoPaciente,dataConsulta=data)
print(
    f"Nome: {novoPaciente.nome}\n"
    f"Idade: {novoPaciente.idade}\n"
    f"Altura: {novoPaciente.altura}\n"
    f"Peso: {novoPaciente.peso}\n"
    f"Queixa: {novoPaciente.queixa}\n"
    f"Consultas: {novoPaciente.consultas}\n"    
    )

### Alterar Idade
p.altera_idade(self=novoPaciente,nova_idade=31)
print(
    f"Nome: {novoPaciente.nome}\n"
    f"Idade: {novoPaciente.idade}  ***Idade Alterada***\n"
    f"Altura: {novoPaciente.altura}\n"
    f"Peso: {novoPaciente.peso}\n"
    f"Queixa: {novoPaciente.queixa}\n"
    f"Consultas: {novoPaciente.consultas}\n"    
    )

### Alterar Peso
p.altera_peso(self=novoPaciente,novo_peso=85)
print(
    f"Nome: {novoPaciente.nome}\n"
    f"Idade: {novoPaciente.idade}\n"
    f"Altura: {novoPaciente.altura}\n"
    f"Peso: {novoPaciente.peso}  ***Peso Alterado***\n"
    f"Queixa: {novoPaciente.queixa}\n"
    f"Consultas: {novoPaciente.consultas}\n"    
    )

### Alterar Queixa
p.altera_queixa(self=novoPaciente,nova_queixa='Reclamação alterada: Atendimento em atraso no dia 10/09/2020')
print(
    f"Nome: {novoPaciente.nome}\n"
    f"Idade: {novoPaciente.idade}\n"
    f"Altura: {novoPaciente.altura}\n"
    f"Peso: {novoPaciente.peso}\n"
    f"Queixa: {novoPaciente.queixa}  ***Queixa Alterada***\n"
    f"Consultas: {novoPaciente.consultas}\n"    
    )