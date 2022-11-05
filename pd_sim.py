class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data



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
            
        
def loc(index, columns):
    '''
    Retorna la columna completa del titulo que se ingreso
    >>> df= pd.DataFrame([1,2],[3,4])
    >>> pd.DataFrame(columns=['titulo1','titulo2'])
    >>> pd.DataFrame(index=['estado1', 'estado2'])
    >>> ['estado1']
    ['titulo1', 'titulo2']
    '''
import doctest
doctest.testmod(verbose=True)
