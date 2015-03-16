__author__ = 'walter'

class Usuario():
    def __init__(self, nombre, password,alias,direccion, telefono, noTarjeta):
        self.nombre=nombre
        self.pasword = password
        self.alias = alias
        self.direccion = direccion
        self.telefono = telefono
        self.noTarjeta = noTarjeta

    def get_alias(self):
        return  self.alias

    def get_direccion(self):
        return self.direccion

    def get_nombre(self):
        return self.nombre

    def get_noTarjeta(self):
        return self.noTarjeta

    def get_telefono(self):
        return self.telefono

    def get_password(self):
        return self.pasword

    def valida_usuario(self, alias, password):
        return self.alias == alias and self.password == password

    def set_alias(self,alias):
        self.alias=alias

    def set_direccion(self,direccion):
        self.direccion = direccion

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_noTarjeta(self,noTarjeta):
        self.noTarjeta = noTarjeta

    def set_telefono(self,telefono):
        self.telefono = telefono

    def set_password(self,password):
        self.pasword = password