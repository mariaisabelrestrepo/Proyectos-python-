import csv,json 
from csv import reader
import pandas
import numpy 
def solucion():
    # se lee el archivo tesla.csv con pandas datframe
    texto=pandas.read_csv("C:/Users/user/Desktop/Mision tic/Programación I/Semana 7/TESLA.csv",header=0)
    print(texto)
    #se extraen las columnas del dataframe anterior
    Open=texto['Open']
    close=texto['Close']
    high=texto['High']
    low=texto['Low']
    date=texto['Date']
    #se crean las listas para guardar los datos para el nuevo archivo
    comportamiento_accion=[]
    accion=[]
    resultado=0
    df=texto['Close']- texto['Adj Close']
    #se evalua el comportamiento de las acciones 
    for i in texto.index:
        if texto.loc[i,'Close']- texto.loc[i,'Open']>0:
            comportamiento_accion.append('SUBE')
        elif texto.loc[i,'Close']- texto.loc[i,'Open']<0:
            comportamiento_accion.append('BAJA')
        elif texto.loc[i,'Close']- texto.loc[i,'Open']==0:
            comportamiento_accion.append('ESTABLE')
        resultado=numpy.sqrt(df**2)
        accion=resultado
    # se crea el nuevo archivo 
    with open("analisis_archivo.csv", "w") as file:   
        file.write("Fecha\t")
        file.write("Comportamiento de la accion\t")   # se escriben los datos de cabecera 
        file.write("Ajuste Cuadratico de Close\n")

        dimension=len(comportamiento_accion)
        for j in range(dimension):
            file.write("%s\t" % date[j])  
            file.write("%s\t" % comportamiento_accion[j])   # se llevan los datos al nuevo archivo
            file.write("%s\n" % accion[j])
        file.close() 
    diccionario={} # diccionario para el archivo json 

    min_open= texto["Open"].min()
    max_close=texto["Close"].max()             # se calculan los maximos y minimos 
    promedio_volume=texto["Volume"].mean()
    f=[]
    for k in texto.index:
        f.append(abs(low[k]-high[k]))
    valor_absoluto=max(f)
    # se agregan los datos al diccionario
    for i in range(dimension):
        if Open[i]==min_open:
            diccionario['date_lowest_open']=date[i]
            diccionario['lowest_open']=min_open
        if close[i]==max_close:
            diccionario['date_highest_close']=date[i]
            diccionario['highest_close']=max_close
        diccionario['mean_volume']=promedio_volume
        if f[i]==valor_absoluto:
            diccionario['date_greatest_difference']=date[i]
            diccionario['greatest_difference']=valor_absoluto
            # se crea el archivo json
    with open("detalles.json", "w") as file:
        json.dump(diccionario, file)
    archivo_json=pandas.read_csv('detalles.json')
    print(archivo_json)                                    # se leen ambos archivos nuevos
    nuevo_archivo=pandas.read_csv('analisis_archivo.csv',sep= '\t')
    print(nuevo_archivo)
solucion()



