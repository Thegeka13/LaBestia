import random

class Character:
    def __init__(self, name="Sofia", initial_inventory=None, initial_room=0):
        self._name = name  # Atributo privado
        self._inventory = initial_inventory if initial_inventory else ["linterna"]  # Atributo privado
        self._current_room = initial_room  # Atributo privado

    # Getter y Setter para el nombre
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter y Setter para el inventario
    @property
    def inventory(self):
        return self._inventory

    def add_to_inventory(self, item):
        self._inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self._inventory:
            self._inventory.remove(item)
        else:
            print(f"El item {item} no está en el inventario.")

    # Getter y Setter para la habitación actual
    @property
    def current_room(self):
        return self._current_room

    @current_room.setter
    def current_room(self, room_index):
        self._current_room = room_index

    def __str__(self):
        return f"Personaje: {self._name}, Inventario: {self._inventory}, Habitación actual: {self._current_room}"


class Game:
    def __init__(self):
        self._rooms = ["Dormitorio", "Baño", "Sala de Estar", "Cocina", "Sótano"]  # Atributo privado
        self._items = ["Reloj de cuerda", "Lata", "Batería"]  # Atributo privado
        self.character = Character()

    # Getter para las habitaciones
    @property
    def rooms(self):
        return self._rooms

    # Getter para los items
    @property
    def items(self):
        return self._items

    # Generador de eventos aleatorios
    def random_event(self, range_init, range_end):
        return random.randint(range_init, range_end)

    # Método para mover al personaje a una nueva habitación
    def move_character(self, room_index):
        if 0 <= room_index < len(self._rooms):
            self.character.current_room = room_index
        else:
            print("Habitación no válida.")

    def __str__(self):
        return f"Habitaciones: {self._rooms}\nItems disponibles: {self._items}\n{self.character}"
