"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: Luis Daniel Negrete Mata - Estructura Principal y Gestión de Datos
- Estudiante 2: Zurith Anelis Fierros Garcia  - Funciones Matemáticas
- Estudiante 3: Luis Alejandro Ambriz Cordero - Conversores y Sistema de Historial

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL"""

import os
from datetime import datetime

# Variable global para almacenar historial (lista de strings)
historial = []

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

#Funciones simples 

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def potencia(a, b): return a ** b  

def modulo(a, b):
  #Division de modulo con validacion de division por cero
  if b == 0: return None
  return a % b

def dividir(a, b):
    # División con validación de división por cero
    if b == 0: return None
    return a / b


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS 
# ============================================

def decimal_a_binario(numero):
    if numero == 0: return "0"
    resultado = ""
    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado
        numero //= 2
    return resultado


def decimal_a_hexadecimal(numero):
    if numero == 0: return "0"
    valores_hex= "0123456789ABCDEF"
    resultado = ""

    while numero > 0:
        residuo = numero % 16
        resultado = valores_hex[residuo] + resultado
        numero = numero // 16
    
    return resultado

def binario_a_decimal(binario):
#Convierte el numero ingresado a string y luego a int para obtener el valor decimal
    decimal = 0
    binario_str = str(binario)[::-1]

    for posicion in range(len(binario_str)):
        digito = int(binario_str[posicion])
        decimal += digito *(2 ** posicion)

    return decimal


def hexadecimal_a_decimal(hexadecimal):
     
     return int(str(hexadecimal), 16)



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
    