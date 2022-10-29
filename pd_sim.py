
from multiprocessing.resource_sharer import stop
class Iloc:
    '''
    Oscar Poblador
    Juan Rodriguez
    Manuel Guio
    Crea listas de selección con los elementos solicitados
    uso: df2.iloc[3:5,0:2] =  titulo 1 : dato 3 y datos 4, titulo 2: dato 3 y dato 4
    '''
    seleccion_titulo=[]
    seleccion_valor=[]


    def __init__(self,data,*args,**kwargs):
        self.data=data
    def __getitem__(self,i):


        self.lista_claves=[]
        self.lista_valores=[]
        self.lista_columnas=[]
        self.lista_filas=[]
        self.diccionario={}


        try:
            j=list(i)
        except:
            j=[0]
        

        for clave in self.data:   #Para poder recorrer las posiciones
            self.lista_claves.append(clave)
        self.lista_valores=list(self.data.values())

        try:
            
            if (isinstance(j[0],slice))&(j[1].start!=None)&(j[1].stop!=None):
                l=0
                g=0
                
                titulos=self.data.keys()
                self.seleccion_titulo.clear()
                self.seleccion_valor.clear()
                titulos=self.data.keys()
                if (isinstance(j[1],slice)):
                    for k in titulos:
                        valores=self.data[k]
                        
                        if (l>=j[1].start)&(l<j[1].stop):

                            self.seleccion_titulo.append(k)
                            for g in range(j[0].start,j[0].stop):
                                self.seleccion_valor.append(valores[g])
                            self.diccionario[k]=self.lista_valores[g]
                        l=l+1
                print(self.diccionario)
                if (isinstance(j[0],slice) & isinstance(j[1],slice))&(j[1].start!=None)&(j[1].stop!=None)&(j[1].step!=None):
                    for k in range(j[1].start,j[1].stop):
                        self.lista_columnas=self.data[self.lista_claves[k]]
                        self.lista_filas=[]
                        for h in j[0]:
                            self.lista_filas.append(self.lista_columnas[h])
                            self.diccionario[self.lista_claves[k]] = self.lista_filas
                    print(self.diccionario)

            if (isinstance(j[0],slice))&(j[1].start==None)&(j[1].stop==None)&(j[1].step==None):
                for k in range(len(self.lista_claves)):
                    self.lista_columnas=self.data[self.lista_claves[k]]
                    self.lista_filas=[]
                    for h in range(j[0].start, j[0].stop):
                        self.lista_filas.append(self.lista_columnas[h])
                        self.diccionario[self.lista_claves[k]] = self.lista_filas
                print(self.diccionario)
            
            if (isinstance(j[1],slice))&(j[0].start==None)&(j[0].stop==None)&(j[0].step==None):
                for k in range(j[1].start,j[1].stop):
                    self.lista_columnas=self.data[self.lista_claves[k]]
                    self.lista_filas=[]
                    for h in range(len(self.lista_valores)):
                        self.lista_filas.append(self.lista_valores[h])
                        self.diccionario[self.lista_claves[k]] = self.lista_filas
                print(self.diccionario)

        except:
            if isinstance (i,int):
                self.seleccion_titulo.clear()
                self.seleccion_valor.clear()
                titulos=self.data.keys()
                for j in titulos:
                    valores=self.data[j]
                    self.seleccion_titulo.append(j)
                    self.seleccion_valor.append(valores[i])
                    self.diccionario[j] = self.lista_valores[i]
            print(self.diccionario)
                

            if (isinstance(j[0], list) & isinstance(j[1], list)): #Función 3 iloc
                print("entro2")
                print(j)
                for i in j[1]:
                    self.lista_columnas=self.data[self.lista_claves[i]]
                    self.lista_filas=[]
                    for k in j[0]:
                        self.lista_filas.append(self.lista_columnas[k])
                    self.diccionario[self.lista_claves[i]] = self.lista_filas
                print(self.diccionario)

            if (isinstance(j[0], int)) &  (isinstance(j[1], int)): #Función 6 iloc
                print(j)
                self.lista_columnas=self.data[self.lista_claves[j[1]]]
                print(self.lista_columnas)
                self.lista_filas=[self.lista_columnas[j[0]]]
                print(self.lista_filas)
                self.diccionario[self.lista_claves[j[1]]]=self.lista_filas
                print(self.diccionario)    

            
class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        self.iloc=Iloc(self.data)

    def __str__(self):
        return str(self.data)

    
    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices = []
            indices.append(indice)
            return indices

    def __setitem__(indice, valor):
        pass

    def iat(self, row, column):
        a = self.data
        b = a[row]
        c = b[column]
        print(c)

    def head(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[n:]

    def T(self, d):
        # print("Hola Mundo"
        print(d.data)
        keys = dict.keys(d.data)



    def funcion_tail(arch, n):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]


    def funcion_crea_Archivo(arch, sep=','):
        # esta funcion creara y guardara un nuevo archivo CSV con el mismo contenido.
        pass


    def funcion_tail(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]

    # Nicolas Arevalo 20202005024
    # Crear el comando copy


    def copy(arch, sep=';'):
        arch = open(arch)

    # Funcion encargada de localizar filas y columnas del documento e identificar si la entrada es un int,str o slice. Imprimiendo los datos.


    def loc(self, columna, fila=None):
        dat = self.data
        # fila=dat[titulos(0)]
        dat[0]
        return fila

    def __neg__(self):
        '''
        Gerardo Muñoz
        Crea un nuevo DataFrame con cada elemento negado
        uso: df2 = -df 
        '''

        # recupera el diccionario del este DataFrame 
        diccionario = self.data
        diccionario_nuevo = {}


        # niega cada elemento del diccionario (si se puede)
        llaves = diccionario.keys()

        for llave in llaves:
            lista = diccionario[llave]
            lista_nueva = []

            diccionario_nuevo[llave] = []
            for elemento in lista:
                try:
                    elemento_nuevo = - elemento
                except Exception as e:
                    elemento_nuevo = elemento
                    print('__neg__.error:',e)
                lista_nueva.append(elemento_nuevo)

            diccionario_nuevo[llave]=lista_nueva
        return DataFrame(diccionario_nuevo)


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
    


