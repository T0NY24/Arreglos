Trabajadores_Empresa_Hexabite = {
    3: {"nombre": "Juan", "trabajo": "Ingeniero"},
    1: {"nombre": "María", "trabajo": "Doctora"},
    5: {"nombre": "Carlos", "trabajo": "Profesor"},
    2: {"nombre": "Laura", "trabajo": "Abogada"},
    4: {"nombre": "Pedro", "trabajo": "Chef"}
}
print("Lista de trabajadores:")
for codigo, persona in Trabajadores_Empresa_Hexabite.items():
    print(f"Código: {codigo}, Nombre: {persona['nombre']}, Trabajo: {persona['trabajo']}")


ordenar = input("¿Desea ordenar los trabajadores? (1: Sí, 2: No): ")

if ordenar == "1":
   
    lista_trabajadores_ordenados = sorted(Trabajadores_Empresa_Hexabite.items())
    print("Lista de trabajadores ordenada por código:")
    for codigo, persona in lista_trabajadores_ordenados:
        print(f"Código: {codigo}, Nombre: {persona['nombre']}, Trabajo: {persona['trabajo']}")
elif ordenar == "2":
    pass
else:
    print("Opción inválida.")


buscar = input("¿Desea buscar un trabajador por código? (1: Sí, 2: No): ")

if buscar == "1":
    codigo_buscado = int(input("Ingrese el código del trabajador: "))
    if codigo_buscado in Trabajadores_Empresa_Hexabite:
        persona = Trabajadores_Empresa_Hexabite[codigo_buscado]
        print(f"Trabajador encontrado - Código: {codigo_buscado}, Nombre: {persona['nombre']}, Trabajo: {persona['trabajo']}")
    else:
        print("Trabajador no encontrado.")
elif buscar == "2":
    pass
else:
    print("Opción inválida.")

