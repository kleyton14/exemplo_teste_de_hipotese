from scipy.stats import shapiro
import numpy as np

# Crie uma amostra aleatória de 50 pontos com distribuição normal
amostra = np.random.normal(size=50)

# Execute o teste de Shapiro-Wilk
stat, p = shapiro(amostra)

# Exibe o resultado
print('Estatística do teste de Shapiro-Wilk:', stat)
print('Valor p:', p)

# Interprete o resultado
alpha = 0.05
if p > alpha:
    print('Não podemos rejeitar a hipótese nula (amostra vem de uma distribuição normal)')
else:
    print('Rejeitamos a hipótese nula (amostra não vem de uma distribuição normal)')
