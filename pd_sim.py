from msilib.sequence import InstallExecuteSequence


seleccion_titulo=[]
seleccion_valor=[]


class DataFrame:
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.iloc= Iloc(data)

    def __str__(self):
        return str(self.data)

    
#     def _index_(arch):
#         arch = open(arch)
#         for i in arch.keys():
#             indice = arch.keys()
#             indices = []
#             indices.append(indice)
#             return indices
# 
#     def __setitem__(indice, valor):
#         pass
# 
#     def iat(self, row, column):
#         a = self.data
#         b = a[row]
#         c = b[column]
#         print(c)
# 
#     def head(arch, n, sep=';'):
#         with open(arch) as f:
#             lineas = [lineas.strip('\n') for lineas in f.readlines()]
#         return lineas[n:]
# 
#     def T(self, d):
#         # print("Hola Mundo"
#         print(d.data)
#         keys = dict.keys(d.data)
# 
# 
# 
#     def funcion_tail(arch, n):
#         with open(arch) as f:
#             lineas = [lineas.strip('\n') for lineas in f.readlines()]
#         return lineas[-n:]
# 
# 
#     def funcion_crea_Archivo(arch, sep=','):
#         # esta funcion creara y guardara un nuevo archivo CSV con el mismo contenido.
#         pass
# 
# 
#     def funcion_tail(arch, n, sep=';'):
#         with open(arch) as f:
#             lineas = [lineas.strip('\n') for lineas in f.readlines()]
#         return lineas[-n:]
# 
#     # Nicolas Arevalo 20202005024
#     # Crear el comando copy
# 

#     def __getitem__(self,i):
#         if isinstance(i,slice):
#             pass
#         elif isinstance(i,int):
#             
#             pass
#         
            
    #    j=list(i)
#         l=0
#         g=0
#         if isinstance(j[0],slice):
#             titulos=self.data.keys()
#             seleccion_titulo.clear()
#             seleccion_valor.clear()
#             for k in titulos:
#                 valores=self.data[k]
#                 if (l>=j[1].start)&(l<j[1].stop):
#                     seleccion_titulo.append(k)
#                     print("\nTitulo: ",k)
#                     for g in range(j[0].start,j[0].stop):
#                         seleccion_valor.append(valores[g])
#                         print("Dato solicitado ",g,": ",valores[g])
# 
#                 l=l+1
     
            
    #Realizar lecturas según su posición

#  
#     
# 
# 
# 
# def funcion_tail(arch, n,sep=';'):
# 	with open(arch) as f:
# 		lineas = [lineas.strip('\n') for lineas in f.readlines()]
# 	return lineas[-n:]
#  
#  
# def read_csv(arch,sep=';'):
# 
# 
#     def copy(arch, sep=';'):
#         arch = open(arch)
# 
#     # Funcion encargada de localizar filas y columnas del documento e identificar si la entrada es un int,str o slice. Imprimiendo los datos.
# 
# 
#     def loc(self, columna, fila=None):
#         dat = self.data
#         # fila=dat[titulos(0)]
#         dat[0]
#         return fila
# 
#     def __neg__(self):
#         '''
#         Gerardo Muñoz
#         Crea un nuevo DataFrame con cada elemento negado
#         uso: df2 = -df 
#         '''
# 
#         # recupera el diccionario del este DataFrame 
#         diccionario = self.data
#         diccionario_nuevo = {}
# 
# 
#         # niega cada elemento del diccionario (si se puede)
#         llaves = diccionario.keys()
# 
#         for llave in llaves:
#             lista = diccionario[llave]
#             lista_nueva = []
# 
#             diccionario_nuevo[llave] = []
#             for elemento in lista:
#                 try:
#                     elemento_nuevo = - elemento
#                 except Exception as e:
#                     elemento_nuevo = elemento
#                     print('__neg__.error:',e)
#                 lista_nueva.append(elemento_nuevo)
# 
#             diccionario_nuevo[llave]=lista_nueva
#         return DataFrame(diccionario_nuevo)

    def __getitem__(self,item):
        
        '''
        Argumentos:
        Por medio de la funcion __getitem__ se pretende imprimir el elemento de una ubicacion
        en especifico bien sean filas, y/o columnas
        ejemplos
        
        >>> df = DataFrame({'T1':[1,2,3],'T2':[4,5,6],'T3':[7,8,9],'T4':[10,11,12] })
        >>> df [0:2]
        {'T1':[1,2,3],'T2':[4,5,6]}
        >>> df ["T1":"T2"]
        {'T1':[1,2,3],
         'T2':[4,5,6]}
        
        '''

        diccionarrio = self.data
        nuevo_diccionario = {}
        if isinstance(item,str):
            nuevo_diccionario[item]=self.data[item]
            return DataFrame(nuevo_diccionario)

        if isinstance(item,int):
            
            return DataFrame(nuevo_diccionario)

        if isinstance(item, slice):
            print(item)
            return DtatFrame(nuevo_diccionario)

# 
# 
# 
# 
# 
# def read_csv(arch, sep=','):
# 
#     arch = open(arch)
#     linea = arch.readline()
#     data = {}
#     titulos = []
#     for titulo in linea.split(sep):
#         titulo = titulo.strip()
#         data[titulo] = []
#         titulos.append(titulo)
#         
#     for linea in arch.readlines():
# 
#         for i,elem in enumerate(linea.split(sep)):
#             data[titulos[i]].append(elem.strip())
# 
#         for i, elem_str in enumerate(linea.split(sep)):
#             try:
#                 elem = int(elem_str)
#             except:
#                 try: 
#                     elem = float(elem_str)
#                 except:
#                     elem=elem_str.strip()
# 
#             data[titulos[i]].append(elem)
# 
#     return DataFrame(data)
# 
# 
#     return DataFrame(data)           
# #prueba
# # d=read_csv('datos.csv')
# # print(d.data)
# # print(d[6])
# # print(d[3:9:2])
# # print(d[:])
# #x=sum(map(len,d.data.values()))
# #print(x)
# 
# # for c in d.data.keys():
# #     print (d.data[c])
# #     
# # for t in d.data:
# #    print (t, ":", d.data[t])
# #    
# # 
# #   
# # print ("\n",funcion_tail("datos.csv",5))  
# #             
# #         
# # #pruebaaa
# # d=read_csv('datos.csv')
# # print(d.data)
# # 
# # #prueba Willian
# # #d=read_csv('datos.csv')
# # #print(d.data)
# # #>>>>>>> origin/main
# # 
import doctest
doctest.testmod(verbose=True)
