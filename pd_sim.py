
seleccion_titulo = []
seleccion_valor = []


class Loc:
    def __init__():
        pass

    def __getitem__(self,n):
        lista=list(n)
        n=0
        print("datos de la fila: " +n)
        ##Falla fila no esta definida
        # if fila(d,slice):
        #     d=x+1
        #     print("datos de la fila: " +dat)
        #     for dat in x
        #     pass



class Iloc:
    '''
    Oscar Poblador
    Crea listas de selección con los elementos solicitados
    uso: df2.iloc[3:5,0:2] =  titulo 1 : dato 3 y datos 4, titulo 2: dato 3 y dato 4
    '''
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

class Iat(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.loc = Loc()
    def __getitem__(self, nums):  # Obtiene los indices de fila y columna
        row, column = nums
        return self.data[row][column]

    def __setitem__(self, nums, valor):
        row, column = nums
        self.data[row][column] = valor


class DataFrame:
    
    def __init__(self, data, index=None, *args, **kwargs):
        self.data = data  # Es un diccionario de la siguiente forma:
        '''
        {
            Titulo1 : [elem11,elem12,elem13,...],
            Titulo2 : [elem21,elem22,elem23,...],
            Titulo3 : [elem31,elem32,elem33,...],
            ...
        }
        '''
        if isinstance(data, dict):
            for primer_titulo in data.keys():
                break  # truco para obtener la primera llave del diccionario
        else:
            primer_titulo = 0
        # es una lista con el nombre de los indices
        self.index = index if index else list(range(len(data[primer_titulo])))
    
    def __str__(self):

        return str(self.data)+('\nindices: '+str(self.index) if self.index else '')

    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices = []
            indices.append(indice)
            return indices

    def __setitem__(indice, valor):
        pass

    def head(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[n:]

    def T(self, d):
        # print("Hola Mundo"
        print(d.data)
        keys = dict.keys(d.data)

    def funcion_crea_Archivo(arch, sep=','):
        # esta funcion creara y guardara un nuevo archivo CSV con el mismo contenido.
        pass

    def funcion_tail(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]

    def __getitem__(self, i):
        j = list(i)
        l = 0
        g = 0
        if isinstance(j[0], slice):
            titulos = self.data.keys()
            seleccion_titulo.clear()
            seleccion_valor.clear()
            for k in titulos:
                valores = self.data[k]
                if (l >= j[1].start) & (l < j[1].stop):
                    seleccion_titulo.append(k)
                    print("\nTitulo: ", k)
                    for g in range(j[0].start, j[0].stop):
                        seleccion_valor.append(valores[g])
                        print("Dato solicitado ", g, ": ", valores[g])

                l = l+1

    # Realizar lecturas según su posición

    def iloc(self, i):
        if isinstance(i, slice):
            print("lo logramos")
        if isinstance(i, int):
            seleccion_titulo.clear()
            seleccion_valor.clear()
            titulos = self.data.keys()
            for j in titulos:
                valores = self.data[j]
                seleccion_titulo.append(j)
                print("\nTitulo: ", j)
                seleccion_valor.append(valores[i])
                print("Dato solicitado: ", valores[i])

    # 20202005024
    # Crear el comando que agrege una nueva columna

    def adi(self):

        diccionario = self.data
        diccionario_nuevo = {}
        columna = diccionario.keys()
        fila_nueva = []
        diccionario_nuevo[columna] = fila_nueva

    # Funcion encargada de localizar filas y columnas del documento e identificar si la entrada es un int,str o slice. Imprimiendo los datos.

    def loc(self, columna, fila=None):
        dat = self.data
        # fila=dat[titulos(0)]
        dat[0]
        return fila

    def iat(self, row, column):
        a = self.data
        b = a[row]
        c = b[column]
        print(c)

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
                    print('__neg__.error:', e)
                lista_nueva.append(elemento_nuevo)

            diccionario_nuevo[llave] = lista_nueva
        return DataFrame(diccionario_nuevo)

    def T(self, d):
        print(d.data, end="\n\n")
        keys = dict.keys(d.data)
        values = dict.values(d.data)
        print("Llaves: "+str(keys)+"\n\nValores: "+str(values)+"\n", end="\n\n")


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
                    elem = elem_str.strip()

            data[titulos[i]].append(elem)
    return DataFrame(data)