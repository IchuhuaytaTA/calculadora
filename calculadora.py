def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division por cero."
print("\t BIENVENIDO A LA CALCULADORA BASICA.")
print("Presione un numero.")
print("1 = SUMA")
print("2 = RESTA")
print("3 = MULTIPLICACION")
print("4 = DIVISION")
print("5 = exit")

while True:
    try:
        opcion = int(input("Ingrese la operación: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        continue

    if opcion == 5:
        print("Chao!")
        break

    elif opcion in [1, 2, 3, 4]:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Solo se permiten números.")
            continue

        if opcion == 1:
            print("Resultado:", suma(num1, num2))
        elif opcion == 2:
            print("Resultado:", resta(num1, num2))
        elif opcion == 3:
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == 4:
            print("Resultado:", division(num1, num2))

    else:
        print("Opción inválida. Intente de nuevo.")
