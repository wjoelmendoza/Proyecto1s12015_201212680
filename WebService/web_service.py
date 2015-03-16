__author__ = 'walter'

from estructura.ListaD import ListaDobleUser

if __name__=="__main__":
    lista = ListaDobleUser()
    lista.add_element("Andrea")
    lista.add_element("Mackey")
    lista.add_element("Walter")
    lista.add_element("Michelle")
    print lista.get_size()
    lista.recorrer()
    lista.del_element("Mackey")
    lista.del_element("nada")
    print lista.get_size()
    lista.recorrer()