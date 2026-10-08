import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf

# Z_t = e_t - 0.8 * e_(t-1)
# theta_1 = 0.8

ar_ma1 = np.array([1])
ma_ma1 = np.array([1, -0.8])

processo_ma1 = ArmaProcess(ar_ma1, ma_ma1)

dados_ma1 = processo_ma1.generate_sample(nsample=1000)

# Plot da FAC
fig, ax = plt.subplots(figsize=(8, 3))

plot_acf(
    dados_ma1,
    lags=10,
    ax=ax,
    title="FAC do MA(1): Identificação do Corte no Lag 1"
)

plt.show()

###########3
# Como o processo é MA(1) esperamos que a autocorrelaçao seja significativa 
# no lag 1 mas comece a desaparecer no lag 2
###########