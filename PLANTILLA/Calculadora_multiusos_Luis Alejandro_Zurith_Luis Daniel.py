"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:

- Estudiante 1: [Luis Daniel Negrete Mata ] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Zurith Anelis Fierros García] - Funciones Matemáticas
- Estudiante 3: [Luis Alejandro Ambriz Cordero] - Conversores y Sistema de Historial


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

# CONVERTIDOR
# Conversiones que ocupamos
def bits_a_bytes(val): return val / 8
def kilobytes_a_megabytes(val): return val / 1000
def megabytes_a_gigabytes(val): return val / 1000
def gigabytes_a_megabytes(val): return val * 1000
def megabytes_a_kilobytes(val): return val / 1000
def kilobytes_a_bytes(val): return val * 1000


# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):
    global historial
    fecha_hora = datetime.now().strftime("%H:%M:%S")
    if num2 == "-":
        entrada = f"[{fecha_hora}] {operacion}({num1}) = {resultado}"
    else:
        entrada = f"[{fecha_hora}] {operacion}: {num1} y {num2} = {resultado}"
    historial.append(entrada)
    if len(historial) > 10: historial.pop(0)


def mostrar_historial():
    print("\n" + "HISTORIAL RECIENTE " * 2)
    if not historial:
        print("   > El historial está vacío.")
    else:
        for i, registro in enumerate(historial, 1):
            print(f"  {i}. {registro}")


def borrar_historial():
    global historial
    while True:
        try:
            opcion = int(input("\n¿Borrar historial?\n1 = SI\n2 = NO\n> "))
            if opcion == 1:
                historial.clear()
                if os.path.exists("datos/historial.txt"): os.remove("datos/historial.txt")
                print("✅ Historial borrado.")
                return
            elif opcion == 2:
                return
        except ValueError:
            print("Error: Ingresa un número (1 o 2).")


# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (Estudiante 1)
# ============================================

def guardar_historial_archivo():
    if not os.path.exists("datos"): os.makedirs("datos")
    with open("datos/historial.txt", "w") as archivo:
        for linea in historial: archivo.write(linea + "\n")


def cargar_historial_archivo():
    global historial
    if os.path.exists("datos/historial.txt"):
        with open("datos/historial.txt", "r") as archivo:
            historial = [linea.strip() for linea in archivo.readlines()]


# ============================================
# SECCIÓN 6: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" ❌ Error: Ingrese un número válido.")


def validar_numero_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" ❌ Error: Ingrese un número entero.")


# ============================================
# SECCIÓN 7: MENÚS (Estudiante 1)
# ============================================

def menu_calculadora_basica():
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma\n2. Resta\n3. Mult\n4. Div\n5. Potencia\n6. Volver")
    op = input("Opción: ")
    if op == "6": return
    n1, n2 = validar_numero("Num 1: "), validar_numero("Num 2: ")
    res = None
    if op == "1":
        res, n_op = sumar(n1, n2), "Suma"
    elif op == "2":
        res, n_op = restar(n1, n2), "Resta"
    elif op == "3":
        res, n_op = multiplicar(n1, n2), "Mult"
    elif op == "4":
        res, n_op = dividir(n1, n2), "Div"
    elif op == "5":
        res, n_op = potencia(n1, n2), "Potencia"

    if res is not None:
        print(f" ✅ Resultado: {res}")
        agregar_al_historial(n_op, n1, n2, res)
    else:
        print(" ❌ Error en la operación.")


def menu_conversor_unidades():
    print("\n--- CONVERSOR DE DATOS (Base 1000) ---")
    print("1. Bits a Bytes\n2. KB a MB\n3. MB a GB\n4. GB a MB\n5. MB a KB\n6. KB a Bytes\n7. Volver")
    op = input("Seleccione: ")
    if op == "7": return
    val = validar_numero("Cantidad: ")

    if op == "1":
        res, n_op = bits_a_bytes(val), "Bits a Bytes"
    elif op == "2":
        res, n_op = kilobytes_a_megabytes(val), "KB a MB"
    elif op == "3":
        res, n_op = megabytes_a_gigabytes(val), "MB a GB"
    elif op == "4":
        res, n_op = gigabytes_a_megabytes(val), "GB a MB"
    elif op == "5":
        res, n_op = megabytes_a_kilobytes(val), "MB a KB"
    elif op == "6":
        res, n_op = kilobytes_a_bytes(val), "KB a B"
    else:
        return

    print(f" ✅ Resultado: {res}")
    agregar_al_historial(n_op, val, "-", res)


def menu_sistemas_numericos():
    print("\n--- SISTEMAS NUMÉRICOS ---")
    print("1. Dec a Bin\n2. Dec a Hex\n3. Bin a Dec\n4. Volver")
    op = input("Seleccione: ")
    if op == "4": return
    if op in ["1", "2"]:
        n = validar_numero_entero("Número decimal: ")
        res = decimal_a_binario(n) if op == "1" else decimal_a_hexadecimal(n)
        print(f" ✅ Resultado: {res}")
        agregar_al_historial("Conversión", n, "-", res)
    elif op == "3":
        b = input(" Ingrese binario: ")
        res = binario_a_decimal(b)
        if res is not None:
            print(f" ✅ Resultado: {res}")
            agregar_al_historial("Bin a Dec", b, "-", res)
        else:
            print(" ❌ Binario no válido.")
# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    cargar_historial_archivo()
    while True:
        # Menú
        print(r"""
      ++ ____________________________________________++
      ||                                              ||
      ||   _____   _   _    ____   _ _     __         ||
      ||  | ____| | | | |  / ___| |  _  \ | |         ||
      ||  | |     | | | | |  _    | | | | | |         ||
      ||  | |___  | |_| | | |_| | | |_| | | |___      ||
      ||  |_____|  \___/   \____| |____/  |_____|     ||
      ||                                              ||
      ||               *Calculador multiusos *        ||
      ||               * te sirve pa'todo    *        ||
      ||                                              ||
      ++______________________________________________++
     """)

        print("1. Calculadora Básica\n2. Conversor de Datos\n3. Sistemas Numéricos\n4. Historial\n5. Borrar Historial \n6. Salir")
        opcion = input("\nOpción: ")
        if opcion == "1": menu_calculadora_basica()
        elif opcion == "2": menu_conversor_unidades()
        elif opcion == "3": menu_sistemas_numericos()
        elif opcion == "4": mostrar_historial()
        elif opcion == "5": borrar_historial()
        elif opcion == "6":
            guardar_historial_archivo()
            print("Chau!")
            break
        else:
            print(" error Opción no válida.")

if __name__ == "__main__":
    main()