#Daniel Cortes, esta es la funcion la cual recibira un arreglo
#Daniel Cortes*args el cual tendra distinto valores, con el **kwargs elegira los parametros
# Daniel Cortes los cuales apareceran en pantalla
def asm_pio(*args, **kwargs):
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs)
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    #daniel cortes, nos da un tiempo determinado de espera

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        #Daniel Cortes; sobra igualar sm_iniciandose= self; porque
        #Daniel Cortes; no lo estamos usando y al final de esta funcion termina en su estado inicial
        fsms[id_]=self
        pass
      #Daniel Cortes; en esta funcion se recibne los parametros
      #Daniel Cortes; guardando e imprimiendo el valor de self en una variable global "fsms"

  def active(self, x=None):
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')
    #Daniel Cortes; la simulacion seria un buen objeto de practica, pero que se vean con una interfaz grafica :P

fsms=[None]*8

sm_iniciandose=None


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)
        #Daniel Cortes imprimira el self y el nombre de la clase
        pass

    def __getitem__(self,name):
        #print('nop.__getattr__',name)
        pass
        #Daniel Cortes, no esta en funcionamiento ya que la unica accion accion
        #Daniel Cortes; que realizaba  esta en comentario
class set(nop):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
   #Daniel Cortes esta clase hereda las condiciones de la clase nop,
   #Daniel Cortes pero aparecera impresa la clase set
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass
   #Daniel Cortes esta clase hereda las condiciones de la clase nop,
   #Daniel Cortes pero aparecera impresa la clase wrap_traget
class wrap(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass
    #Daniel Cortes esta clase hereda las condiciones de la clase nop,
    #Daniel Cortes pero aparecera impresa la clase wrap
