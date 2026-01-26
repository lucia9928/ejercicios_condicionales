# Peticion unidades
unidades = int(input("Indica el numero de unidades: "))
# Peticion precio
precio_unitario = float(input("Indica el precio unitario: "))
# Peticion socio?
respuesta = input("Eres socio? (s/n): ").upper()
socio = respuesta == "S"

# Validaciones
ok_unidades = unidades > 0
ok_precio = precio_unitario > 0.0

if not ok_unidades:
    # MAL UNIDADES
    print("Unidades no validas")
    exit()                          # La aplicacion termina aqui

if not ok_precio:
    # MAL PRECIO
    print("Precio no valida")
    exit()                          # La aplicacion termina aqui

# Cálculo del descuento
if unidades < 5:
    tasa_descuento = 0.0
elif 5 <= unidades <= 10:
    tasa_descuento = 15.0 if socio else 10.0
else:
    tasa_descuento = 25.0 if socio else 20.0

# Calculo importe bruto
importe_bruto = unidades * precio_unitario
# Calculo del descuento
descuento = importe_bruto * ( tasa_descuento / 100.0)
# Calculo del importe neto
importe_neto = importe_bruto - descuento

# Visualizacion de resultados
print(f"Unidades {unidades} Unidades.")
print(f"Precio {precio_unitario:.2f} Euros")
print("El usuario " + "es socio" if socio else "no es socio")
print(f'El importe bruto es {importe_bruto:.2f} Euros')
print(f"El descuento es {tasa_descuento}%")
print(f"El importe final es {importe_neto:.2f} Euros")

pago = float(input("Ingrese el pago: "))
if pago > importe_neto:
    devolucion = pago - importe_neto
    print(f'Devolucion {devolucion:.2f} Euros')
elif pago < importe_neto:
    faltante = importe_neto - pago
    print(f'Pago insuficiente. Faltan {faltante:.2f} Euros ')
else:
    print('Importe exacto')

print('FIN')