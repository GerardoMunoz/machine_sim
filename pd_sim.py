
class Iloc:
    seleccion_titulo=[]
    seleccion_valor=[]

    def __init__(self,data,*args,**kwargs):
        self.data=data
    def __getitem__(self,i):
        try:
            j=list(i)
        except:
            j=[0]
        l=0
        g=0
        if isinstance(j[0],slice):
            titulos=self.data.keys()
            self.seleccion_titulo.clear()
            self.seleccion_valor.clear()
            for k in titulos:
                valores=self.data[k]
                if (l>=j[1].start)&(l<j[1].stop):
                    self.seleccion_titulo.append(k)

                    print("\nTitulo: ",k)
                    for g in range(j[0].start,j[0].stop):
                        self.seleccion_valor.append(valores[g])
                        print("Dato solicitado ",g,": ",valores[g])

                l=l+1
        if isinstance (i,int):
            self.seleccion_titulo.clear()
            self.seleccion_valor.clear()
            titulos=self.data.keys()
            for j in titulos:
                valores=self.data[j]
                self.seleccion_titulo.append(j)
                print ("\nTitulo: ", j)
                self.seleccion_valor.append(valores[i])
                print("Dato solicitado: ",valores[i])

class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        self.iloc=Iloc(self.data)

    def __getitem__(self,i):
        print("hola")
     

def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline() #renglones
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        data[titulo]=[]
        titulos.append(titulo) #guarda titulos
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)


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




