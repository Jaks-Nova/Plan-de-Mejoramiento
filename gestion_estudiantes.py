print("Bienvenido a La Gestión de estudiantes \n")
print("""                 ／＞　 フ
                | 　_　_|
              ／` ミ＿xノ
             /　　　　 |
            /　 ヽ　　 ﾉ
           │　　|　|　|
        ／￣|　　 |　|　
        (￣ヽ＿_ヽ_)__)""")
print("-" * 30)
# ____________________________________________________________________________________________________________________________________________________

# Diccionario para almacenar los estudiantes
# Clave: numero de identificacion, Valor: diccionario con nombre, edad y notas
estudiantes = {}
# ____________________________________________________________________________________________________________________________________________________

# Funcion para registrar un estudiante
def registrar_estudiante():
    try:
        id = int(input("Numero de identificacion: "))
        if id in estudiantes:
            return "Este estudiante ya esta registrado"
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i+1} (0 a 5): "))
            while nota < 0 or nota > 5:
                nota = float(input("Nota invalida. Ingrese una nota entre 0 y 5: "))
            notas.append(nota)
        estudiantes[id] = { 
            "nombre": nombre,
            "edad": edad,
            "notas": notas
        }
        print(f"Estudiante {nombre} registrado.\n")
    except ValueError:
        print("Error: asegurate de ingresar los datos correctamente.\n")
        
# ____________________________________________________________________________________________________________________________________________________

# Funcion para consultar un estudiante
def consultar_estudiante():
    id = int(input("Ingrese el numero de identificacion: "))
    estudiante = estudiantes.get(id)
    if estudiante:
        promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
        print(f"\nNombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Notas: {estudiante['notas']}")
        print(f"Promedio: {promedio:.2f}\n")
    else:
        print("Estudiante no encontrado.\n")

# ____________________________________________________________________________________________________________________________________________________

# Funcion para actualizar notas
def actualizar_notas():
    id = int(input("Ingrese el numero de identificacion: "))
    if id in estudiantes:
        nuevas_notas = []
        for i in range(3):
            nota = float(input(f"Nota nueva {i+1} (0 a 5): "))
            while nota < 0 or nota > 5:
                nota = float(input("Nota invalida, Ingresar una nota entre 0 y 5: "))
            nuevas_notas.append(nota)
        estudiantes[id]["notas"] = nuevas_notas
        print(f"Notas actualizadas para {estudiantes[id]['nombre']}\n")
    else:
        print("Estudiante no encontrado.\n")

# ____________________________________________________________________________________________________________________________________________________

# Funcion para eliminar estudiante
def eliminar_estudiante():
    id = int(input("Ingrese el numero de identificación del estudiante a eliminar: "))
    if id in estudiantes:
        eliminado = estudiantes.pop(id)
        print(f" Estudiante {eliminado['nombre']} eliminado con exito.\n")
    else:
        print("Estudiante no encontrado.\n")

# ____________________________________________________________________________________________________________________________________________________

# Funcion para ver todos los estudiantes
def ver_todos_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    print("\nLista de todos los estudiantes:\n")
    for id, datos in estudiantes.items():
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print(f"ID: {id} | Nombre: {datos['nombre']} | Edad: {datos['edad']} | Promedio: {promedio:.2f}\n")

# ____________________________________________________________________________________________________________________________________________________

# Menu principal
def mostrar_menu():
    print("MENÚ DE OPCIONES ")
    print("1. Registrar estudiante")
    print("2. Consultar estudiante")
    print("3. Actualizar notas")
    print("4. Eliminar estudiante")
    print("5. Ver todos los estudiantes")
    print("6. Salir")

# ____________________________________________________________________________________________________________________________________________________

# Ejecución principal del programa
opcion = True
while opcion:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        consultar_estudiante()
    elif opcion == "3":
        actualizar_notas()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        ver_todos_estudiantes()
    elif opcion == "6":
        print("Finalizando programa...")
        opcion = False
    else:
        print(" Opción inválida. Intenta de nuevo.\n")