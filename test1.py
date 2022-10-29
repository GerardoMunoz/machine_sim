# test funcion iat - Willian Chaparro
import pd_sim as pd
data={"tit1":[0, 2, 3],"tit2":[0, 4, 1],"tit3":[10, 20, 30]}
df =pd.DataFrame(data)
#df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]])
print(df.iat[0,1])
print('Valor antiguo: ',df.iat[0,2])
df.iat[0,2]=10
print('Valor nuevo: ',df.iat[0,2])
