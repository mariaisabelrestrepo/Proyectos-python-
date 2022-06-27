'''
datos=[]
falta= " "
ingreso= True
beneficiarios_can_fel={}
can_fel=[]
beneficiarios_equ_bov={}
equ_bov=[]
promedio_can_fel=None
promedio_equi_bov=None
acumC=0
acumE=0
contadorC=0
contadorE=0
while ingreso:

    nombres= str(input("Ingrese el nombre de su mascota: "))
    tipos=str(input("Ingrese el tipo de especie: "))
    edades=int(input("Ingrese la edad del animal: "))
    pesos=float(input("Ingrese el peso del animal: "))

    diccionario={'1':nombres,'2':tipos,'3':edades,'4':pesos}
    datos.append(diccionario)
    if tipos=='canino'and edades>=9 or tipos=='felino'and edades>=9:
       beneficiarios_can_fel= {'1':nombres,'2':tipos, '3': pesos}
       can_fel.append(beneficiarios_can_fel)
       contadorC+=1
       acumC+=edades

    if tipos=='equino'and edades>=16 or tipos=='bovino'and edades>=16:
       beneficiarios_equ_bov= {'1':nombres,'2':tipos, '3': pesos}
       equ_bov.append(beneficiarios_equ_bov)
       contadorE+=1
       acumE+=edades
       
    falta=(input("desea ingresar un nuevo animal:")).upper()
    if falta== 'N':
    
        print(datos)
        print(can_fel)
        print(equ_bov)
        if contadorC>1: 
           promedio_can_fel=acumC/contadorC
           print(promedio_can_fel)
        if contadorE>1: 
           promedio_equi_bov=acumE/contadorE
           print(promedio_equi_bov)
        
        ingreso==False
        break
'''

diccionario={}
listaC=[]
listaE=[]
falta= " "
beneficiarios_can_fel={}
beneficiarios_equ_bov={}
promedio_can_fel=None
promedio_equi_bov=None
acumC=0
acumE=0
contadorC=0
contadorE=0
while True:
   clave=str(input("ingrese la clave: "))
   nombres= str(input("Ingrese el nombre de su mascota: "))
   tipos=str(input("Ingrese el tipo de especie: "))
   edades=int(input("Ingrese la edad del animal: "))
   pesos=float(input("Ingrese el peso del animal: "))

   diccionario[clave]=[nombres, tipos,edades, pesos]

   if tipos=='canino'and edades>=9 or tipos=='felino'and edades>=9:
      beneficiarios_can_fel[clave]=[nombres,tipos,pesos] 
      contadorC+=1
      acumC+=edades
   if tipos=='equino'and edades>=16 or tipos=='bovino'and edades>=16:
      beneficiarios_equ_bov[clave]=[nombres,tipos,pesos] 
      contadorE+=1
      acumE+=edades

   falta=(input("desea ingresar un nuevo animal:")).upper()
   if falta== 'N':

      print(diccionario) 
      print(beneficiarios_can_fel)
      print(beneficiarios_equ_bov)
      if contadorC>1: 
         promedio_can_fel=acumC/contadorC
         print(promedio_can_fel)
      if contadorE>1: 
         promedio_equi_bov=acumE/contadorE
         print(promedio_equi_bov)       
       
      break     
   else:
      True
   

   
   

