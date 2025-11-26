def mostrar_menu():
    print("\n 3.1 Contenidos accesibles desde el menú")
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia. Resumen de fuente y definición")
    print("3. Estructura por tabla. Columnas y tipo")
    print("4. Escalas de medición. Descripción y ejemplos")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Salir")

def mostrar_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\n" + contenido)
    except FileNotFoundError:
        print(f" No se encontró el archivo {nombre_archivo}")

def mostrar_estructura(nombre_archivo, nombre_tabla):
    try:
        with open(nombre_archivo, encoding="utf-8") as archivo:
            primera_linea = archivo.readline()
            columnas = primera_linea.strip().split(",")
            print(f"\n Tabla: {nombre_tabla}")
            print("-" * 40)
            for col in columnas:
                if "id" in col.lower():
                    tipo = "int"
                    escala = "Nominal"
                elif "fecha" in col.lower():
                    tipo = "date"
                    escala = "Intervalo"
                elif "precio" in col.lower() or "importe" in col.lower() or "cantidad" in col.lower():
                    tipo = "int"
                    escala = "Razón"
                else:
                    tipo = "str"
                    escala = "Nominal"
                print(f"{col:<25} | {tipo:<10} | {escala}")
    except FileNotFoundError:
        print(f" No se encontró el archivo {nombre_archivo}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == "1":
            mostrar_desde_archivo("tema.txt")
        elif opcion == "2":
            mostrar_desde_archivo("dataset.txt")
        elif opcion == "3":
            mostrar_estructura("productos.csv", "Productos")
            mostrar_estructura("clientes.csv", "Clientes")
            mostrar_estructura("ventas.csv", "Ventas")
            mostrar_estructura("detalle_ventas.csv", "Detalle Ventas")
        elif opcion == "4":
            mostrar_desde_archivo("escalas.txt")
        elif opcion == "5":
            mostrar_desde_archivo("sugerencias.txt")
        elif opcion == "6":
            print(" Hasta luego!")
            break
        else:
            print(" Opción inválida. Probá de nuevo.")

main()
