import numpy as np
datos=["2009-09-30", 18.0, 28.7, 310, 17, 13, 0, "2009-10-30", 16.6, 26.8, 326, 15, 15, 0,"2009-11-29", 17.3, 26.8, 409, 14, 16, 0, "2009-12-29", 17.3, 27.6, 339, 13, 16, 1, "2010-01-28", 17.1, 25.5, 345, 14, 16, 0, "2010-02-27", 16.8, 25.8, 396, 14, 14, 2, "2010-03-29", 18.2, 26.7, 404, 16, 14, 0, "2010-04-28", 16.8, 26.3, 371, 15, 15, 0, "2010-05-28", 17.8, 27.5, 334, 16, 14, 0, "2010-06-27", 17.6, 26.4, 399, 13, 17, 0, "2010-07-27", 18.0, 26.2, 308, 17, 13, 0, "2010-08-26", 17.9, 28.6, 327, 13, 17, 0, "2010-09-25", 17.7, 27.4, 399, 12, 14, 4, "2010-10-25", 17.0, 28.3, 404, 14, 14, 2,"2010-11-24", 17.6, 25.2, 416, 17, 13, 0, "2010-12-24", 16.8, 25.7, 415, 14, 15, 1, "2011-01-23", 18.3, 25.1, 374, 17, 13, 0, "2011-02-22", 16.7, 28.5, 304, 17, 13, 0,"2011-03-24", 17.0, 26.4, 309, 12, 18, 0, "2011-04-23", 17.5, 26.2, 405, 16, 14, 0, "2011-05-23", 17.4, 26.7, 332, 15, 14, 1, "2011-06-22", 16.8, 25.4, 341, 14, 14, 2, "2011-07-22", 17.0, 27.3, 310, 16, 14, 0, "2011-08-21", 18.4, 27.7, 354, 13, 16, 1,"2011-09-20", 16.9, 25.7, 356, 12, 15, 3, "2011-10-20", 17.9, 25.3, 330, 13, 14, 3, "2011-11-19", 18.5, 28.7, 403, 14, 14, 2, "2011-12-19", 16.9, 29.3, 330, 17, 13, 0,"2012-01-18", 18.0, 28.9, 405, 12, 16, 2, "2012-02-17", 16.6, 27.1, 363, 14, 14, 2, "2012-03-18", 16.9, 25.9, 400, 16, 14, 0, "2012-04-17", 18.0, 28.1, 302, 15, 14, 1, "2012-05-17", 17.9, 28.3, 310, 14, 14, 2, "2012-06-16", 16.9, 26.9, 407, 13, 15, 2, "2012-07-16", 17.0, 26.3, 300, 12, 17, 1, "2012-08-15", 18.1, 26.1, 353, 14, 14, 2,"2012-09-14", 17.6, 27.5, 331, 14, 16, 0, "2012-10-14", 18.3, 26.6, 383, 17, 13, 0,"2012-11-13", 17.6, 28.2, 315, 14, 15, 1, "2012-12-13", 18.2, 28.1, 337, 17, 13, 0,"2013-01-12", 17.8, 25.4, 378, 17, 13, 0, "2013-02-11", 17.7, 26.3, 432, 13, 17, 0, "2013-03-13", 16.8, 26.3, 422, 12, 14, 4, "2013-04-12", 16.9, 29.2, 390, 13, 15, 2,"2013-05-12", 18.0, 28.3, 344, 15, 14, 1, "2013-06-11", 17.6, 29.1, 367, 13, 15, 2, "2013-07-11", 17.5, 29.2, 390, 13, 17, 0, "2013-08-10", 16.5, 29.2, 356, 14, 16, 0, "2013-09-09", 17.6, 27.0, 354, 12, 15, 3, "2013-10-09", 17.8, 27.1, 411, 12, 17, 1, "2013-11-08", 16.8, 25.6, 383, 13, 15, 2, "2013-12-08", 16.7, 29.1, 396, 13, 17, 0, "2014-01-07", 17.2, 26.6, 418, 12, 17, 1, "2014-02-06", 17.5, 26.0, 416, 15, 15, 0, "2014-03-08", 17.2, 26.9, 407, 12, 14, 4, "2014-04-07", 17.4, 25.0, 422, 14, 16, 0, "2014-05-07", 17.5, 25.4, 354, 15, 15, 0, "2014-06-06", 16.7, 27.9, 366, 12, 16, 2, "2014-07-06", 18.2, 26.1, 302, 15, 14, 1, "2014-08-05", 18.0, 29.2, 324, 17, 13, 0, "2014-09-04", 17.9, 26.0, 340, 13, 14, 3, "2014-10-04", 16.8, 28.5, 354, 14, 16, 0, "2014-11-03", 17.2, 28.9, 379, 15, 14, 1, "2014-12-03", 18.2, 25.6, 323, 13, 15, 2, "2015-01-02", 17.4, 29.1, 440, 17, 13, 0, "2015-02-01", 16.9, 25.2, 403, 12, 15, 3, "2015-03-03", 17.9, 26.1, 413, 13, 14, 3, "2015-04-02", 17.9, 28.4, 367, 13, 16, 1, "2015-05-02", 16.6, 27.4, 405, 12, 15, 3, "2015-06-01", 17.3, 25.1, 388, 17, 13, 0, "2015-07-01", 17.8, 29.2, 319, 14, 16, 0, "2015-07-31", 17.2, 26.1, 332, 12, 15, 3, "2015-08-30", 18.0, 26.9, 346, 13, 14, 3, "2015-09-29", 17.0, 25.9, 307, 17, 13, 0, "2015-10-29", 18.4, 27.5, 329, 17, 13, 0, "2015-11-28", 17.3, 29.3, 413, 16, 14, 0, "2015-12-28", 18.4, 28.1, 365, 16, 14, 0, "2016-01-27", 18.0, 25.8, 433, 15, 15, 0, "2016-02-26", 18.4, 25.4, 380, 15, 15, 0, "2016-03-27", 16.7, 27.4, 377, 16, 14, 0, "2016-04-26", 18.4, 28.0, 392, 12, 14, 4, "2016-05-26", 16.7, 25.6, 380, 12, 16, 2, "2016-06-25", 17.4, 29.0, 387, 12, 17, 1, "2016-07-25", 16.7, 26.8, 420, 17, 13, 0,"2016-08-24", 18.5, 27.5, 372, 14, 14, 2, "2016-09-23", 18.1, 27.5, 311, 13, 14, 3, "2016-10-23", 16.9, 26.0, 324, 12, 17, 1, "2016-11-22", 17.4, 27.6, 354, 14, 14, 2, "2016-12-22", 17.2, 27.0, 364, 14, 16, 0, "2017-01-21", 17.9, 29.2, 374, 16, 14, 0, "2017-02-20", 17.3, 27.3, 418, 12, 15, 3, "2017-03-22", 17.6, 29.1, 311, 14, 14, 2, "2017-04-21", 18.1, 26.3, 400, 15, 14, 1, "2017-05-21", 17.9, 26.4, 419, 15, 14, 1, "2017-06-20", 17.1, 28.3, 343, 12, 15, 3, "2017-07-20", 17.2, 27.1, 319, 13, 17, 0, "2017-08-19", 16.9, 27.4, 398, 15, 14, 1, "2017-09-18", 17.5, 27.4, 352, 13, 14, 3, "2017-10-18", 18.2, 26.6, 420, 13, 17, 0, "2017-11-17", 17.6, 27.8, 337, 12, 16, 2, "2017-12-17", 18.4, 25.1, 344, 13, 16, 1, "2018-01-16", 17.5, 25.1, 416, 14, 15, 1, "2018-02-15", 18.3, 25.6, 420, 13, 16, 1, "2018-03-17", 17.6, 26.0, 412, 15, 15, 0, "2018-04-16", 17.2, 26.8, 327, 17, 13, 0, "2018-05-16", 17.0, 27.3, 372, 12, 18, 0, "2018-06-15", 17.7, 29.1, 421, 14, 14, 2, "2018-07-15", 18.4, 26.1, 352, 17, 13, 0]
fechas_temp_min=[]
fechas_temp_max=[]
fechas_precip_min=[]
fechas_precip_max=[]            # Listas para almacenar las fechas a impriir
fechas_max_dias_sol=[]

listafecha=[]
listatem_min=[]
listatem_max=[]                   #Listas para almacenar cada columna del arreglo
listaprecipitacion_acom=[]
listadias_soleados=[]

datos=np.array(datos,dtype=type(datos)) #se hace el arreglo de los datos
datos.shape=(108,7)                     #se dimensiona el arreglo 
nuevo=np.hsplit(datos,np.array(7))      # se divide el arreglo en columnas
listafecha=np.array(nuevo[0])
listatem_min=np.array(nuevo[1])
listatem_max=np.array(nuevo[2])             # se almacena cada columna del arreglo en una lista
listaprecipitacion_acom=np.array(nuevo[3])
listadias_soleados=np.array(nuevo[6])

tem_min=np.min(listatem_min)
tem_max=np.max(listatem_max)                      #se buscan los puntos maximos y niminos por cada columna
tem_prom_min=np.min(listaprecipitacion_acom)
tem_prom_max=np.max(listaprecipitacion_acom)
tem_sol_max=np.max(listadias_soleados)

for i in range(0,len(datos)):
    if datos[i][1]==tem_min:
        fechas_temp_min.append(datos[i][0])
    if datos[i][2]==tem_max:
        fechas_temp_max.append(datos[i][0])          # condiciones para almacenar las fechas si se cumplen los minimos y maximos
    if datos[i][3]==tem_prom_min:
        fechas_precip_min.append(datos[i][0])
    if datos[i][3]==tem_prom_max:
        fechas_precip_max.append(datos[i][0])
    if datos[i][6]==tem_sol_max:
        fechas_max_dias_sol.append(datos[i][0])
    
print(fechas_temp_min)
print(fechas_temp_max)
print(fechas_precip_min)                   # se imprimen los datos
print(fechas_precip_max)
print(fechas_max_dias_sol)


       


