class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
    def iat(self,row,column):
        a=self.data
        b=a[row]
        c=b[column]
        print(c)
        
    



def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        data[titulo]=[]
        titulos.append(titulo)
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)
            
        
#prueba Willian
#d=read_csv('datos.csv')
#print(d.data)
