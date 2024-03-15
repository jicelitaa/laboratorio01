#autenticacion de usuario
def usuario():
    print("ingrese nombre del usuario")

# Definir el saldo inicial del cajero automático
saldo = 10000

# Función para mostrar el menú principal
def mostrar_menu():
    print("Bienvenido al Cajero Automático")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. transferencia")
    print("5. Salir")
#contraseña
def ingrese_nombre_del_usuario():
    print("INGRESE CONTRASEÑA")
    

# Función para mostrar el saldo actual
def ver_saldo():
    print(f"Su saldo actual es: ${saldo}")

# Función para retirar dinero
def retirar_dinero():
    global saldo
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= cantidad
        print(f"Retiraste ${cantidad}. Saldo restante: ${saldo}")

# Función para depositar dinero
def depositar_dinero():
    global saldo
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    print(f"Depositaste ${cantidad}. Saldo actual: ${saldo}")
# funcion para transeferencia
def transferencia():
    global saldo
    cantidad = float(input("Ingrese la cantidad a transferir: "))
    saldo += cantidad
    print(f"tranferir ${cantidad}. Saldo actual: ${saldo}")


# Loop principal del programa
while True:
    usuario()
    opcion = input("ingrese contraseña")
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ver_saldo()
    elif opcion == "2":
        retirar_dinero()
    elif opcion == "3":
        depositar_dinero()
    elif opcion == "4":
        transferencia()
    elif opcion == "5":
        print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

