import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess

# Definindo um processo MA(2)
# Z_t = e_t + 0.6*e_(t-1) - 0.3*e_(t-2)

ar_params = np.array([1])
ma_params = np.array([1, 0.6, -0.3])

processo_ma2 = ArmaProcess(ar_params, ma_params)

# Simulando 500 observações
np.random.seed(123)

dados_ma2 = processo_ma2.generate_sample(nsample=500)

plt.figure(figsize=(8, 3))
plt.plot(dados_ma2, linewidth=1)
plt.title('Serie Temporal Simulada de um Processo MA (2)')
plt.show()

#################
# O cod gera um grafico de uma serie temporal criada a partir do processo MA(2).
# Um ponto importante da MA(2) é a existencia de dependencia entre a obervaçao 
# atual e os dois erros anteriores. Por isso buscamos encontrar autocorrelaçao significativa
# princiaplmente no lag 1 e 2, e no lag 2 a autocorrelaçao tende a desaparecer.
#################
