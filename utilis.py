import numpy as np
import pandas as pd

def calcular_retornos(df):
    """
    Calcula retornos logarítmicos.
    """
    retornos = np.log(df / df.shift(1))
    return retornos.dropna()


def estandarizar(df):
    """
    Estandariza columnas.
    """
    return (df - df.mean()) / df.std()


def matriz_correlacion(df):
    """
    Calcula matriz de correlaciones.
    """
    return df.corr()