import csv, json, pandas,numpy

#amazon=open("AMAZON.csv")
#lectura=csv.reader(amazon)

amazon=pandas.read_csv(r"AMAZON.csv", header=0) 
print(amazon)

Date= amazon["Date"]
acciones=[]
raiz_cuadrada=numpy.sqrt((amazon["Close"]-amazon["High"])**2)
print(raiz_cuadrada)

for posicion in amazon.index:
  if amazon.loc[posicion,"Close"]-amazon.loc[posicion,"Open"]>0:
    acciones.append("SUBE")
  elif amazon.loc[posicion,"Close"]-amazon.loc[posicion,"Open"]<0:
    acciones.append("BAJA")
  elif amazon.loc[posicion,"Close"]- amazon.loc[posicion,"Open"]==0:
    acciones.append("ESTABLE")
print(acciones)

with open("analisis_archivo.csv", "w") as archivo:
  archivo.write("Fecha ")
  archivo.write("Comportamiento_de_la_accion ")
  archivo.write("Diferencia_absoluta_open-high\n") 
  
  for posicion in range (len(Date)):
    archivo.write("%s\t" % Date[posicion])
    archivo.write("%s\t" % acciones[posicion])
    archivo.write("%s\n" % raiz_cuadrada[posicion])

archivo_json={}
Volume=amazon["Volume"]
min_volume=int(Volume.min())
promedio_volume= float(Volume.mean()) 
minimo_diferencia=float(raiz_cuadrada.min())
maximo_diferencia=float(raiz_cuadrada.max()) 

for posicion in range(len(Date)):
  if min_volume==Volume[posicion]:
    archivo_json["date_lowest_volume"]=Date[posicion]
    archivo_json["lowest_volume"]= min_volume

  archivo_json["mean_volume"]=promedio_volume

  if minimo_diferencia== raiz_cuadrada[posicion]:
    archivo_json["date_smallest_difference"]=Date[posicion]
    archivo_json["smallest_difference"]=minimo_diferencia
  
  if maximo_diferencia==raiz_cuadrada[posicion]:
    archivo_json["date_greatest_difference"]= Date[posicion]
    archivo_json["greatest_difference"]=maximo_diferencia

with open("detalles.json","w") as file:
  json.dump(archivo_json,file)


  

 




