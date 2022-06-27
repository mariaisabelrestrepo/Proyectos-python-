'''
RETO 2 - FUNDAMENTOS DE PROGRAMACION


def modificar_materia(pensum, semestre, materia, nombre, creditos):

return mensaje


'''

pensum = [{'0123': {'nombre': 'intro a la ing', 'créditos': 2},'4567': {'nombre': 'inglés', 'créditos': 1}},{}, {}]
contador = int (0)

while (contador >=0):
    semestre = int (input('Digite el número del semestre que quiere modificar '))     
    
    if (semestre <=0 or semestre > len(pensum)):
        mensaje = ('Ingrese un semestre válido')
        print(mensaje)
    else:
        semestre-=1
        
        if(len(pensum[semestre]) == 0):
            mensaje = ('El semestre no tiene materias')
            break
        else:
            materia = input('Digite el código de la materia ') 

            if (materia not in pensum[semestre]):
                mensaje = 'La materia no existe'
                print()
                break 

            else:
                nombre = input ('Escriba el nombre de la materia ')
                creditos = int (input ('Digite la cantidad de créditos que llevara la nueva materia '))
                pensum[semestre][materia]['nombre']= nombre
                pensum[semestre][materia]['créditos']= creditos
                mensaje ='Modificada con éxito'
                break
print(pensum)
print(mensaje)
        
       