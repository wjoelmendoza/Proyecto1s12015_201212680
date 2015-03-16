__author__ = 'walter'

class NodoD(object):
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_anterior(self, anterior):
        self.anterior = anterior

    def get_siguiente(self):
        return self.siguiente

    def get_anterior(self):
        return self.anterior

    def get_dato(self):
        return self.dato

class NodoA(object):
    def __init__(self,valor):
        self.fe =0
        self.valor = valor
        self.nDer = None
        self.nIzq= None

    def get_valor(self):
        return self.valor

    def get_n_der(self):
        return self.nDer

    def get_n_izq(self):
        return self.nDer

    def set_valor(self,valor):
        self.valor=valor

    def set_n_der(self, nodoDer):
        self.nDer = nodoDer

    def set_n_izq(self,nodoIzq):
        self.nIzq=nodoIzq

    def get_factor(self):
        return self.fe

    def set_factor(self,fe):
        self.fe = fe

    def print_dato(self):
        print self.dato