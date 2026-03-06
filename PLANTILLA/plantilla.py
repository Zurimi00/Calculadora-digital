"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: [Nombre] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Nombre] - Funciones Matemáticas
- Estudiante 3: [Luis Alejandro Ambriz Cordero] - Conversores y Sistema de Historial

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

import os
from datetime import datetime

# Variable global para almacenar historial (lista de strings)
historial = []

def borrar_historial():
  global historial
  #Dar la opción al usuario de borrar el historial, se repite hasta que se ingrese una opcion valida
  while True:
    try:
      opcion_borrar_historial = int(input("Seguro que quieres borrar el historial?\n1 = SI\n2 = NO\n"))

      if opcion_borrar_historial == 1:
        #Esto limpia el historial de la memoria
        historial.clear()
        if os.path.exists("datos/historial.txt"):
          with open("datos/historial.txt", "w") as archivo:
            archivo.write("")  # Vacía el archivo si es que existe
        print("✅ Historial borrado correctamente.")
        return
      elif opcion_borrar_historial == 2:
        #Esto vuelve al menu principal si se decide que no
        return
        #Se imprime si se elige una opcion invalida con numero entero
      else:
        print("Elige una de las opciones validas")
        #Se imprime si se elige una letra como opcion
    except ValueError:
      print("Error: Debes ingresar un número entero")

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la suma
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la resta
    """
    # TODO: Implementar
    pass


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la multiplicación
    """
    # TODO: Implementar
    pass


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Resultado de la división
        None: Si b es cero

    Raises:
        None: Retorna None en lugar de lanzar excepción
    """
    # TODO: Implementar
    # Verificar que b no sea cero
    # Si b == 0, retornar None
    # Si no, retornar a / b
    pass


def modulo(a, b):
    """
    Calcula el módulo (residuo) de dos números.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Residuo de la división
    """
    # TODO: Implementar
    pass


def potencia(a, b):
    """
    Calcula a elevado a la potencia b.

    Args:
        a (float): Base
        b (float): Exponente

    Returns:
        float: Resultado de a^b
    """
    # TODO: Implementar
    pass


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS (Estudiante 2)
# ============================================

def decimal_a_binario(numero):
    """
    Convierte un número decimal a binario usando algoritmo manual.

    Args:
        numero (int): Número decimal

    Returns:
        str: Representación binaria como string
    """
    # TODO: Implementar algoritmo de división sucesiva
    # Algoritmo:
    # 1. Crear string vacío para resultado
    # 2. Mientras numero > 0:
    #    - residuo = numero % 2
    #    - agregar residuo al inicio del string
    #    - numero = numero // 2
    # 3. Retornar el string
    # Caso especial: si numero == 0, retornar "0"
    pass


def decimal_a_hexadecimal(numero):
    """
    Convierte un número decimal a hexadecimal.

    Args:
        numero (int): Número decimal

    Returns:
        str: Representación hexadecimal como string
    """
    # TODO: Implementar
    # Pueden usar el método similar a binario
    # Recordar: 10=A, 11=B, 12=C, 13=D, 14=E, 15=F
    pass


def binario_a_decimal(binario):
    """
    Convierte un número binario (string) a decimal.

    Args:
        binario (str): Número binario como string

    Returns:
        int: Número decimal
    """
    # TODO: Implementar
    # Algoritmo:
    # 1. Inicializar decimal = 0
    # 2. Para cada dígito en binario (de derecha a izquierda):
    #    - decimal += dígito * (2 ^ posición)
    # 3. Retornar decimal
    pass


def hexadecimal_a_decimal(hexadecimal):
    """
    Convierte un número hexadecimal (string) a decimal.

    Args:
        hexadecimal (str): Número hexadecimal como string

    Returns:
        int: Número decimal
    """
    # TODO: Implementar
    pass


# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES (Estudiante 3)
# ============================================

def bytes_a_kilobytes(bytes_val):
    """
    Convierte bytes a kilobytes.

    Args:
        bytes_val (float): Cantidad en bytes

    Returns:
        float: Cantidad en kilobytes
    """
    return bytes_val / 1024


def kilobytes_a_megabytes(kb):
    """
    Convierte kilobytes a megabytes.

    Args:
        kb (float): Cantidad en kilobytes

    Returns:
        float: Cantidad en megabytes
    """
    # TODO: Implementar (1 MB = 1024 KB)
    pass


def megabytes_a_gigabytes(mb):
    """
    Convierte megabytes a gigabytes.

    Args:
        mb (float): Cantidad en megabytes

    Returns:
        float: Cantidad en gigabytes
    """
    # TODO: Implementar
    pass


# TODO: Implementar las funciones inversas
# gigabytes_a_megabytes(), megabytes_a_kilobytes(), kilobytes_a_bytes()


# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):
    """
    Agrega una operación al historial.

    Args:
        operacion (str): Tipo de operación (ej: "Suma", "División")
        num1 (float): Primer número
        num2 (float): Segundo número
        resultado (float): Resultado de la operación
    """
    global historial

    # TODO: Implementar
    # 1. Crear string con formato: "operación: num1 op num2 = resultado"
    # 2. Agregar al final de la lista historial
    # 3. Si historial tiene más de 10 elementos, eliminar el primero

    # Ejemplo de formato:
    # fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # entrada = f"{fecha_hora} | {operacion}: {num1} + {num2} = {resultado}"
    # historial.append(entrada)

    pass


def mostrar_historial():
    """
    Muestra el historial de operaciones.
    """
    global historial

    # TODO: Implementar
    # 1. Verificar si historial está vacío
    # 2. Si está vacío, mostrar mensaje
    # 3. Si no, iterar sobre historial y mostrar cada operación numerada

    pass


def limpiar_historial():
    """
    Limpia el historial de operaciones.
    """
    global historial

    # TODO: Implementar
    # Vaciar la lista historial
    pass


# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (Estudiante 1)
# ============================================

def guardar_historial_archivo():
    """
    Guarda el historial en el archivo datos/historial.txt
    """
    global historial

    # TODO: Implementar
    # 1. Crear carpeta "datos" si no existe (usar os.makedirs())
    # 2. Abrir archivo "datos/historial.txt" en modo escritura ("w")
    # 3. Escribir cada línea del historial al archivo
    # 4. Cerrar archivo

    # Ejemplo:
    # if not os.path.exists("datos"):
    #     os.makedirs("datos")
    #
    # with open("datos/historial.txt", "w") as archivo:
    #     for linea in historial:
    #         archivo.write(linea + "\n")

    pass


def cargar_historial_archivo():
    """
    Carga el historial desde el archivo datos/historial.txt
    """
    global historial

    # TODO: Implementar
    # 1. Verificar si el archivo existe (os.path.exists())
    # 2. Si existe:
    #    - Abrir archivo en modo lectura ("r")
    #    - Leer todas las líneas
    #    - Agregar cada línea (sin \n) a la lista historial
    # 3. Si no existe, no hacer nada

    pass


# ============================================
# SECCIÓN 6: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    """
    Solicita y valida un número al usuario.

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        float: Número validado
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Ingrese un número válido.")


def validar_numero_entero(mensaje):
    """
    Solicita y valida un número entero al usuario.

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        int: Número entero validado
    """
    # TODO: Implementar similar a validar_numero
    # pero convirtiendo a int en lugar de float
    pass


# ============================================
# SECCIÓN 7: MENÚS (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0")
    print("="*60)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora Básica")
    print("2. Conversor de Unidades de Datos")
    print("3. Calculadora de Sistemas Numéricos")
    print("4. Ver Historial")
    print("5. Limpiar Historial")
    print("6. Salir")
    print("-"*60)


def menu_calculadora_basica():
    """Menú y lógica de la calculadora básica"""
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo (residuo)")
    print("6. Potencia")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")

    if opcion == "7":
        return

    # Solicitar números
    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")

    # TODO: Implementar lógica según opción
    # - Si opcion == "1": resultado = sumar(num1, num2)
    # - Si opcion == "2": resultado = restar(num1, num2)
    # - etc.
    # - Mostrar resultado
    # - Llamar a agregar_al_historial()

    pass


def menu_conversor_unidades():
    """Menú y lógica del conversor de unidades"""
    # TODO: Implementar
    pass


def menu_sistemas_numericos():
    """Menú y lógica de conversión de sistemas numéricos"""
    # TODO: Implementar
    pass


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  CALCULADORA MULTIFUNCIONAL - Versión Avanzada".center(58) + "║")
    print("║" + " "*58 + "║")
    print("║" + "  Con historial, funciones y persistencia de datos".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

    # Cargar historial al iniciar
    cargar_historial_archivo()
    print("\n✅ Historial cargado desde archivo.")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_calculadora_basica()

        elif opcion == "2":
            menu_conversor_unidades()

        elif opcion == "3":
            menu_sistemas_numericos()

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            confirmacion = input("\n¿Está seguro de limpiar el historial? (s/n): ")
            if confirmacion.lower() == "s":
                limpiar_historial()
                print("✅ Historial limpiado.")

        elif opcion == "6":
            print("\n💾 Guardando historial...")
            guardar_historial_archivo()
            print("✅ Historial guardado en datos/historial.txt")
            print("\n¡Gracias por usar la Calculadora Multifuncional!")
            print("¡Hasta pronto! 👋")
            continuar = False

        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

    print("\nPrograma terminado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
    