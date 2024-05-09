

lista_de_estudiantes = []  

lista_de_estudiantes.append("Daddy Acacho")
lista_de_estudiantes.append("Anthony Perez")
lista_de_estudiantes.append("Kevin Cuenca")
print("Hola, bienvenido. ¿Qué deseas hacer?")
print("1. Buscar un estudiante")
print("2. Ingresar un nuevo estudiante")
opcion = input("Ingrese el número de la opción: ")
print(lista_de_estudiantes)  


nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
lista_de_estudiantes.append(nuevo_estudiante)

estudiante_a_buscar = input("Ingrese el nombre del estudiante a buscar: ")

if estudiante_a_buscar in lista_de_estudiantes:
    print(f"{estudiante_a_buscar} está en la lista de estudiantes.")
else:
    print(f"{estudiante_a_buscar} no está en la lista de estudiantes.")
print("Lista actualizada de estudiantes:")
print(lista_de_estudiantes)