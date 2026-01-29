while True:
    try:
        # Código Propenso a Errores
        num1 = float(input("Introduce primer valor: "))
        num2 = float(input("Introduce segundo valor: "))
        operador = input("Introduce el operador (+, -, *, /): ")
        resultado = None
        # Calculo
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        elif operador=='x':
            print("Adios")
            break
        else:
            raise Exception("Operador no valido")
    except ValueError:
        # Maneja si el input no es convertible a número
        print("\n¡Error de Entrada! Debes ingresar valores numéricos válidos.")
    except ZeroDivisionError:
        # Maneja la división por cero
        print("\n¡Error Matemático! No se puede dividir un número por cero.")
    except Exception as e:
        print(e)
    else:
        # Se ejecuta solo si NO hubo errores
        print(f"\nOperación exitosa. El resultado es: {resultado}")