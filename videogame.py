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
                'antes de que noten la falta de tu presencia ¿Hacia dónde vas?', 3, 4, 1, 2)

    room_list.append(room)

    room = Room('Has llegado a una sala de reuniones secretas. Encuentras unos socumentos'
                'sobre la mesa y descubres que el principe esta planeando un golpe para ser el rey. ¡No puedes'
                'permitir que eso pase! Hay dos puertas, una al norte y otra al sur', None, None, None, None)

    room_list.append(room)

    room = Room('¡Oh no, un guardia! debes dar la vuelta o te volveran a atrapar', None, None, None, None)

    room_list.append(room)

    room = Room('Esta debe ser la sala de interrogatorios para los intrusos... No me da buena espina, salgamos de aqui'
                'Hay una puerta en el ---- '
                , None, None, None, None)

    room_list.append(room)

    room = Room('Hacia el este hay una puerta muy grande, ¡Podria ser la salida!', None, None, None, None)

    room_list.append(room)

    room = Room('¡Vaya! has llegado a una sala sin salida, vuelve hacia atrás', None, None, None, None)

    room_list.append(room)

    current_room = room_list[0]

    done = False


    main()
