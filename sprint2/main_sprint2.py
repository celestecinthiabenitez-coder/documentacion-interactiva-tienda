import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Carga de datasets con pandas
# =========================
def cargar_datos():
    df_productos = pd.read_csv("productos99.csv")
    df_clientes = pd.read_csv("clientes99.csv")
    df_ventas = pd.read_csv("ventas99.csv", sep=";")
    df_detalle = pd.read_csv("detalle_ventas99.csv")

    # Limpieza mínima
    for col in ["id_venta","id_producto","cantidad","precio_unitario","importe"]:
        if col in df_detalle.columns:
            df_detalle[col] = pd.to_numeric(df_detalle[col], errors="coerce")

    for col in ["id_venta","id_cliente","fecha"]:
        if col in df_ventas.columns:
            df_ventas[col] = pd.to_numeric(df_ventas[col], errors="coerce")

    for col in ["id_cliente","fecha_alta"]:
        if col in df_clientes.columns:
            df_clientes[col] = pd.to_numeric(df_clientes[col], errors="coerce")

    for col in ["id_producto","precio_unitario"]:
        if col in df_productos.columns:
            df_productos[col] = pd.to_numeric(df_productos[col], errors="coerce")

    return df_productos, df_clientes, df_ventas, df_detalle

# =========================
# Funciones de visualización y análisis
# =========================
def mostrar_menu():
    print("\n 3.1 Contenidos accesibles desde el menú")
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia. Resumen de fuente y definición")
    print("3. Estructura por tabla. Columnas y tipo (pandas)")
    print("4. Escalas de medición. Descripción y ejemplos")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Salir")
    print("7. Estadística aplicada (con gráficos)")

def mostrar_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, encoding="utf-8") as archivo:
            print("\n" + archivo.read())
    except FileNotFoundError:
        print(f" No se encontró el archivo {nombre_archivo}")

def mostrar_estructura_pandas(df, nombre_tabla):
    print(f"\n Tabla: {nombre_tabla}")
    print("-" * 40)
    print("Tipos de datos:")
    print(df.dtypes)
    print("\nColumnas:")
    print(list(df.columns))
    print("\nPrimeras 5 filas:")
    print(df.head())

def estadistica_aplicada(df_productos, df_clientes, df_ventas, df_detalle):
    print("\n  Estadística aplicada")

    # ---------- 1) Descriptiva ----------
    precios = pd.to_numeric(df_productos["precio_unitario"], errors="coerce").dropna()
    precios = precios[precios > 0]
    print("\n--- Descriptiva: precios de productos ---")
    print(precios.describe())

    # Histograma de precios
    plt.figure(figsize=(6,4))
    plt.hist(precios, bins=30, color="skyblue", edgecolor="black")
    plt.title("Distribución de precios de productos")
    plt.xlabel("Precio unitario")
    plt.ylabel("Frecuencia")
    plt.show()

    print("\n--- Descriptiva: clientes por ciudad ---")
    print(df_clientes["ciudad"].value_counts())

    print("\n--- Descriptiva: medios de pago ---")
    print(df_ventas["medio_pago"].value_counts())

    # ---------- 2) Distribución ----------
    cantidades = pd.to_numeric(df_detalle["cantidad"], errors="coerce").dropna()
    cantidades = cantidades[cantidades > 0]
    print("\n--- Distribución: cantidades vendidas ---")
    print(cantidades.value_counts().head(10))

    # Boxplot de cantidades
    plt.figure(figsize=(6,4))
    sns.boxplot(x=cantidades, color="lightgreen")
    plt.title("Boxplot de cantidades vendidas")
    plt.show()

    # ---------- 3) Correlaciones ----------
    num = df_detalle[["cantidad","precio_unitario","importe"]].apply(pd.to_numeric, errors="coerce")
    num = num[num["cantidad"] > 0]
    print("\n--- Correlaciones ---")
    print(num.corr())

    # Heatmap de correlaciones
    plt.figure(figsize=(6,4))
    sns.heatmap(num.corr(), annot=True, cmap="coolwarm")
    plt.title("Matriz de correlaciones")
    plt.show()

# =========================
# Programa principal
# =========================
def main():
    df_productos, df_clientes, df_ventas, df_detalle = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ").strip()
        if opcion == "1":
            mostrar_desde_archivo("tema.txt")
        elif opcion == "2":
            mostrar_desde_archivo("dataset.txt")
        elif opcion == "3":
            mostrar_estructura_pandas(df_productos, "Productos")
            mostrar_estructura_pandas(df_clientes, "Clientes")
            mostrar_estructura_pandas(df_ventas, "Ventas")
            mostrar_estructura_pandas(df_detalle, "Detalle Ventas")
        elif opcion == "4":
            mostrar_desde_archivo("escalas.txt")
        elif opcion == "5":
            mostrar_desde_archivo("sugerencias.txt")
        elif opcion == "6":
            print(" Hasta luego!")
            break
        elif opcion == "7":
            estadistica_aplicada(df_productos, df_clientes, df_ventas, df_detalle)
        else:
            print(" Opción inválida. Probá de nuevo.")

if __name__ == "__main__":
    main()


