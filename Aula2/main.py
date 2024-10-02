# # 2A - Definir classe Dog e instanciar o seu objeto no main
# class Dog:
#     def __init__(self):
#         pass
#
# # ----main
# rex = Dog()
# print(rex)
###

# # 2B - Inserir Atributos com valor fixo
# class Dog:
#     def __init__(self): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self.age = 5 # Boa prática de programação conforme a PEP8 - todos os atributos são instanciados dentro do "init"
#
# # ----main
# rex = Dog()
# print(f'A idade do rex é: {rex.age}')
# caramelo = Dog()
# print(f'A idade do caramelo é: {caramelo.age}')
###

# # 2C - Inserir Atributos com passagem de parâmetros no construtor da class
# class Dog:
#     def __init__(self, age): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self.age = age
#
# # ----main
# rex = Dog(10)
# print(f'A idade do rex é: {rex.age}')
# caramelo = Dog(5)
# print(f'A idade do caramelo é: {caramelo.age}')
###

# # 2D - Atributo da classe
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self.age = age
#
# # ----main
# rex = Dog(10)
# print(f'A idade do rex é: {rex.age} e pertence a família: {rex.family}')
# caramelo = Dog(5)
# print(f'A idade do caramelo é: {caramelo.age} e pertence a família: {caramelo.family}')
#
# print(f'A família que pertence a todos os cachorros: {Dog.family}')
###

# 2E - Definindo o tipo de um atributo
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age: int): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self.age: int = age
#         self.age.real
#
# # ----main
# rex = Dog(10)
# print(f'A idade do rex é: {rex.age} e pertence a família: {rex.family}')
# caramelo = Dog(5)
# print(f'A idade do caramelo é: {caramelo.age} e pertence a família: {caramelo.family}')
#
# print(f'A família que pertence a todos os cachorros: {Dog.family}')
###

# # 2F - Atributos Especiais __class__ e __name__
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age: int): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self.age: int = age
#         self.age.real
#
# # ----main
# rex = Dog(10)
# print(f'A idade do rex é: {rex.age} e pertence a família: {rex.family}')
# caramelo = Dog(5)
# print(f'A idade do caramelo é: {caramelo.age} e pertence a família: {caramelo.family}')
#
# print(f'Rex é um objeto de qual classe? R:{rex.__class__.__name__}')
# print(f'Caramelo é um objeto de qual classe? R:{caramelo.__class__.__name__}')
###

# # 2G - Atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age, peso): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self._age = age # _ uma dica que é um atributo privado e não deve ser modificado diretamente fora da classe.
#         self.__peso = peso # __ o interpretador Python realiza uma "mangling!", no qual evita colisão de nomes.
#
# # ----main
# rex = Dog(10,45)
# print(f'Rex - idade: {rex.age}, peso: {rex.peso} e pertence a familia: {rex.family}')
# caramelo = Dog(5, 30)
# print(f'Rex - idade: {caramelo.age}, peso: {caramelo.peso} e pertence a familia: {caramelo.family}')
#
# print(f'A que família pertence todos os cachorros: {Dog.family}')
###

# # 2H - Utilizando métodos
#     # < 2G > - Atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age): # O "__" refere-se a métodos especiais inv. automaticamente em situações específicas.
#         self._age = age # _ uma dica que é um atributo privado e não deve ser modificado diretamente fora da classe.
#         self.__peso = 0
#
#     def get_age(self) -> int: #pode se definir o dado de retorno
#         return self._age
#
#     def get_peso(self) -> int: #pode se definir o dado de retorno
#         return self.__peso
#
#     def set_peso(self, peso: int): # pode se definir o dado de entrada
#         self.__peso = peso
#
# # ----main
# rex = Dog(10)
# rex.set_peso(45)
# print(f'Rex - idade: {rex.get_age()}, peso: {rex.get_peso()} e pertence a familia: {rex.family}')
# caramelo = Dog(5)
# caramelo.set_peso(30)
# print(f'Caramelo - idade: {caramelo.get_age()}, peso: {caramelo.get_peso()} e pertence a familia: {caramelo.family}')
#
# print(f'A que família pertence todos os cachorros: {Dog.family}')
###

# 3 - Herança

class Animal:
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        self.age = age
        self.height = height
        self.weight = weight
        self.position: tuple = position # posiiton [position_x, position_y, position_z]

    def move_x(self):
        self.position[0] += 1

    def move_y(self):
        self.position[1] += 1

    def move_z(self):
        self.position[2] += 1

class Dog(Animal):
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        super().__init__(self, age, height, weight, position)

        def move_z(self):
            self.position[2] += 2

caramelo = Dog(age=10, weight=30, position=(0, 0, 0), height=10)
print(caramelo.age)