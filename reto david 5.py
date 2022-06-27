import csv,json
import pandas

archivo=pandas.read_csv('C:/Users/user/Desktop/Mision tic/Programación I/Semana 7/JandJ.csv', header=0)
print(archivo)

with open('analisi_archivo.csv','w') as file:
    escritor=csv.writer(file,delimiter='\t')
    escritor.writerow(['fecha analizada','comportamiento de la accion','abs','diferencia Close-open'])
'''with open(r'analis_archivo.csv') as file2:
    print(file2.read())'''
tabla_2=pandas.read_csv('analisi_archivo.csv')
print(tabla_2)