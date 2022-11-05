seleccion_titulo = []
seleccion_valor = []


class Loc:
    def __init__():
        pass

    def __getitem__(self, n):
        lista = list(n)
        n = 0
        print("datos de la fila: " + n)
        # Falla fila no esta definida
        # if fila(d,slice):
        #     d=x+1
        #     print("datos de la fila: " +dat)
        #     for dat in x
        #     pass


class Iloc:

    lista_claves = []
    lista_valores = []
    lista_columnas = []
    lista_filas = []
    diccionario = {}
    '''
    Oscar Poblador
    Juan Rodriguez
    Manuel Guio
    Crea listas de selección con los elementos solicitados
    uso: df2.iloc[3:5,0:2] =  titulo 1 : dato 3 y datos 4, titulo 2: dato 3 y dato 4
    '''
    seleccion_titulo = []
    seleccion_valor = []

    def __init__(self, data, *args, **kwargs):
        self.data = data

    def __getitem__(self, i):

        self.lista_claves = []
        self.lista_valores = []
        self.lista_columnas = []
        self.lista_filas = []
        self.diccionario = {}

        try:
            j = list(i)
        except:
            j = [0]

        for clave in self.data:  # Para poder recorrer las posiciones
            self.lista_claves.append(clave)
        self.lista_valores = list(self.data.values())

        try:

            if(isinstance(j[1], slice)) & (j[0].start == None) & (j[0].stop == None) & (j[0].step == None):

                for k in range(j[1].start, j[1].stop):
                    for h in range(j[1].start, j[1].stop):
                        self.diccionario[self.lista_claves[k]
                                         ] = self.data[self.lista_claves[k]]

            if (isinstance(j[0], slice)) & (j[1].start == None) & (j[1].stop == None) & (j[1].step == None):
                for k in range(len(self.lista_claves)):
                    self.lista_columnas = self.data[self.lista_claves[k]]
                    self.lista_filas = []
                    for h in range(j[0].start, j[0].stop):
                        self.lista_filas.append(self.lista_columnas[h])
                        self.diccionario[self.lista_claves[k]
                                         ] = self.lista_filas

            if (isinstance(j[0], slice)) & (j[1].start != None) & (j[1].stop != None):
                l = 0
                g = 0
                aux = []
                titulos = self.data.keys()
                self.seleccion_titulo.clear()
                self.seleccion_valor.clear()
                titulos = self.data.keys()

                if (isinstance(j[1], slice)):
                    for k in titulos:
                        valores = self.data[k]
                        if (l >= j[1].start) & (l < j[1].stop):
                            self.seleccion_titulo.append(k)
                            for g in range(j[0].start, j[0].stop):
                                self.seleccion_valor.append(valores[g])
                            aux = list(self.seleccion_valor)
                            self.diccionario[k] = aux

                            self.seleccion_valor.clear()
                        l = l+1

                if (isinstance(j[0], slice) & isinstance(j[1], slice)) & (j[1].start != None) & (j[1].stop != None) & (j[1].step != None):

                    for k in range(j[1].start, j[1].stop):
                        self.lista_columnas = self.data[self.lista_claves[k]]
                        self.lista_filas = []
                        for h in j[0]:
                            self.lista_filas.append(self.lista_columnas[h])
                            self.diccionario[self.lista_claves[k]
                                             ] = self.lista_filas

        except:

            if isinstance(i, int):

                self.seleccion_titulo.clear()
                self.seleccion_valor.clear()
                titulos = self.data.keys()
                for j in titulos:
                    valores = self.data[j]
                    self.seleccion_titulo.append(j)
                    self.seleccion_valor.append(valores[i])
                    self.diccionario[j] = valores[i]

            if (isinstance(j[0], list) & isinstance(j[1], list)):  # Función 3 iloc

                for i in j[1]:
                    self.lista_columnas = self.data[self.lista_claves[i]]
                    self.lista_filas = []
                    for k in j[0]:
                        self.lista_filas.append(self.lista_columnas[k])
                    self.diccionario[self.lista_claves[i]] = self.lista_filas

            if (isinstance(j[0], int)) & (isinstance(j[1], int)):  # Función 6 iloc

                self.lista_columnas = self.data[self.lista_claves[j[1]]]
                self.lista_filas = [self.lista_columnas[j[0]]]
                self.diccionario[self.lista_claves[j[1]]] = self.lista_filas

        return DataFrame(self.diccionario)


'''Willian Chaparro codigo 9520520
 Se define el metodo .iat
uso: df[a,b] devuelve la fila 'a' y la columna 'b' de una matriz '''


class Iat(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data

    def __getitem__(self, nums):  # Obtiene los indices de fila y columna
        row, column = nums
        return self.data[row][column]

    def __setitem__(self, nums, valor):
        row, column = nums
        self.data[row][column] = valor


class DataFrame:

    def __init__(self, data, index=None, *args, **kwargs):
        """Devuelve los datos como string
        >>> df = DataFrame({'T1':[1,2],'T2':[3,4]})
        >>> df #print(df)
        {'T1': [1, 2], 'T2': [3, 4]}
        >>> df.titles
        ['T1', 'T2'] 
        >>> df.index
        [0, 1]
        """
        
 
        if isinstance(data,dict):
            self.data = data  
        elif isinstance(data,list):
            self.data = {i:val for i,val in enumerate(data)}
        else:
            raise Exception('Sólo se aceptan dict como {"T1": [1, 2], "T2": [3, 4]} o list, pero se recibió '+ str(data) )

        self.titles = list(data.keys())

        # index es una lista con el nombre de los indices
        self.index = index if index else list(range(len(data[self.titles[0]])))

    #@table_decorador.table
    def __str__(self):
        return str(self.data)+('\nindices: '+str(self.index) if self.index else '')

    def print_data_pretty(self, data, vertical_data=[]):
        table_string = ""
        titles = data.keys()
        values = data.values()
        _list_values = []
        _dict_values_spacing = {}
        _vertical_values_spacing = {}
        _values_spacing = []
        _values_spacing_vertical = []
        for _, new_val in data.items():
            _list_values.append(len([item for item in new_val if item]))
        for i in range(-1, max(_list_values)):
            for title in titles:
                for key, value in data.items():
                    if not title in _dict_values_spacing:
                        _dict_values_spacing[title] = []
                    if key == title:
                        _dict_values_spacing[title].append(len(value[i]))
        for i in range(0, len(vertical_data)):
            _values_spacing_vertical.append(len(vertical_data[i]))
        for i in range(-1, max(_list_values)):
            if len(vertical_data) > 0:
                row = " " * (max(_values_spacing_vertical) + 2)
            else:
                row = " " * (len(str(max(_list_values))) + 2)
            if i != -1:
                if i < 10:
                    if len(vertical_data) > 0:
                        row = vertical_data[i] + " " * \
                            (max(_values_spacing_vertical) -
                             len(vertical_data[i]) + 2)
                    else:
                        row = str(i) + " " * (len(str(max(_list_values))) + 1)
                else:
                    if len(vertical_data) > 0:
                        row = vertical_data[i] + " " * \
                            (max(_values_spacing_vertical) -
                             len(vertical_data[i]) + 2)
                    else:
                        row = str(i) + " " * len(str(max(_list_values)))
            for title in titles:
                if i != -1:
                    for key, value in data.items():
                        if key == title:
                            row += value[i] + " " * \
                                (max(
                                    _dict_values_spacing[title]) - len(str(value[i])) + 2)
                else:
                    row += title + " " * \
                        (max(_dict_values_spacing[title]) - len(title) + 2)
            table_string += row + "\n"
        return table_string

    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices = []
            indices.append(indice)
            return indices

    def __setitem__(indice, valor):
        pass

    def head(self, n=5):

    '''
     Argumentos:
     Self:Diccionario dentro del cual se enceuntran los datos
     n: nu
     
    
    '''
        for column_title in list(self.data.keys()):
            print(self.data[column_title][:n])

    def tail(self, n=-5):
        for column_title in list(self.data.keys()):
            print(self.data[column_title][n:])

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
    # Nicolas Arevalo 20202005024
    # Crear el comando copy

    def iat(self, row, column):
        a = self.data
        b = a[row]
        c = b[column]
        print(c)

    def funcion_tail(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]

    def copy(arch, sep=';'):
        arch = open(arch)

    # Funcion encargada de localizar filas y columnas del documento e identificar si la entrada es un int,str o slice. Imprimiendo los datos.

    def loc(self, columna, fila=None):
        dat = self.data
        # fila=dat[titulos(0)]
        dat[0]
        return fila

#     def sort_index(axis, ascending)
#
#         if ascendig ==true:
#             n = len(indice)
#             for i in range(n-1):       # <-- bucle padre
#                 for j in range(n-1-i): # <-- bucle hijo
#                     if indice[j] > indice[j+1]:
#                         indice[j], indice[j+1] = incice[j+1], indice[j]
#         else
#             n = len(indice)
#             for i in range(n-1):       # <-- bucle padre
#                 for j in range(n-1-i): # <-- bucle hijo
#                     if indice[j] > indice[j+1]:
#                         indice[j], indice[j+1] = incice[j+1], indice[j]
#

    # DataFrame.sort_index()

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

    def describe(self):
        data = self.data
        _dict_describe = {}
        _list_values = []
        _list_values_count = []
        _list_values_only_numbers = []
        titles = data.keys()
        for _, new_val in self.data.items():
            _list_values.append([item for item in new_val if item])
            _list_values_count.append(len([item for item in new_val if item]))
        for i in range(0, len(_list_values)):
            _list = []
            for j in _list_values[i]:
                _list.append(j.isnumeric())
            _list_values_only_numbers.append(_list)

        for x in _list_values_only_numbers:
            global _only_numbers
            _only_numbers = False
            if x.count(True):
                _only_numbers = True
        for i in range(-1, len(_list_values)):
            for title in titles:
                for key, value in data.items():
                    if key == title:
                        _dict_describe[title] = []
                        _dict_describe[title].append(_list_values_count[i])
        # if not _only_numbers:

        print(_dict_describe)

    def __gt__(self, other):
        a = self.data
        for titulo in a:
            for elem in titulo:
                for elem, i in enumerate(titulo):
                    if (elem > other):
                        a[titulo][i] = elem
                    else:
                        a[titulo][i] = None
        return DataFrame(a)

    def _getitem_(self, item):

        diccionarrio = self.data
        nuevo_diccionario = {}

        if isinstance(item, int):
            print(item)
            return nuevo_diccionario[item]

        if isinstance(item, slice):
            print(item)
            return nuevo_diccionario[item]


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
