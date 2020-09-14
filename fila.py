"""
Fila - Politica FIFO Fisrt IN First OUT

Dados armazenados:
* Sequência arbitrária de dados

Operações fornecidas:
* Criar esturura
* Inserir no fim da fila
* Remover do inicio da fila
* Saber o tamanho
* Verificar quem é o primeiro da fila sem remover
"""
from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def insere(self, novo):
        self.fila.append(novo)

    def remove(self):
        return self.fila.popleft()
    
    def removeUltimo(self):
        return self.fila.pop()

    def __len__(self):
        return len(self.fila)

    def proximo(self):
        prox = self.fila.popleft()
        self.fila.appendleft(prox)
        return prox
    
    def ultimo(self):
        ult = self.fila.pop()
        self.fila.append(ult)
        return ult

## Inserir elementos na fila
f = Fila()
f.insere(41)
f.insere(85)
f.insere(29)
f.insere(50)
f.insere(60)
print(f"Fila Atual: {f.fila}")
## Remoção do primeiro elemento
print(f"Elemento removido: {f.remove()}")
## Verificar tamanho da fila
print(f"Tamanho fa fila é: {f.__len__()}")
## Verificar o primeiro da fila (a esquerda)
print(f"Primeiro da fila: {f.proximo()}")
## Fila atual
print(f"Fila atual: {f.fila}")
## Remoção do elemento ultimo elemento
print(f"Elemento removido: {f.removeUltimo()}")
## Verificar ultimo da fila
print(f"Ultimo da fila: {f.ultimo()}")
## Fila atual
print(f"Fila atual: {f.fila}")
