# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Diccionario para almacenar las tareas
tasks={}

#Funcion para agregar tareas
def add_task(id_task, description):
    tasks[id_task]={"description": description, "complete": False}
    pprint(f"Tarea '{description}' agregada con éxito")

#Función para marcar tarea como completada
def complete_task(id_task):
    if id_task in tasks:
        tasks[id_task]["complete"]=True
        print(f"Tarea '{tasks[id_task]['description']}' marcada como completada.")
    else:
        print(f"Tarea con ID {id_task} no encontrada.")

def menu():
    # Función principal para el menú
    while true:
        print("\n--- Menú de Lista de Tareas ---")
        print("\n 1. Agregar tarea")
        print("\n 2. Marcar tarea como completada")

        option = input("Seleccione una opción: ")

        if option=="1":
            id_task=input("Ingrese un ID de la tarea")
            description=input("Ingrese la descripción de la tarea")
            add_task(id_task, description)
        elif option=="2":
            id_task=input("Ingrese el ID de la tarea a completar")
            complete_task(id_task)
        else:
            print("\n Opción no válida")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
