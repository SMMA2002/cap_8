class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierdo is None:
                self.izquierdo = Nodo(valor)
            else:
                self.izquierdo.insertar(valor)
        elif valor > self.valor:
            if self.derecho is None:
                self.derecho = Nodo(valor)
            else:
                self.derecho.insertar(valor)
    
    def recorrido_inorden(self):
        if self.izquierdo:
            self.izquierdo.recorrido_inorden()
        print(self.valor, end=' ')
        if self.derecho:
            self.derecho.recorrido_inorden()
            
    def recorrido_preorden(self):
        print(self.valor, end=' ')
        if self.izquierdo:
            self.izquierdo.recorrido_preorden()
        if self.derecho:
            self.derecho.recorrido_preorden()
            
    def recorrido_postorden(self):
        if self.izquierdo:
            self.izquierdo.recorrido_postorden()
        if self.derecho:
            self.derecho.recorrido_postorden()
        print(self.valor, end=' ')

nodo_raiz = Nodo(6)

nodo_raiz.insertar(3)
nodo_raiz.insertar(4)
nodo_raiz.insertar(10)
nodo_raiz.insertar(25)
nodo_raiz.insertar(13)
nodo_raiz.insertar(24)
nodo_raiz.insertar(22)
nodo_raiz.insertar(35)

print("Recorrido inorden:")
nodo_raiz.recorrido_inorden()

print("\nRecorrido preorden:")
nodo_raiz.recorrido_preorden()

print("\nRecorrido postorden:")
nodo_raiz.recorrido_postorden()