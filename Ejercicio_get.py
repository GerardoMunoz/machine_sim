class Indexado():##Revisar donde va reailmente esto!!!! CarlosMario1818

    def __init__(self):
        self.data=[0,0,0,0]
        doc=open("FSM_dosUnosSeguidos.csv")
        leer=doc.read()
        print(leer)
        
    def __getitem__(self,item):

        if (item,int):
            print("Est_act: ",item)
            return self.data[item]
        else:
            print("slice: ",item)
            return self.data[item]
    
    def __setitem__(self, key, value):
        self.data[key]=value
        
i=Indexado()
print(i[0:4])

i[0]=15
print(i[0])