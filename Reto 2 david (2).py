pensum = [{'0123': {'nombre': 'intro a la ing', 'créditos': 2},
           '4567': {'nombre': 'inglés', 'créditos': 1}},{}, {},{}]

semestre = int (input('Digite el número del semestre que quiere modificar ')) 
nombre = input ('Escriba el nombre de la materia ')
materia = input('Digite el código de la materia ') 
creditos =  int (input ('Digite la cantidad de créditos que llevara la nueva materia ')) 

aux =0
def modificar_materia (pensum, semestre, materia, creditos):
    
    contenido_semestre = 0
    while True:
        if semestre > 0 and semestre <= len(pensum):
            aux = pensum[semestre -1]
        else:
            mensaje = "Ingrese un semestre válido"
            break
        if len(aux)==0:
            mensaje = "El semestre no tiene materias"
            break
        if materia not in aux:
            mensaje = "La materia no existe"
            break
        aux[materia]['nombre'] = nombre
        aux [materia]['créditos'] = creditos
        mensaje = "Modificado con éxito"
        break
    return mensaje

print(modificar_materia(pensum, semestre, materia, creditos))