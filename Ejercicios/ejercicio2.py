titulo= 'BIENVENIDO AL PROGRAMA DE COMPRA '
print(f'|{titulo:^80}| \n')

num_uni= int(input('Ingresa el numero de productos que estas comprando'))
precio= float(input('Ingrese el precio del producto'))
tiene_tarjeta=input('¿Tiene tarjeta de fidelidad?')
precio_total= precio * num_uni
descuento=0
precio_desc=precio_total


if num_uni<= 0:
    print("Unidade no validas")
if precio<=0:
    print("Precio no valido")
if num_uni<5:
    print("Sin descuento")
elif num_uni >=5 and num_uni<=10:
    if tiene_tarjeta == 'si':
        descuento= (precio_total *15)/100
        precio_desc= precio_total - descuento
    else:
        descuento= (precio_total *10)/100
        precio_desc= precio_total - descuento
elif num_uni >10:
    if tiene_tarjeta == 'si':
        descuento= (precio_total *25)/100
        precio_desc= precio_total - descuento
    else:
        descuento= (precio_total *20)/100
        precio_desc= precio_total - descuento

print(f'El numero de unidades adquiridas es: {num_uni}')
print(f'El precio unitario por unidad es: { precio}')
print(f'el usuario tiene tarjeta de fidelidad: {tiene_tarjeta}')
print(f' el importe bruto es: { precio_total:.2f}')
print(f'El descuento aplicado es: {descuento:.2f}')
print(f'El importe final de la compra es: { precio_desc}')

pago=int(input('Ingrese la cantidad con la que desea pagar: '))
if pago > precio_desc:
    devolucion=pago-precio_desc
    print(f'devolucion {devolucion:.2f}')
elif pago< precio_desc:
    falta=precio_desc-pago
    print(f'pago insuficiente, falta a pagar {falta:.2f}')
else:
    print(f'importe exacto')



