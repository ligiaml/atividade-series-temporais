import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# Gerando série estocástica
np.random.seed(42)

serie = np.random.randn(200)

# Cálculo explícito da FAC amostral até o lag 10
fac_valores = sm.tsa.stattools.acf(serie, nlags=10)

print("Valores da FAC (lags 0 a 10):")
print(np.round(fac_valores, 3))

# Plotagem do correlograma com intervalo de confiança
fig, ax = plt.subplots(figsize=(8, 3))

plot_acf(
    serie,
    lags=20,
    ax=ax,
    alpha=0.05
)

plt.title("Correlograma (FAC Amostral)")
plt.show()

##########
# No lag 0 a FAC sempre será igual a 1 pois estamos comparando a série com ela mesma, 
# já em outros lags esperamos valores proximos a zero (dados gerados aleatoriamente)
# Portanto o grafico apresenta a maioria dos valores dentro da banda de confiança, isso indica
# uma autocorrelaçao significativa nesses lags. 
# Esse comportamento aponta ruido branco
###########