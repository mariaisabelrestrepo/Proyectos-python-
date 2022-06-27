print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre_estudiante = input('Ingrese su nombre :')
nombre_materia = input('Ingrese el nombre de la materia :')   #se solicitan datos 
boleano=True
prom_acu = 0
nota_acu = 0             
nota_acu_red =0
nueva_notas = ""
while boleano :
    n1=float(input("Ingrese la nota obtenida :"))
    porcentaje_n1=float(input("Ingrese el porcentaje de la nota :"))
    prom_acu = prom_acu + porcentaje_n1
    if prom_acu > 100 :
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        prom_acu = prom_acu - porcentaje_n1
    else:
        if prom_acu <= 100 :
            nota_acu = nota_acu + n1 * porcentaje_n1
        if prom_acu < 100 :
            nueva_notas = input("¿Falta añadir notas? S/N ")
        if nueva_notas == "N" or nueva_notas== 'n' or prom_acu == 100 : 
            boleano = False
            break
            
nota_acu = nota_acu / 100
nota_acu_red = round(nota_acu, 2) # se redondea la nota acumulada

# se utiliza format para agregar los datos al print        
if  nota_acu_red > 3.0:
    print(f"El estudiante {nombre_estudiante} cursó la materia {nombre_materia} y obtuvo {nota_acu_red } resultando en aprobado" )
else:
    print(f"El estudiante {nombre_estudiante} cursó la materia {nombre_materia} y obtuvo {nota_acu_red } resultando en desaprobado" )
        
porcentaje_notas = 0
sumat_porcentajes = 0
faltan_notas = "S"
nota_acumulada = float(0)
print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre = input("Por favor ingrese su nombre: ").capitalize() #capitalize se utiliza para poner la primera letra en mayuscula
materia = input("Ingrese el nombre de la materia: ").capitalize()
while faltan_notas == "S" and sumat_porcentajes<100:
    nota = float(input("Ingrese la nota obtenida: "))
    porcentaje_nota = int(input("Ingrese el porcentaje de la nota: "))
    sumat_porcentajes += porcentaje_nota
    if sumat_porcentajes > 100:
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        sumat_porcentajes -= porcentaje_nota
    else: 
        if sumat_porcentajes<=100:
            nota_acumulada += nota*porcentaje_nota
        if (sumat_porcentajes < 100):                   # Upper se utiliza para convertir todo a mayuscula 
            faltan_notas= input("¿Falta añadir notas? S/N ").upper() #hasta aquí va el bucle infinito, siempre lleva a agregar nota y porcentaje nota
        if faltan_notas== "N" or sumat_porcentajes==100:
            break
nota_acumulada/=100  
if(nota_acumulada >= 3.0):
    print(f"El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada:.2f} resultando en aprobado")
else:                           # :.2f se utiliza para darle longitud y ancho a la cadena float, total de decimales  
    print(f"El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada:.2f} resultando en reprobado")


print ("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
Nombre = input ("Por favor ingrese su nombre: ")
Materia= input ("Ingrese el nombre de la materia: ")
BucleNota= True
ContadorProm=0
AcumNota=float(0)
Pregunta= 'S'
while(BucleNota):

    Nota= float(input("Ingrese la nota obtenida "))
    Porcentaje=int(input("Ingrese el porcentaje de la nota "))
    ContadorProm+=Porcentaje
    if(ContadorProm>100):
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        ContadorProm-=Porcentaje
    else:
        if(ContadorProm<=100):
            AcumNota=Nota*Porcentaje+AcumNota
        if(ContadorProm<100):
            Pregunta= input("Desea ingresar otra nota? S/N ").upper()
        if ContadorProm==100 or Pregunta=='N':
           break
if(AcumNota>=3):
    print(f"El estudiante {Nombre.capitalize()} cursó la materia {Materia.capitalize()} y obtuvo {pon} resultando en aprobado ")
else:
    print(f"El estudiante {Nombre.capitalize()} cursó la materia {Materia.capitalize()} y obtuvo {pon} resultando en desaprobado ")
