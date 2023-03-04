class Room:
    """ En esta sala empieza el juego"""
    def __init__(self, descripcion, norte, sur, este, oeste):
        """metodo constructor, inicializa"""
        self.descripcion = descripcion
        self.norte = norte
        self.south = sur
        self.east = este
        self.west = oeste

def main():
    room_list = []
    #sala de inicio
    room = Room('Te encuentras en los pasadizos secretos de un castillo habitado por el principe bastardo.'
                'Fuiste atrapado y llevado a las mazmorras pero conseguiste escapar, deberas encontrar la salida'
                'antes de que noten la falta de tu presencia ¿Hacia dónde vas?', 3, 4, 1, 2)

    room_list.append(room)
    #sala1
    room = Room('Has llegado a una sala de reuniones secretas. Encuentras unos socumentos'
                'sobre la mesa y descubres que el principe esta planeando un golpe para ser el rey. ¡No puedes'
                'permitir que eso pase! Hay una puerta al norte', 8, None, None, 0)

    room_list.append(room)
    #sala2
    room = Room('Parece que has llegado a una sala utilizada como almacen pero...¡Espera! Eso no son conservas'
                'normales, por mis grandes conocimientos puedo asegurar que son botes de veneno. Debes salir pronto'
                'para que no puedan utilizarlos en contra del rey. Hay dos puertas, una al oeste y otra al sur', None,
                None, 0, 9)

    room_list.append(room)
    #sala3
    room = Room('Esta debe ser la sala de interrogatorios para los intrusos... No me da buena espina, salgamos de aqui'
                'Hay una puerta en el este '
                , None, 0, 8, None)

    room_list.append(room)
    #sala4
    room = Room('Esta sala esta vacía pero, hacia el este hay una puerta muy grande, ¡Podria ser la salida!', 0,
                None, 5, None)

    room_list.append(room)
    #sala5
    room = Room('¡Que decepcion! Una puerta tan grande y no es la de la salida... Bueno, ahora estás en lo que parece'
                ' la sala de descanso de los guardias. Hay una puerta en el sur', None, 6, None, 4)

    room_list.append(room)
    #sala6
    room = Room('Mmm, este pasillo me empieza a gustar más. Ve hacia el oeste hasta terminar el pasillo, esto es '
                'buena señal', 5, None, None, 7)

    room_list.append(room)
    #sala7
    room = Room('Wow, ¡que sala tan hermosa! Debe ser la galeria de arte personal del principe, lo que no entiendo es'
                '¿Por qué guardar tales obras de arte tan profundamente?. Bueno, tampoco es nuestro problema. Hay una'
                ' puerta al norte y otra al sur', None, None, 6, None)

    room_list.append(room)
    #sala9
    room = Room('¡Oh no, un guardia! debes dar la vuelta o te volveran a atrapar', None, None, 2, None)

    room_list.append(room)

    current_room = room_list[0]

    done = False


    main()
