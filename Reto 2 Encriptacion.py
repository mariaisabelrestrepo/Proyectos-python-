'''from string  import ascii_uppercase as alfabeto
mensaje= 'The Starry Night'
valueslist=[]
clave={}
listm=list(mensaje)
lista1= list(alfabeto)
clave=dict(zip(listm,lista1))
for letter in listm:
    valueslist.append(clave[letter])
encriptado="".join(valueslist)
print(encriptado)
print(clave)

#desencriptador
valuelist2=[]
encriptadolist=list(encriptado) #eliminar lista
claveitems=clave.items()
claveinv={v:k for k, v in clave.items()}

for letter in encriptadolist:# modificar a encriptado
    valuelist2.append(claveinv[letter])
desencriptado="".join(valuelist2)
print (desencriptado)
'''
'''from string  import ascii_uppercase as alfabeto
mensaje= 'The Garden of Earthly Delights'

listm=list(mensaje)
listm= set(listm)
print(listm)
valueslist={}
encriptado=""
global clave
clave=dict(zip(listm,alfabeto))
for letter in listm:
    valueslist[letter]=clave[letter]
for letra in mensaje:
    encriptado+=clave[letra]

print(encriptado)
print(clave)

#desencriptador
valuelist2=[]
claveitems=clave.items()
claveinv={v:k for k, v in clave.items()}

for letter in encriptado:
    valuelist2.append(claveinv[letter])
desencriptado="".join(valuelist2)
print (desencriptado)'''

import numpy as np
import random

texto='Today is Caturday!'
dimension=np.sqrt(len(texto))
if dimension%1!=0:
   dimension=round(dimension)+1
print(dimension)
dimension= int (dimension)
for i in range (len(texto),dimension**2):
    texto+="_"
texto=list(texto) 
print (texto)
clave=[]
for i in range(len(texto)):
    clave.append(i)
random.shuffle(clave)
encriptacion=[]
for i in clave:
    encriptacion.append(ord(texto[i]))
array_encriptado=np.array(encriptacion).reshape(dimension,dimension)

print(array_encriptado)
print(clave)
#desencriptacion
matriz_encriptado=array_encriptado.ravel().tolist() 
print(matriz_encriptado)
desencriptacion=[]
for i in range(len(matriz_encriptado)):
    posicion=clave.index(i)
    desencriptacion.append(chr(matriz_encriptado[posicion]))
    texto="".join(desencriptacion)
    texto= texto.replace("_","")
print(texto)
