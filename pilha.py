"""
Pilha - Politica LIFO (LAST IN FORST OUT)

Dados armazenados:
* Sequência arbitrária de dados

Operações fornecidas:
* Criar estrutura
* Inserir no topo
* Remover do topo
* Consultar o topo sem remover
* Consultar o tamanho (número de elementos) 
"""

class Pilha:
    def __init__(self):
        self.pilha = []
        self.tamanho = 0
    
    def insere(self,novo):
        self.pilha.append(novo)
        self.tamanho += 1
    
    def remove(self):
        self.tamanho -= 1
        return self.pilha.pop()

    def topo(self):
        return self.pilha[-1]
    
    def __len__(self):
        return self.tamanho

p = Pilha()
p.insere(101)
p.insere(102)
p.insere(103)
print(f"Pilha atual: {p.pilha}")

p.remove()
print(f"Pilha -1: {p.pilha}")

print(f"Elemento do topo: {p.topo()}")

print(f"Total de elementos: {p.__len__()}")