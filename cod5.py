import numpy as np
import pandas as pd
import statsmodels.api as sm

from statsmodels.tsa.arima_process import ArmaProcess

# Comparação entre a FAC teórica e a FAC amostral
theta1 = 0.7

ma_params = np.array([1, -theta1])

processo = ArmaProcess(
    np.array([1]),
    ma_params
)

# FAC teórica exata
fac_teorica = processo.acf(lags=5)

# Amostra com N = 500
np.random.seed(42)

amostra = processo.generate_sample(nsample=500)

fac_amostral = sm.tsa.stattools.acf(
    amostra,
    nlags=5
)

df_comparacao = pd.DataFrame({
    'Lag': range(6),
    'FAC Teórica': fac_teorica,
    'FAC Amostral (N=500)': fac_amostral
})

print(df_comparacao.round(4))

##########
# Neste exemplo, é feita uma comparação entre a FAC esperada teoricamente para um modelo MA(1) e
# a FAC calculada a partir de uma amostra de 500 observações. Os valores podem apresentar pequenas diferenças, 
# pois a FAC amostral é uma estimativa baseada nos dados observados.
####