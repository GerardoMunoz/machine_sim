import numpy as np

class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def T(self,d):
        print(d.data,end="\n\n")
        keys=dict.keys(d.data)
        values=dict.values(d.data)
        print("Llaves: "+str(keys)+"\n\nValores: "+str(values)+"\n",end="\n\n")
        
        
        
def read_csv(arch, sep=','):
    arch = open(arch)
    linea = arch.readline()
    data = {}
    titulos = []
    for titulo in linea.split(sep):
        titulo = titulo.strip()
        data[titulo] = []
        titulos.append(titulo)
    for linea in arch.readlines():
        for i, elem_str in enumerate(linea.split(sep)):
            try:
                elem = int(elem_str)
            except:
                try: 
                    elem = float(elem_str)
                except:
                    elem=elem_str.strip()
            data[titulos[i]].append(elem)
    return DataFrame(data)

# d1 = {
#   "Nombre": "Sara",
#   "Edad": 27,
#   "Documento": 1003882
# }

# df=pd.DataFrame()
# nombres = ['Juan', 'Laura', 'Pepe']
# edades = [42, 40, 37]
# df['Nombre'] = nombres
# df['Edad'] = edades
# print(df)

#prueba

d=read_csv('datos.csv')
d.T(d)