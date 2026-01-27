'''
1.- Crea una aplicación que solicite al usuario un valor y muestre su tabla de multiplicar de
manera formateada
'''
for numero in range(1,11):
    print(f" 5 x {numero} = {numero*5}")

'''
2.- Modifica el ejercicio anterior para que muestre una tabla con los valores de las tablas de 
multiplicar del 1 al 10 del siguiente modo:
'''
for numero2 in range(1, 11):
    for numero in range(1,11):
        print(numero, end="\t")
    print(numero2,f' {numero2*numero}')

