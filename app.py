import yaml

direccionArchivo = "personas.yaml"

def cargar_datos():
    try:
        with open(direccionArchivo, "r") as f:
            return yaml.safe_load(f) or {"personas": []}
    except FileNotFoundError:
        return {"personas": []}

def guardar_datos(data):
    with open(direccionArchivo, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False)

def listar_personas(data):
    print("\nLista de personas:")
    for i, p in enumerate(data["personas"], start=1):
        print(f"{i}. {p['nombre']}, {p['edad']} años, vive en {p['ciudad']}")

def agregar_persona(data):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")
    nueva = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    data["personas"].append(nueva)
    guardar_datos(data)
    print("Persona agregada.")

def buscar_por_ciudad(data):
    ciudad = input("Ciudad a buscar: ")
    resultados = [p for p in data["personas"] if p["ciudad"].lower() == ciudad.lower()]
    if resultados:
        print(f"\nPersonas en {ciudad}:")
        for p in resultados:
            print(f"- {p['nombre']} ({p['edad']} años)")
    else:
        print("No se encontraron personas en esa ciudad.")

def menu():
    data = cargar_datos()
    while True:
        print("\n--- MENÚ ---")
        print("1. Listar personas")
        print("2. Agregar persona")
        print("3. Buscar por ciudad")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_personas(data)
        elif opcion == "2":
            agregar_persona(data)
        elif opcion == "3":
            buscar_por_ciudad(data)
        elif opcion == "4":
            print("Adios")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
