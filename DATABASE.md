# Base de Datos

## Fuente

Yahoo Finance vía API yfinance


## Universo

S&P 500 (primeros 50 componentes por orden alfabético del ticker)


## Periodo

1 ene 2020 — 31 dic 2024 (5 años)


## Frecuencia

Diaria (días hábiles bursátiles)


## Variables

Precio de cierre ajustado (Adjusted Close)


### Retorno logarítmico

\[
R_t=\ln\left(\frac{P_t}{P_{t-1}}\right)
\]

Se trabaja con retornos logarítmicos en lugar de precios por tres razones:

Estacionariedad — los precios tienen tendencia; los retornos son aproximadamente estacionarios.

Comparabilidad — elimina diferencias de escala entre activos.

Aditividad temporal — el retorno acumulado es la suma de retornos diarios.


## Limpieza

Activos eliminados por inicio tardío en mercado:

- Eliminación de ABNB por IPO(Oferta Pública Inicial) diciembre 2020
- Eliminación de APP por IPO 2021

La incorporación tardía de estos activos generaría un volumen significativo de valores faltantes al inicio de la serie, introduciendo sesgo en estimaciones de media, varianza y correlación.


## Número final de activos

48 acciones


## Observaciones por activo

~1,258 días hábiles


## Dimensión de la matriz de retornos

1,258 × 48

