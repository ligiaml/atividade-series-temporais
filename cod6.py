import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox

# Teste formal de hipótese para autocorrelação global
# H0: a série é um ruído branco

np.random.seed(42)

dados_ruido = np.random.normal(0, 1, 300)

# Executando o teste até os lags 5 e 10
resultado_lb = acorr_ljungbox(
    dados_ruido,
    lags=[5, 10],
    return_df=True
)

print(resultado_lb)

# ###########
# O teste de Ljung-Box verifica se existe autocorrelação na série até determinados lags. 
# A hipótese nula considera que a série é um ruído branco. Se o p-value for maior que 0,05, 
# não rejeitamos essa hipótese, indicando que não há evidências suficientes de autocorrelação
###########