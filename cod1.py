import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando dados sintéticos de vendas
np.random.seed(42)

datas = pd.date_range(
    start='2026-01-01',
    periods=100,
    freq='D'
)

ruido = np.random.normal(0, 5, 100)
tendencia = np.linspace(10, 50, 100)

vendas = tendencia + ruido

df = pd.DataFrame({
    'Data': datas,
    'Vendas': vendas
}).set_index('Data')

# Média Móvel Simples (SMA) de 7 e 14 dias
df['SMA_7'] = df['Vendas'].rolling(window=7).mean()
df['SMA_14'] = df['Vendas'].rolling(window=14).mean()

print(df.tail(5))

########################
##A média movel serve para suavizar as oscilações da série temporal, 
##em vez de observar cada valor de venda podemos observar a media dos
##valores resentes. A média de 14 dias tente a ser mais suave que a de 7 dias
## pois considera uma quantidade maior de observações. Não existe média movel 
## dos primeiros valores por não termos 7 ou 14 observações anteriores suficientes
#########################

