'''
crear una aplicacion que solicite dos nombres y dos edades, respectivamente
 acto seguido que nos indicque a continuacion lo siguiente,
 1.si ambas peronas son adultas,
 2. que nos indique si alguna persona es adulta
 3. la primera persona es mayor que la segunda
 4. indique el nombre de la persona que es mayor y si ambas tiene la misma edad que lo indique
 "ambas personas tienen la misma edad"
'''


titulo= 'CLASIFICACION DE MAYORES Y MENORES DE EDAD '
print(f'|{titulo:^80}| \n')
nombre1=input('Ingrese el nombre de la primera persona: ')
edad1=int(input('Ingrese la edad de la primera persona: '))
nombre2=input('Ingrese el nombre de la segunda persona: ')
edad2=int(input('Ingrese la edad de la segunda persona: '))

mensaje= 'ambas personas son mayores de edad' if edad1>=18 and edad2 >=18 else 'no, ambas personas no son adultas'
print(mensaje)

if edad1 >=18 or edad2>=18:
    print('uno de los usuarios es mayor de edad')


mensaje2= 'si , el usuario 1 es mayor al usuario 2'if edad1 > edad2 else 'no, el usuario 1 no es mayor que el usuario 2'
print(mensaje2)


if edad1 > edad2:
    print('el nombre de la persona mayor es : ', nombre1)
elif edad2 > edad1:
    print('el nombre de la persona mayor es : ', nombre2)
else:
    print('ambos usuarios tienen la misma edad')
