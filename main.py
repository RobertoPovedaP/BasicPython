# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Diccionario para almacenar las tareas
tasks={}

#Funcion para agregar tareas
def add_task(id_task, description):
    tasks[id_task]={"description": description, "complete": False}
    print(f"Tarea '{description}' agregada con éxito")

#Función para marcar tarea como completada
def complete_task(id_task):
    if id_task in tasks:
        tasks[id_task]["complete"]=True
        print(f"Tarea '{tasks[id_task]['description']}' marcada como completada.")
    else:
        print(f"Tarea con ID {id_task} no encontrada.")

#Función para eliminar una tarea
def delete_task(id_task):
    if id_task in tasks:
        description=tasks[id_task]['description']
        del tasks[id_task]
        print(f"Tarea '{description}' eliminada.")
    else:
        print(f"Tarea con ID {id_task} no existe")
#Funcion para listar las tareas
def listar_tareas():
    if not tasks:
        print("No hay tareas en la lista")
    else:
        print("\nLista de tareas:")
        for id_task, detalles in tasks.items():
            estado="Complete" if detalles["complete"] else "Pendiente"
            print(f"{id_task}: {detalles['description']} - {estado}")

def menu():
    # Función principal para el menú
    while True:
        print("\n--- Menú de Lista de Tareas ---")
        print("\n 1. Agregar tarea")
        print("\n 2. Marcar tarea como completada")
        print("\n 3. Eliminar tarea")
        print("\n 4. Listar todas las tareas")
        print("\n 5. Salir")

        option = input("Seleccione una opción: ")

        if option=="1":
            id_task=input("Ingrese un ID de la tarea")
            description=input("Ingrese la descripción de la tarea")
            add_task(id_task, description)
        elif option=="2":
            id_task=input("Ingrese el ID de la tarea a completar")
            complete_task(id_task)
        elif option=="3":
            id_task=input("\n Ingresa el ID de la tarea a eliminar: ")
            delete_task(id_task)
        elif option == "4":
            listar_tareas()
        elif option == "5":
            print("\n Saliendo del gestor de tareas.")
            break
        else:
            print("\n Opción no válida")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
