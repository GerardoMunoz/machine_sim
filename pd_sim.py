class Iloc:
    seleccion_titulo=[]
    seleccion_valor=[]

    lista_claves=[]
    lista_valores=[]
    lista_columnas=[]
    lista_filas=[]
    diccionario={}

    def __init__(self,data,*args,**kwargs):
        self.data=data
    def __getitem__(self,i):
        try:
            j=list(i)
        except:
            j=[0]
        l=0
        g=0

        for clave in self.data:   #Para poder recorrer las posiciones
            self.lista_claves.append(clave)
        self.lista_valores=list(self.data.values())

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

            
        if (isinstance(i[0], int) &  isinstance(i[1], int)): #Función 6 iloc
            self.lista_columnas=self.data[self.lista_claves[i[1]]]
            self.lista_filas=[self.lista_columnas[i[0]]]
            self.diccionario[self.lista_claves[i[1]]]=self.lista_filas
            print(self.diccionario)


