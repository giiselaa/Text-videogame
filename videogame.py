class Room:
    """ En esta sala empieza el juego"""
    def __init__(self, description, north, south, east, west):
        """metodo constructor, inicializa"""
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    room_list = []

    room = Room('Te encuentras en los pasadizos secretos de un castillo habitado por el principe bastardo.'
                'Fuiste atrapado y llevado a las mazmorras pero conseguiste escapar, deberas encontrar la salida'
                'antes de que noten la falta de tu presencia', 3, 4, 1, 2)

    room = Room('Has llegado a una sala de reuniones secretas. Encuentras unos socumentos'
                'sobre la mesa y descubres que el principe esta planeando un golpe para ser el rey. ¡No puedes'
                'permitir que eso pase!', None, None, None, None)

    room = Room('¡Oh no, un guardia! debes dar la vuelta o te volvera a atrapar', None, None, None, None)

    room = Room('Esta debe ser la sala de interrogatorios para los intrusos... No me da buena espina, salgamos de aqui'
                , None, None, None, None)

    room = Room('Hacia el este hay una puerta muy grande, ¡Podria ser la salida!', None, None, None, None)

    room_list.append(room)

    current_room = 0

    main()
