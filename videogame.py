class Room:
    """ Clase para crear las salas del juego"""

    def __init__(self, descripcion, norte, sur, este, oeste):
        """metodo constructor, inicializa"""
        self.descripcion = descripcion
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste


def main():
    room_list = []
    done = False
    # sala de inicio
    room = Room('Te encuentras en los pasadizos secretos de un castillo habitado por el principe bastardo.'
                'Fuiste atrapado y llevado a las mazmorras pero conseguiste escapar, deberas encontrar la salida '
                'antes de que noten la falta de tu presencia', 3, 4, 1, 2)

    room_list.append(room)
    # sala1
    room = Room('Has llegado a una sala de reuniones secretas. Encuentras unos socumentos'
                'sobre la mesa y descubres que el principe esta planeando un golpe para ser el rey. ¡No puedes'
                'permitir que eso pase! Hay una puerta al norte', 8, None, None, 0)

    room_list.append(room)
    # sala2
    room = Room('Parece que has llegado a una sala utilizada como almacen pero...¡Espera! Eso no son conservas'
                'normales, por mis grandes conocimientos puedo asegurar que son botes de veneno. Debes salir pronto'
                'para que no puedan utilizarlos en contra del rey. Hay una puerta al oeste', None,
                None, 0, 9)

    room_list.append(room)
    # sala3
    room = Room('Esta debe ser la sala de interrogatorios para los intrusos... No me da buena espina, salgamos de aqui.'
                ' Hay una puerta en el este ', None, 0, 8, None)

    room_list.append(room)
    # sala4
    room = Room('Esta sala esta vacía pero, hacia el este hay una puerta muy grande, ¡Podria ser la salida!', 0,
                None, 5, None)

    room_list.append(room)
    # sala5
    room = Room('¡Que decepcion! Una puerta tan grande y no es la de la salida... Bueno, ahora estás en lo que parece'
                ' la sala de descanso de los guardias. Hay una puerta en el sur', None, 6, None, 4)

    room_list.append(room)
    # sala6
    room = Room('Mmm, este pasillo me empieza a gustar más. Ve hacia el oeste hasta terminar el pasillo, esto es '
                'buena señal', 5, None, None, 7)

    room_list.append(room)
    # sala7
    room = Room('Wow, ¡que sala tan hermosa! Debe ser la galeria de arte personal del principe, lo que no entiendo es'
                '¿Por qué guardar tales obras de arte tan profundamente?. Bueno, tampoco es nuestro problema. Hay una'
                ' puerta al norte y otra al sur', 2, 10, 6, None)

    room_list.append(room)

    # sala8
    room = Room('Vaya... había rumores de que en estos pasadizos había una sala para torturas pero nunca pensé que '
                'fuera cierto. Mejor salgamos antes de que decidan usarla en nuestra contra. Hay dos puertas, una'
                ' al oeste y por la que entraste', None, 1, None, 3)
    room_list.append(room)

    # sala9
    room = Room('¡Oh no, un guardia! debes dar la vuelta o te volveran a atrapar', None, None, 2, None)

    room_list.append(room)

    # final

    room = Room('¡Felicidades!, conseguiste escapar del castillo', None, None, None, None)

    room_list.append(room)

    current_room = room_list[0]

    # instrucciones
    print('\n')
    print('Para moverte por el juego solo se aceptarán las palabras norte, sur, este, oeste y las letras n, s , e, o. '
          'Si desea salir del juego escribe salir')

    while not done:
        print()
        print(current_room.descripcion)
        direccion = input('¿Hacia donde vas? ')

        if direccion.lower() == 'n' or direccion.lower() == 'norte':
            if room_list[current_room.norte] is None:
                print('La dirección no es válida')
                current_room = room_list[current_room.sur]
            else:
                current_room = room_list[current_room.norte]
        elif direccion.lower() == 's' or direccion.lower() == 'sur':
            if room_list[current_room.sur] is None:
                 print('La dirección no es válida')
                 current_room = room_list[current_room.norte]
            else:
                current_room = room_list[current_room.sur]
        elif direccion.lower() == 'e' or direccion.lower() == 'este':
            if room_list[current_room.este] is None:
                print('La dirección no es válida')
                current_room = room_list[current_room.oeste]
            else:
                current_room = room_list[current_room.este]
        elif direccion.lower() == 'o' or direccion.lower() == 'oeste':
            if room_list[current_room.oeste] is None:
                print('La dirección no es válida')
                current_room = room_list[current_room.este]
            else:
                current_room = room_list[current_room.oeste]
        elif direccion.lower() == 'salir':
            done = True
        else:
            print('Lo siento, no entiendo lo que dices')

        if current_room == room_list[10]:
            print(current_room.descripcion)
            done = True


main()
