import pd_sim as pd2

nombre_archivo = 'FSM_dosUnosSeguidos.csv'

#data_frame1 = pd1.read_csv(nombre_archivo)
data_frame2 = pd2.read_csv(nombre_archivo)


# #print(data_frame1)
# print(data_frame2)


# print()

#print(data_frame1.head())
#error print(data_frame2.head())

# print()

# #print(data_frame1.tail())
# #error print(data_frame2.tail())

# print()

# #print(data_frame1.index)
# #error print(data_frame2.index)

# print()

# #print(data_frame1.describe())
# #error print(data_frame2.describe())

# print()


# #print(data_frame1.T)
# print(data_frame2.T)
# #error print(data_frame2.T())


# print()


# #print(data_frame1.sort_index(axis=1, ascending=False))
# #error print(data_frame2.sort_index(axis=1, ascending=False))

# print()

# #print(data_frame1['Est_act'])
# #print(data_frame2['Est_act'])

# print()

# #print(data_frame1[0:3])
# #print(data_frame2[0:3])

# print()

# #print(data_frame1.loc[0])
# #error print(data_frame2.loc[0])
# #error print(data_frame2.loc(0))

# print()

#print(data_frame1.at[1, "Est_act"])
#error print(data_frame2.at[1, "Est_act")])
#error print(data_frame2.at(1, "Est_act"))

# print()

# #print(data_frame1 > 0)
# #error print(data_frame2 > 0)

# print()

# #print(data_frame1.iloc[3])
# #error print(data_frame2.iloc[3])
# #error print(data_frame2.iloc(3))

# print()

# #data_frame1_a=data_frame1.copy()
# #print(data_frame1_a)
# #error data_frame2_a=data_frame2.copy()
# #error print(data_frame2_a)

# print()

# #data_frame1_a['Est_act'] = 0
# #print(data_frame1_a)
# #data_frame2['Est_act'] = 0
# #print(data_frame2)

# print('Función negar -, Gerardo Muñoz')

# #print(-data_frame1)
# print(-data_frame2)

# print()


#Oscar David Poblador Parra - 20211005116
#Función de selección de datos Iloc
print("\nIloc seleccion entero y slice - Oscar Poblador 20211005116")
print("\nPRUEBA CON PARAMETRO ENTERO")
data_frame2.iloc[2]
print("\n")
print("\nValores seleccionados")
print(data_frame2.iloc.seleccion_titulo)
print(data_frame2.iloc.seleccion_valor)
print("\nPRUEBA CON PARAMETRO SLICE")
data_frame2.iloc[1:3,0:2]
print("\nValores seleccionados")
print("\n")
print(data_frame2.iloc.seleccion_titulo)
print(data_frame2.iloc.seleccion_valor)



#Test función 3 iloc
#Juan David Bello Rodríguez - 20211005028

data_frame2.iloc[[1,2],[1,2]] #Selecciona filas y columnas y las imprime
data_frame2.iloc[1,2]


#Test función 4 iloc
#Manuel Alejandro Guio Cardona - 20211005061
print("\nIloc seleccion slice y slice completo - Manuel Guio 20211005061")

print("\nPrueba con slice en columnas (derecha), imprime todas las filas")
data_frame2.iloc[ : ,1:3]

print("\nPrueba con slice en filas (izquierda), imprime todas las columnas ")
data_frame2.iloc[1:3, : ]

