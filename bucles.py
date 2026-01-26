#bucle condicionado
#bucle que se ejecuta mientras se cumple una condicion
#ejemplo
clave="1234"
respuesta=input('indica la clave: ')
#comienza el bucle
while(respuesta != clave):
    #codigo dentro del bucle que se ejecuta mientras respuesta no es igual a la clave
    print('clave incorrecta')
    respuesta = input('indica la clave:')
    #finaliza el bucle
print('clave correcta, BIENVENIDO')

#----------------------------------------------------------------------------------------------------------
#ejemplo de cucle 1-N (que al menos se ejecuta una vez)
clave="1235"
respuesta=""

while respuesta != clave:
    respuesta=input('indica la clave:')
    #fin del bucle
print("ok")

#peligros los bucles inifinitos
a=10
while a >0:
    a +=1
    print(a)

print("FIN")
#BUCLE INFINITO MAS BREAK
while True: #bucle implicitamente infinito
    respuesta=input('quieres seguir: ').upper()
    if respuesta == 'N':
        print('BREAK!!!!')
        break #rotura incondicional del bucle
print("FIN")
#------------------------------------------------------
#ELSE
sumatorio = 0
numeros = 0
while(numeros < 5):
    valor=int(input('ingrese un numero: '))
    if valor>0:
        sumatorio=sumatorio+valor
        numeros=numeros+1
    else:
        print("fin")
        break
else:
#este codigo se ejecuta si el bucle termina con su condicion NO BREAK

    print(f'numeros: {numeros}')
    print(f'sumatorio: {sumatorio}')

print("fin")