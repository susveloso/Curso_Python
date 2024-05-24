class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f'{i+1}. {tarea.descripcion} - {estado}')

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")

# Programa principal
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
        