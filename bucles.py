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

#BUCLE FOR -------------------------------------------------------------
''' 
1- EJECUTAR el codigo un determinado numero de veces conocido
2- recorrer una secuencia de valores 
'''

for numero in range(3):
    print("hola")

#FOR PARA RECORRER UNA SECUENCIA DE VALORES
#range -> un argumento te genera valores de 0 a n -1 =range(n)
for numero in range(10):
    print(f" 7 x {numero} = {numero*7}")


#range(a,b) genera una secuencia de a incluido a b excluido
for numero in range(100,201):
    print(numero)

#range(a,b, paso)
for numero in range(1,10,2):
    print(numero)

lista=[10,2,4,55,8,70,10,15] #lista
for numero in lista:
    print(numero)

texto="HOLAAAAAAA!!!!!"
for letra in texto:
    print(letra)