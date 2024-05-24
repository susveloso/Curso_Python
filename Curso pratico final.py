class Tarea:
    ''' Clase para representar las tareas.

    - descripcion:   un texto para describir la tarea
    - completada:    estado de la tarea:  True si está completada
    '''
    def __init__(self, descripcion, completada=False):
        # constructor de la tarea
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    ''' Clase con los métodos para gestionar las tareas

    - tareas:   una lista con todas las tareas creadas
    '''
    def __init__(self):
        # constructor del gestor de tareas
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # crea una tarea con la descripción facilitada y la añade a self.tareas
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def marcar_completada(self, posicion):
        # cambia el estado de una tarea a completda
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        # muestra una lista de las tareas creadas, con su posición y descripción
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f'{i+1}. {tarea.descripcion} - {estado}')

    def eliminar_tarea(self, posicion):
        # elimina una tarea
        try:
            del self.tareas[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")


''' Programa principal

Bucle del programa principal que hace las siguientes acciones:
- muestra las opciones
- pide una opción al usuario
- y la ejecuta
'''
gestor = GestorTareas()

while True:
    print("\n1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        descripcion = input("Ingrese la descripción de la tarea: ")
        gestor.agregar_tarea(descripcion)
    elif opcion == "2":
        posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
        gestor.marcar_completada(posicion)
    elif opcion == "3":
        gestor.mostrar_tareas()
    elif opcion == "4":
        posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
        gestor.eliminar_tarea(posicion)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
