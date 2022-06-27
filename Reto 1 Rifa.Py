
b=30
n=26
acumulador=0
numero= 0
while(numero!=n):
   numero=int(input("Ingrese un número entero: "))
   if(numero>=0 and numero>n and numero<=b):
      acumulador+=1                                  # este codigo lo desarrolle yo
      print("¡Ups! Te pasaste")
   elif (numero>=0 and numero<n and numero<=b):
      acumulador+=1
      print("¡Ups! Estás por debajo")
   elif (numero==n):
      acumulador+=1
      print(f"¡LO LOGRASTE! Usaste {acumulador} intentos") 
   else:
      print("¡Te saliste del intervalo!")

# codigos desarrollados por otros compañeros 
'''
b=30
n=26
acumulador=0
numero_ingresado= None
while(numero_ingresado!=n):
   numero_ingresado= int(input("Ingrese un numero entero: "))
   if(numero_ingresado>n and numero_ingresado<=b):             
      acumulador=acumulador+1
      print("¡Ups! Te pasaste")
   elif(numero_ingresado<n and numero_ingresado>=0):
      acumulador=acumulador+1
      print("¡Ups! Estás por debajo")
   elif(numero_ingresado==n):
      acumulador=acumulador+1
      print(f"¡LO LOGRASTE! Usaste {acumulador} intentos")   
   else:
      print("¡Te saliste del intervalo!")
  
n=15
b=30
x=0
acierto= False
while acierto!= True:
        
   num= int(input("Ingrese un número: "))
        
   if num> b or num< 0:
      x+= 1
      print("¡Te saliste del intervalo!")
       
   elif num<n:
      x+= 1
      print("¡Ups! Estás por debajo")
           
   elif num> n and num<b:
         x+= 1
         print("¡Ups! Te pasaste")
   else:
      acierto= True
      x+= 1
      print(f"¡LO LOGRASTE! Usaste {x} intentos")
      break
'''
'''
b=30
n=22

numero_intentos = 0
numero_ganador = False
while numero_ganador!= True:
     numero_intentos +=1
     numero_ingresado = int(input("Ingrese un número: "))

     if (numero_ingresado < 0 or numero_ingresado > b):
            print("¡Te salistes del intervalo!")
     if (numero_ingresado >= 0 and numero_ingresado <n):
            
            print("¡Ups! Estás por debajo")
     if (numero_ingresado >n and numero_ingresado <=b):
            
            print("¡Ups! Te pasastes")
     if (numero_ingresado == n):
            numero_ganador= True
            print(f"¡LO LOGRASTES! Usastes {numero_intentos} intentos")

b=30
n=13
ganador=False
cantidad_intentos=0
while ganador!=True:
       cantidad_intentos+=1
       numero=int(input("Ingrese un número: "))
       if numero<0 or numero>b:
          print("¡Te saliste del intervalo!")
          cantidad_intentos-=1
       elif numero>n and numero<=b:
          print("¡Ups! Te pasaste")
       elif numero<n and numero<=b:
            print("¡Ups! Estás por debajo")
       elif numero==n:
            ganador=True
            print(f"¡ LO LOGRASTE! Usaste {cantidad_intentos} intentos")

'''





