import pandas as pd

from utils import (
    calcular_retornos,
    matriz_correlacion
)

# Cargar datos
df = pd.read_csv(
    "data/raw/sp500_historico.csv",
    index_col=0,
    parse_dates=True
)

# Retornos
retornos = calcular_retornos(df)

# Correlaciones
corr = matriz_correlacion(retornos)

print(corr.head())