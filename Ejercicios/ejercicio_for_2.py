
# Bucle principal dibuja 10 filas
for t in range(1, 11):
    # Bucle anidado - dibuja una fila con 10 valores
    for v in range(1, 11):
        resultado = v * t
        print(f'{resultado:10d}', end='')           # print con justificacion a la derecha + 10 espacios
        #print( t * v, end='\t')                    # print con tabulador

    # salto de carro que separa cada una de las filas
    print()




