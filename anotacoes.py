class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data): # Função para colocar os elementos dentro da pilha 
        # ______________Complete aqui______________

    def pop(self):
        # ______________Complete aqui______________


    def get(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next_node
        return elements


def main():
    stack = Stack()

    elements = input() # O input vai ser colocado aqui

    for element in elements.split(): # Separar o input 
        stack.push(element) # Vai adicionar os elementos na pilha

    print(f"Pilha: {stack.get()}")

    for _ in range(len(elements.split())):
        popped_element = stack.pop()
        print(f"Removido: {popped_element}")
        print(f"Pilha: {stack.get()}")

if __name__ == "__main__":
    main()


# DUVIDAS: como colocar os dados no topo
# Lista encadeada

# Tipos abstratos de dados: é um "contrato" de como vai ser usado aquele dado

# Pesquisar dados vazios em python 
