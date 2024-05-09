Equipos_con_mas_champions = [
    ("Real Madrid", 14), ("AC Milan", 7), ("Liverpool", 6),
    ("Bayern Munich", 6), ("Barcelona", 5), ("Ajax", 4),
    ("Manchester United", 3), ("Inter Milan", 3), ("Juventus", 2),
    ("Benfica", 2), ("Nottingham Forest", 2), ("Porto", 2),
    ("Chelsea", 2), ("Borussia Dortmund", 1), ("Marseille", 1),
    ("Feyenoord", 1), ("PSV Eindhoven", 1), ("Celtic", 1),
    ("Hamburg", 1), ("Steaua București", 1)
]

print("¡Hola! ¿Qué deseas hacer?")
print("1. Ver equipos por número de Champions ganadas")
print("2. Salir")

opcion = input("Ingrese el número de la opción que desea: ")

if opcion == "1":
    numero_champions = input("Ingrese el número de Champions ganadas: ")
    if numero_champions.isdigit():
        numero_champions = int(numero_champions)
        equipos_filtrados = [equipo for equipo, champions in Equipos_con_mas_champions if champions == numero_champions]
        if equipos_filtrados:
            print(f"Equipos que han ganado {numero_champions} Champions League:")
            for equipo in equipos_filtrados:
                print(equipo)
        else:
            print(f"No hay equipos que hayan ganado {numero_champions} Champions League.")
    else:
        print("Por favor, ingrese un número válido.")

elif opcion == "2":
    print("¡Hasta luego!")

else:
    print("Opción inválida. Por favor, ingrese 1 o 2.")