class Nodo:
    dato = 0
    izdo = None
    dcho = None
    
    def __init__(self, valor,  ramaIzdo = None,   ramaDcho = None) :
        self.dato = valor
        if ramaIzdo is None and ramaDcho is None:
            self.izdo = None
            self.dcho = None
        else:
            self.izdo = ramaIzdo
            self.dcho = ramaDcho

    def  valorNodo(self) :
        return self.dato
    def  getSubarbolIzdo(self) :
        return self.izdo
    def  getSubarbolDcho(self) :
        return self.dcho
    def  nuevoValor(self, d) :
        self.dato = d
    def setRamaIzdo(self, n) :
        self.izdo = n
    def setRamaDcho(self, n) :
        self.dcho = n
    


class Arbol:
    raiz = None

    def insertar(self, dato, padre: Nodo = None):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        elif padre != None:
            if dato > padre.valorNodo():
                if padre.getSubarbolDcho() is None:
                    padre.setRamaDcho(Nodo(dato))
                else:
                    if padre.getSubarbolIzdo() is None:
                        padre.setRamaIzdo(Nodo(dato))
                    else:
                        self.insertar(dato, padre.getSubarbolIzdo)


arbol = Arbol()
arbol.insertar(1)
arbol.insertar(2)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(0)