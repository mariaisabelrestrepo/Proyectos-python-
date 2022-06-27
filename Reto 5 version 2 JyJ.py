from numpy import gradient
import pandas as pd 
import csv
import json

df = pd.read_csv(r"C:\Users\user\Desktop\Mision tic\Programación I\Semana 7\Retos 5\JandJ.csv")


fecha_analizada = df['Date']
apertura = df['Open']
cierre = df['Close'] 

aumento=[]
for i in df.index:

    if df.loc[i,'Close']-df.loc[i,'Open']>0:
        aumento.append('SUBE')
    elif df.loc[i,'Close']-df.loc[i,'Open']<0:
        aumento.append('BAJA')
    else:
        aumento.append('ESTABLE')

valor_absoluto=[]

for i in range (len(fecha_analizada)):
    resta =abs(df.loc[i,'Close'] - df.loc[i,'Open'])
    valor_absoluto.append(resta)


with open ('analisis_archivo.csv','w') as file:
    escritor = csv.writer(file,delimiter= '\t')
    escritor.writerow(['fecha analizada', 'Comportamiento de la accion', 'abs Diferencia Close-Open'])
    for i in range(len(fecha_analizada)):   
        lista = [df.loc[1,'Date'],aumento[i],valor_absoluto[i]]
        escritor.writerow(lista)
      

with open ('analisis_archivo.csv', 'r') as file:
    print(file.read())

tabla2= pd.read_csv('analisis_archivo.csv')


lowest_volume = int(df['Volume'].min())
highest_volume = int(df['Volume'].max())
mean_volume = float( df['Volume'].mean())
greatest_difference = float(resta.max())

diccionario = {}
for i in range (len(fecha_analizada)):
    
    if lowest_volume == df['Volume'].min():
        diccionario ['date_lowest_volume']= str(df.loc[i,'Date'])
        diccionario ['lowest_volume']= lowest_volume
    if highest_volume == df['Volume'].max():
        diccionario ['date_highest_volume']= df.loc[i,'Date']
        diccionario ['highest_volume']= highest_volume    
    if greatest_difference == resta:
        diccionario ['date_greatest_diference']= df.loc[i,'Date']
        diccionario['greatest_diference']= greatest_difference
    
    diccionario ['mean_volume']= mean_volume

print (diccionario)


with open ('detalles.json', 'w') as docfinal:
    json.dump(diccionario, docfinal)

with open ('detalles.json','r') as final:
    lector = json.load(final)
  

