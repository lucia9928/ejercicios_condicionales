# peticion de unidades
unidades = int(input('Indica el numero de unidades: '))
# peticion de precio unitario
precio = float(input('Indica el precio unitario: '))
# preguntar si es socio
respuesta = input('Indica si eres socio (s/n): ').upper()
socio = respuesta == "S" or respuesta == "SI"

# VALIDACIONES

# Comprobar si unidades esta mal
if unidades <= 0:                               # VALIDACION UNIDADES
    print('Las unidades son incorrectas')
elif precio <= 0.0:                             # VALIDACION PRECIO
    print('El precio es incorrecto')
else:                                           # esta OK
# Calculo del descuento
    if unidades < 5:
        tasa_descuento = 0.0
    elif 5 <= unidades <= 10:
        tasa_descuento = 15.0 if socio else 10.0
    else:
        tasa_descuento = 25.0 if socio else 20.0

    precio_bruto = precio * unidades
    descuento = precio_bruto * ( tasa_descuento / 100.0)
    precio_neto = precio_bruto - descuento

    # Calculado el descuento - muestro resultados
    print(f'Unidades adquiridas: {unidades}')
    print(f'Precio unitario: {precio:.2f} Euros')
    print(f'Descuento: {tasa_descuento:.2f} %')
    print('El usuario ' + 'es socio' if socio else 'no es socio')
    print(f'Precio bruto: {precio_bruto:.2f} Euros')
    print(f'Precio neto: {precio_neto:.2f} Euros')

print('FIN DE PROGRAMA')


