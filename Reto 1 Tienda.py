#soluciones sobre el reto de la tienda ciclo 1

'''seguir = "S"
total = 0
subtotal=0
while seguir == "S" or seguir == "s":
   valor = int(input("Ingrese el valor unitario: "))
   iva = str(input("¿El producto cuenta con IVA? S/N: "))
   cantidad = int(input("Ingrese la cantidad que lleva el cliente de el producto a registrar: "))
   if iva == "S":
      print ("IVA incluído")
      subtotal = valor*cantidad*1.19
      total = total + subtotal 
   if iva == "N":
      print ("PRODUCTO SIN IVA")
   subtotal = valor*cantidad
   print (f"SUBTOTAL: {subtotal}") 
   total = total + subtotal 
   seguir = input ("¿Faltan productos por cobrar? S/N: ").upper()
print(f"TOTAL A COBRAR: {subtotal}")'''

seguir = "S"
subtotal = 0
while seguir=="S":
   valor = int(input("Ingrese el valor unitario: "))
   iva = str(input("¿El pruducto cuenta con IVA? S/N: ")).upper ()
   cantidad = int(input("Ingrese la cantidad que lleva el cliente de el producto a registrar: "))
   if iva == "S":
      print ("IVA incluído")
      subtotal+= valor*cantidad*1.19
   else:
      print ("PRODUCTO SIN IVA")
      subtotal+=valor*cantidad
   print (f"SUBTOTAL: {subtotal}")
   seguir = input ("¿Faltan productos por cobrar? S/N: ").upper()
print(f"TOTAL A COBRAR: {subtotal}")
    