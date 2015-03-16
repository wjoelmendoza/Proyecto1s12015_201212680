__author__ = 'walter'
from estructura.Nodo import NodoD

class ListaDobleUser(object):
    def __init__(self):
        self.origen = None
        self.size=0
        self.fin = None

    def add_element(self, dato):
        self.size += 1
        nodo_n = NodoD(dato)
        if self.origen<>None:
            self.fin.set_siguiente(nodo_n)
            nodo_n.set_anterior(self.fin)
            self.fin = nodo_n
        else:
            self.origen = self.fin = nodo_n


    def del_element(self, dato):
        count=0
        if(self.origen <> None):
            aux = self.origen
            while (aux <> None):
                if aux.get_dato() == dato:
                    aux_1 = aux.get_anterior()

                    aux_2 = aux.get_siguiente()
                    aux_1.set_siguiente(aux_2)
                    aux_2.set_anterior(aux_1)
                    self.size -=1
                    print "Se elimino"
                    break
                else:
                    count += 1
                aux = aux.get_siguiente()

            if count == self.size:
                print "no se encontro coincidencia"
        else:
            print "No se elimino ningun dato; Lista vacia"

    def get_size(self):
        return self.size

    def recorrer(self):
        if(self.origen <> None):
            aux = self.origen
            while(aux <> None):
                print aux.get_dato() + ";"
                aux=aux.get_siguiente()
        else:
            print "sin datos"
