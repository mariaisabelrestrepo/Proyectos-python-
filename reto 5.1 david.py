import csv, json
import pandas as pd 
def solucion ():

    df = pd.read_csv(r"C:\Users\user\Desktop\Mision tic\Programación I\Semana 7\JandJ.csv")
    print (df)
    fecha= df['Date']
    Volumen = df['Volume']
    resta = abs(df['Open']-df['Close'])
    aumento=[]
    for i in df.index:    
        if df.loc[i,'Close']-df.loc[i,'Open']>0:        
            aumento.append('SUBE')
        elif df.loc[i,'Close']-df.loc[i,'Open']<0:
            aumento.append('BAJA')
        else:
            aumento.append('ESTABLE')

    with open ('analisis_archivo.csv','w') as file:
        escritor = csv.writer(file, delimiter='\t')
        escritor.writerow(['Fecha analizada','Comportamiento de la accion', 'abs Diferencia Close-Open'])
        for i in range (len(fecha)):
            file.write("%s\t" %fecha[i])
            file.write("%s\t" %aumento[i])
            file.write("%s\n" %resta[i])
    #   "%s\n" % separa por saltos de linea
    '''
    with open (r'analisis_archivo.csv')as file2:
        print (file2.read())   
    '''
    tabla2 = pd.read_csv('analisis_archivo.csv')
    print (tabla2)
    diccionario = {}
    lowest_volume= int(Volumen.min())
    highest_volume=int( Volumen.max())
    mean_volume= float(Volumen.mean())
    greatest_difference=float( resta.max())

    for i in range (len(fecha)):
    
        if lowest_volume == Volumen [i]:
            diccionario ['date_lowest_volume'] =fecha[i]
            diccionario ['lowest_volume']= lowest_volume

        if highest_volume == Volumen [i]:
            diccionario ['date_highest_volume']=fecha[i]
            diccionario ['highest_volume'] = highest_volume      

        if greatest_difference == resta[i]:
            diccionario ['date_greatest_difference']= fecha[i]
            diccionario ['greatest_difference']= greatest_difference
        diccionario ['mean_volume'] = mean_volume   

    with open ('detalles.json','w') as jsonfile:
        json.dump(diccionario, jsonfile)
    lectura = pd.read_csv('detalles.json')
    print(lectura)
solucion()
    



