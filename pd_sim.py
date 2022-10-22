seleccion_titulo=[]
seleccion_valor=[]
class Iloc:
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
            seleccion_titulo.clear()
            seleccion_valor.clear()
            for k in titulos:
                valores=self.data[k]
                if (l>=j[1].start)&(l<j[1].stop):
                    seleccion_titulo.append(k)
                    print("\nTitulo: ",k)
                    for g in range(j[0].start,j[0].stop):
                        seleccion_valor.append(valores[g])
                        print("Dato solicitado ",g,": ",valores[g])

                l=l+1
        if isinstance (i,int):
            seleccion_titulo.clear()
            seleccion_valor.clear()
            titulos=self.data.keys()
            for j in titulos:
                valores=self.data[j]
                seleccion_titulo.append(j)
                print ("\nTitulo: ", j)
                seleccion_valor.append(valores[i])
                print("Dato solicitado: ",valores[i])
class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        self.iloc=Iloc(self.data)

    def __getitem__(self,i):
        print("hola")
     
            
    #Realizar lecturas según su posición

    

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

    
            
    
    
datos="hola.csv"       
d=read_csv(datos)
d.iloc[4]
d.iloc[3:5,0:2]
print("\n")
print(seleccion_titulo)
print(seleccion_valor)





#    A         B         C         D
#  0.469112, -0.282863, -1.509059, -1.135632
# 1.212112, -0.173215,  0.119209, -1.044236
# -0.861849, -2.104569, -0.494929,  1.071804
#  0.721555, -0.706771, -1.039575,  0.271860
# -0.424972,  0.567020,  0.276232, -1.087401
# -0.673690,  0.113648, -1.478427,  0.524988


