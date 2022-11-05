seleccion_titulo=[]
seleccion_valor=[]

class DataFrame:        
    def __init__(self, data, *args, **kwargs):
        self.data = data

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
    
    def T(self):
        '''
        La función T transpone las columnas y los renglones .... las llaves del diccionario con los índices de sus valores
        >>> df=DataFrame({'Pri': [2, 3, 5], '2**n': [2, 4, 8]})
        >>> print(df)
        {'Pri': [2, 3, 5], '2**n': [2, 4, 8]}
        >>> print(df.T())
        {'Index':['Pri','2**n'],'0':['2','2'],'1':['3','4'],'2':['5','8']}
        '''
        print(self.data)
        keys=list(self.data.keys())
        values=list(self.data.values())
        newdict={}
        newkeys=[]
        newvalues=[]
        newkeys.append(keys[0])
        for i in values[0]:
            newkeys.append(i)
        for i in keys[1:]:
            newvalues.append(i)
        for i in values[1:]:
            newvalues.append(str(i[0]))
        for i in values[1:]:
            newvalues.append(str(i[1]))
        for i in values[1:]:
            newvalues.append(str(i[2]))
        print(newkeys,end="\n\n")
        print(newvalues,end="\n\n")
        for i in newkeys:
            newdict[i]=[]
        for i in newkeys[0]:
            newdict[i]=[newvalues]
        print(newdict)
        return DataFrame(newdict)
        
    def iat(self, row, column):
        a = self.data
        b = a[row]
        c = b[column]
        print(c)

    def head(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[n:]

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

    def __getitem__(self,i):
        j=list(i)
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
            
    #Realizar lecturas según su posición

    def iloc(self,i):
        
        if isinstance(i,slice):
            print("lo logramos")
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