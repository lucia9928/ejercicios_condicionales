#ejecucion de secuencia

a=1
b=1
r= a+b

a=10
b=20
print(r)

#CONDICIONALES
#Condicional de una rama

nombre= "maria"
if nombre=='maria':
    #codigo contenido en el if (se ejecuta solo si la condicion es cierta
    print ('hola maria')
    print('te conozco')

#codigo fuera del if8se ejecuta independientemente de la condicion)
print('fin del programa')
#condicionales de dos ramas

if nombre=='maria ':

    print ('hola maria')
    print('te conozco')
else:
    print('no te conozco')
    print('no se quien eres ')

print('Adios')

#anidamientos
#en la parte VERDAD
temperatura=120
if temperatura < 0:
    print('no es hiejo')
else:
    if temperatura<100:
        print('agua liquida')
    else:
        print('vapor')
if temperatura <0 and temperatura>100:
    print('agua liquida')
print('ADIOS')

#tambien se puede  anidar en la parte falsa
if temperatura <100:
    print('LIQUIDA')
else:
    print('VAPOR')

if temperatura <0:
    print('LIQUIDA')
else:
    print('VAPOR')
#CONDICIONALES EN SERIE
if temperatura <=0:
    print('no es hiejo')
#if temperatura >0 and temperatura<100:
if 0 <= temperatura <=100:
    print('agua liquida')
if temperatura >= 100:
    print('vapor')

#anidamiento en la parte falsa empleando elif
if temperatura < 0:
    print('no es hiejo')
elif temperatura<100:
    print('agua liquida')
else:
    print('vapor')

#EXPRESION CONDICIONAL TERNARIA

edad=20
if edad> 18:
    mensaje='eres adulto'
else:
    mensaje='eres menor'
print(mensaje)

mensaje='eres adulto' if edad >=18 else "eres menor"
print(mensaje)