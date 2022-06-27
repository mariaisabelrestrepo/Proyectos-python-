
from re import L

'''
lista= [1,2,3,4,5,6]
lista1=[7,8,9,10]

# agregar datos a la lista
lista.append("final")
# cambiar datos de la lista
lista[0]=0
print(lista)
#quitar datos de la lista o la lista completa 
#del lista[4]
# eliminar dato en especifico cuando no se conoce la posicion 
#lista.remove(4)
# elimina dato o por posicion y tambien retorna valor eliminado
x=lista.pop(2)
print (lista)
print ('el valor eliminado es: ',x)
#concatenacion de listas 
# opcion 1 lista=[]* numero de repeticiones
#opcion 2
print(lista)
lista*=5
print (lista)
#unir listas
print(lista+lista1)
print(lista1+lista)

#crear listas a traves de for
l=[]
for i in range(1,11):
    l.append(i) # agregar datos a la lista
    print(len(l)) # conocer tamaño de la lista
for i in range(len(l)): # imprimir lista con tamaño de la lista anterior
    print (i, end= ' ')

    #imprimir cuadrado de datos 
l=[]
for i in range(1,11):
    l.append(i**2) # agregar datos a la lista
    print(len(l)) # conocer tamaño de la lista
for i in range(len(l)): # imprimir lista con tamaño de la lista anterior
    print (l[i]**2, end= ' ')

    #otro metodo para recorrer listas
l=[]
for i in range(1,11):
    l.append(i**2) # agregar datos a la lista
    print(len(l)) # conocer tamaño de la lista
for i in l: # imprimir lista con tamaño de la lista anterior
    print (i,i**2,i**3)

#multilistas
l=[[1,2,3],[4,5,6],[7,8,9]]

for i in l:
    for j in i:
        print(j)

#indexado negativo
l=[1,2,4,6,8,9,12,34,57,89,]#lista original
print(l[-1]) #se imprime lista mostrado datos en el -1
l.pop()#se elimina ultimo dato
print(l[-1]) #se imprime ultimo dato actualizado

#slicing
lista=[1,2,3,4,6,7,8,9,10]
lista1=lista [1:5:2]+ lista[1:7:2]
print(lista1)
#TUPLAS
tupla= (1,3,4,5,6,7,[1,2,3,4,5,6])
# para agregar datos a una lista dentro de una tupla
tupla[-1][1]=5
print(tupla)
#crear un alista a partir de una tupla
lista=list(tupla)
#recorrido de tuplas
tupla=(2,4,5,6,7,8,9,3)
for i in range(len(tupla)):
    print(tupla[i])
for i in tupla:
    print (i)
)
#conjuntos
conjunto= set() # para conjunto vacio 
conjunto={1,4,5,6,7}
conjunto.add(8) # agregar datos manualmente al conjunto
conjunto.update([2,3,5,6,9,0]) # para agregar multiples datos 
conjunto.update([(1,2,3,45,6,72,7)])# para añadir una tupla a un conjunto
conjunto.remove(1)# eliminar datos dentro de un conjunto
conjunto.discard(15)
#remover diferentes posiciones en el conjunto
for i in [1,2,3]:
    conjunto.remove(i)
'''    
#DICCIONARIOS
