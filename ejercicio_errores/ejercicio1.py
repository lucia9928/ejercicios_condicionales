while True:
    try:
        tabla = int(input('Indica la tabla de multiplicar: '))
    except ValueError:
        print('El valor dado no es un numero')
    else:
        for numero in range(1,11):
            print(f'{tabla:2d} x {numero:2d} = {tabla*numero:2d}')
        break

print('FIN DE PROGRAMA')
