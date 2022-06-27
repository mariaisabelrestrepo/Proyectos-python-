

from operator import itemgetter

texto = ('Sucedió que un día el señor Zorro quiso dárselas de importante e invitó a comer a la señora Cigüeña. El menú no era otra cosa que un sopicaldo, una sopa con pocos sólidos que comer, la cual fue servida en un plato llano.Como es de esperarse, la señora Cigüeña no pudo comer debido a la forma y extensión de su pico, en cuanto que el señor Zorro, con su lengua, lamió todo el plato a gusto.Ofendida, la señora Cigüeña decidió desquitarse por la humillación del señor Zorro, y para ello, lo convidó a comer a su casa. El señor Zorro dijo:—¡Enhorabuena! Para los amigos siempre tengo tiempo. la hora de la cita, el señor Zorro se presentó en casa de la señora Cigüeña, hizo todas las reverencias del caso y se sentó a la mesa, donde encontró la comida servida. La señora Cigüeña había preparado un sabroso guisado, servido en un recipiente de cuello largo y embocadura muy angosta, por donde solo ella podía pasar su pico, mientras que el señor Zorro no podía introducir su hocico. Así, el señor Zorro, el mismo que se daba ínfulas de importante, tuvo que \nregresar a casa humillado, con las orejas gachas, el rabo entre las piernas y, claro, el estómago vacío. Moraleja: no hagas a los demás lo que no quieres que te hagan a ti.')
lista = texto.split()

def extraer(lista):
    caracteres=['-','¿','?','.',',','!','¡',':','"',';','_']
    lista=' '.join(lista)
    lista=lista.lower()
    for caracter in caracteres:
        lista=lista.replace(caracter," ")
    lista=lista.split()
    print(lista)
    return lista
def contar(lista):
    frecuentes={}
    for palabra in lista:
        if palabra!=' ':
            frecuentes[palabra]= lista.count(palabra)
            lista_frecuentes=sorted(frecuentes.items(),key=itemgetter(1),reverse=True)
    print(lista_frecuentes)
    ordenada=[]
    for i in range(len(lista_frecuentes)):
          ordenada.append(list(lista_frecuentes[i]))
    lista_texto=[]
    for i in range(20):
        lista_texto.append(ordenada[i])
    print(lista_texto)
    return lista_texto
def main(lista_texto) :
    lista=extraer(lista_texto)
    lista_conteo=contar(lista)
    return lista_conteo
main(lista)

'''lista_texto = [element.lower() for element in lista_texto]
print(lista_texto)
lista_texto = [y.strip('-¿?.,¡!:"–') for y in lista_texto]
print(lista_texto)
counts ={}
list1 = []
for x in lista_texto:
    if x in counts and x != '':
        counts[x] +=1
    else:
        counts[x] = 1
print('hola',counts)
mayor = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print(mayor)
list2 = []
cont = 0

for i in mayor:
    cont += 1
    if cont <= 20 :
        list2.append(list(i))
    else:
        break
print(list2) '''

