# Lista de valores
notas = [4, 8, 3, 10, 5, 7, 2, 9]

contador_aprobados = 0
contador_sobresalientes = 0

# FOR para recorrer la lista
for nota in notas:
    if nota < 5:
        print(f'{nota} es suspenso.')
    elif nota < 9:
        print(f'{nota} es aprobado.')
        contador_aprobados += 1             # Incrementa en la unidad el valor de la variable
    else:
        print(f'{nota} es sobresaliente')
        contador_sobresalientes += 1

# Fin del bucle - muestro resultados
print(f'Aprobados {contador_aprobados}')
print(f'Sobresalientes {contador_sobresalientes}')
