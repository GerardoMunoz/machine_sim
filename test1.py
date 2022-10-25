# test funcion iat - Willian Chaparro
import pd_sim as pd
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
print(df.iat[0,1])
print('Valor antiguo: ',df.iat[0,2])
df.iat[0,2]=10
print('Valor nuevo: ',df.iat[0,2])
