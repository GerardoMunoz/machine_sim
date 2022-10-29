from itertools import count
from decorador import table_decorador

seleccion_titulo=[]
seleccion_valor=[]

class DataFrame:
    def __init__(self, data, *args, **kwargs):
        self.data = data

    def __str__(self):
        return self.print_data_pretty(self.data)

    def __getitem__(self, indice):
        print('indice', indice)
        if isinstance(indice, slice):
            print('slice', indice.start, indice.step, indice.stop)

    def print_data_pretty(self, data, vertical_data = []):
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
                    if not title in _dict_values_spacing :
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
                        row = vertical_data[i] + " " * (max(_values_spacing_vertical) - len(vertical_data[i]) + 2)
                    else:
                        row = str(i) + " " * (len(str(max(_list_values))) + 1)
                else:
                    if len(vertical_data) > 0:
                        row = vertical_data[i] + " " * (max(_values_spacing_vertical) - len(vertical_data[i]) + 2)
                    else:
                        row = str(i) + " " * len(str(max(_list_values)))
            for title in titles:
                if i != -1:
                    for key, value in data.items():
                        if key == title:
                            row += value[i] + " " * (max(_dict_values_spacing[title]) - len(str(value[i])) + 2)
                else:
                    row += title + " "*(max(_dict_values_spacing[title]) - len(title) + 2)
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
        #if not _only_numbers:

        print(_dict_describe)

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

