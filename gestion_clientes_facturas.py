from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellidos, id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal
    
    @property
    def id_fiscal(self):
        return self.__id_fiscal
    
    @id_fiscal.setter
    def id_fiscal(self, value):
        self.__id_fiscal = value
    
    @abstractmethod
    def saludar(self):
        pass
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellidos}, ID Fiscal: {self.id_fiscal}"

class Cliente(Persona):
    contador_clientes = 0
    
    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre, apellidos, id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.contador_clientes += 1
    
    @classmethod
    def obtener_clientes_creados(cls):
        return cls.contador_clientes
    
    @staticmethod
    def saludar():
        return "¡Hola! Soy un cliente."
    
    def __del__(self):
        print(f"Cliente id: {self.id_cliente} eliminado")
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, value):
        self.__id_cliente = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
    
    def __str__(self):
        return f"Cliente {self.nombre} {self.apellidos}, ID Cliente: {self.id_cliente}, Email: {self.email}, {super().__str__()}"
    
    def __eq__(self, other):
        return isinstance(other, Cliente) and self.id_fiscal == other.id_fiscal

class Factura:
    def __init__(self, id_factura, cliente):
        self.id_factura = id_factura
        if not isinstance(cliente, Cliente):
            raise TypeError("El cliente debe ser una instancia de la clase Cliente")
        self.cliente = cliente
    
    @property
    def id_factura(self):
        return self.__id_factura
    
    @id_factura.setter
    def id_factura(self, value):
        self.__id_factura = value
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, value):
        if isinstance(value, Cliente):
            self.__cliente = value
        else:
            raise TypeError("El cliente debe ser una instancia de la clase Cliente")
    
    def __str__(self):
        return f"Factura ID: {self.id_factura}, Cliente: {self.cliente}"
    
    def __eq__(self, other):
        return isinstance(other, Factura) and self.id_factura == other.id_factura and self.cliente.id_fiscal == other.cliente.id_fiscal


cliente1 = Cliente("Juan", "Pérez", "12345678A", 1, "juan@example.com")
cliente2 = Cliente("Ana", "González", "87654321B", 2, "ana@example.com")

print(cliente1)
print(cliente2)

print(cliente1 == cliente2)

factura1 = Factura(101, cliente1)
factura2 = Factura(102, cliente2)

print(factura1)
print(factura2)

del cliente1
print(f"Clientes creados: {Cliente.obtener_clientes_creados()}")
