
from operator import itemgetter

texto = ('Sucedió que un día el señor Zorro quiso dárselas de importante e invitó a comer a la señora Cigüeña. El menú no era otra cosa que un sopicaldo, una sopa con pocos sólidos que comer, la cual fue servida en un plato llano.Como es de esperarse, la señora Cigüeña no pudo comer debido a la forma y extensión de su pico, en cuanto que el señor Zorro, con su lengua, lamió todo el plato a gusto.Ofendida, la señora Cigüeña decidió desquitarse por la humillación del señor Zorro, y para ello, lo convidó a comer a su casa. El señor Zorro dijo:—¡Enhorabuena! Para los amigos siempre tengo tiempo. la hora de la cita, el señor Zorro se presentó en casa de la señora Cigüeña, hizo todas las reverencias del caso y se sentó a la mesa, donde encontró la comida servida. La señora Cigüeña había preparado un sabroso guisado, servido en un recipiente de cuello largo y embocadura muy angosta, por donde solo ella podía pasar su pico, mientras que el señor Zorro no podía introducir su hocico. Así, el señor Zorro, el mismo que se daba ínfulas de importante, tuvo que \nregresar a casa humillado, con las orejas gachas, el rabo entre las piernas y, claro, el estómago vacío. Moraleja: no hagas a los demás lo que no quieres que te hagan a ti.')

lista_texto = texto.split()

def eliminar_simbolos(lista_texto):
      
    lista_texto =" ".join(lista_texto)

    lista_texto= lista_texto.replace('-','')
    lista_texto= lista_texto.replace('¿','')
    lista_texto= lista_texto.replace('?','')
    lista_texto= lista_texto.replace('.','')
    lista_texto= lista_texto.replace(',','')
    lista_texto= lista_texto.replace('¡','')
    lista_texto= lista_texto.replace('!','')
    lista_texto= lista_texto.replace(':','')
    lista_texto= lista_texto.replace('"','')
    lista_texto= lista_texto.replace('—','')

    lista_texto = lista_texto.lower()
    lista_texto = lista_texto.split()
    lista_unicos= list(set(lista_texto)) 
    lista= lista_unicos  
    
    return (lista_texto, lista)

def cont_palabras(lista_texto, lista):
             
    validacionrep = []

    for i in range (len(lista)):
        cont = lista_texto.count(lista[i])
        item = lista[i], cont
        validacionrep.append(list(item))
        validacionrep.sort(key=itemgetter(1),reverse= True)
        listaprimeros=[]

    for i in range (20):
        listaprimeros.append(validacionrep[i])
    return (listaprimeros)


def  main(lista_texto):
    lista_borrado, lista_unica= eliminar_simbolos(lista_texto)
    lista_conteo= cont_palabras(lista_borrado, lista_unica )
    return (lista_conteo)

print (main(lista_texto))




