proteina = float (30.5)
carbohidratos = float (60.1)
verduras = float (-24.4)
estado = "" # variable
clase = ""
dias=0
desnutricion_A = float ((carbohidratos*2) + proteina + (verduras*2))/1000
Sobrepeso_B = float ((carbohidratos * 0.6) + proteina +(verduras*4))/1000
peso_saludable_C = float ((carbohidratos * 0.5) + (proteina * 0.7) +(verduras*2))/1000
edad = int(input('Indicar la edad del paciente: '))
peso = float (input ('Indicar el peso del paciente en kilogramos: '))
if(edad >=5 and edad <=10):
    #Bien
    if(peso < 16.0 ):
        estado = "desnutrición"
        clase = "A"
        dias = ((peso - 22.0)//desnutricion_A)
        if(dias<0):
            dias= dias*-1
    elif(peso >=16.0 and peso <=28.0):
        estado = "peso saludable"
        clase = "C"
        dias = ((peso - 28.0)//peso_saludable_C)
        if(dias<0):
            dias= dias*-1
    else:
        estado = "sobrepeso"
        clase = "B"
        dias = ((peso - 24.0)//Sobrepeso_B)
        if(dias<0):
            dias= dias*-1 
elif(edad >10 and edad <=13):
    #Bien
    if(peso < 30.0 ):
        estado = "desnutrición"
        clase = "A"
        dias = ((peso - 32.0)//desnutricion_A)
        if(dias<0):
            dias= dias*-1 
    elif(peso >=30.0 and peso <=50.0):
        estado = "peso saludable"
        clase = "C"
        dias = ((peso - 50.0)//peso_saludable_C)
        if(dias<0):
            dias= dias*-1 
    else:
        estado = "sobrepeso"
        clase = "B"
        dias = ((peso - 43.0)//Sobrepeso_B)
        if(dias<0):
            dias= dias*-1
elif(edad > 13 and edad <=17):
    if(peso < 51.0 ):
        estado = "desnutrición" 
        clase = "A"
        dias = ((peso - 56.0)//desnutricion_A)
        
        if(dias<0):
            dias= dias*-1         
    elif(peso >=51.0 and peso <=63.0):
        estado = "peso saludable"
        clase = "C"
        dias = ((peso - 63.0)//peso_saludable_C)
        
        if(dias<0):
            dias= dias*-1
    else:
        estado = "sobrepeso"
        clase = "B"
        dias = ((peso - 58.0)//Sobrepeso_B)
        
        if(dias<0):
            dias= dias*-1         
if (clase == "A" or clase == "B"):
    print(f'El estado nutricional del paciente es {clase} y se requieren {int(dias)} días de dieta para que alcance un peso saludable')
else:
    print(f'El estado nutricional del paciente es {clase} y se requieren {int(dias)} días de dieta para que alcance el peso máximo')