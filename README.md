<<<<<<< HEAD
# Análisis Financiero de Acciones del S&P 500

## Descripción

Este proyecto aplica técnicas estadísticas y de aprendizaje no supervisado
para analizar el comportamiento de 48 acciones del índice S&P 500 durante
el periodo 2020–2024. El análisis parte de precios de cierre ajustados
descargados desde Yahoo Finance y trabaja sobre retornos logarítmicos
diarios para garantizar estacionariedad y comparabilidad entre activos.

## Objetivos

1. Analizar la distribución de retornos y detectar desviaciones de la normalidad.
2. Estudiar la estructura de dependencia entre activos mediante correlaciones de Pearson.
3. Identificar grupos de acciones con comportamiento similar usando clustering.
4. Evaluar oportunidades de diversificación de portafolio a partir del agrupamiento sectorial.

## Técnicas utilizadas

| Técnica | Propósito |

| Retornos logarítmicos | Transformación para estacionariedad y comparabilidad |
| Estandarización (StandardScaler) | Normalización de escala previa al clustering |
| KDE + distribución normal ajustada | Análisis de distribución y detección de colas pesadas |
| Correlación de Pearson + heatmaps | Estructura de dependencia entre activos por ventanas temporales |
| K-Means (k=4) + método del codo | Agrupamiento de activos por perfil de retorno-riesgo |
| Clustering jerárquico (Ward) + dendrograma | Validación visual del agrupamiento |
| PCA (2 componentes) | Reducción de dimensionalidad y visualización de clusters |
| Detección de atípicos (KDE gaussiana) | Identificación de retornos extremos por activo |

## Estructura del proyecto
├── main.py               # Flujo principal del análisis
├── utils.py              # Funciones auxiliares
├── requirements.txt      # Dependencias
├── DATABASE.md           # Descripción de la base de datos y limpieza
├── WORKFLOW.md           # Metodología paso a paso
└── sp500_historico.csv   # Datos de precios de cierre (generado al ejecutar)

## Datos

- **Fuente:** Yahoo Finance vía `yfinance`
- **Universo:** Primeros 50 componentes del S&P 500 (orden alfabético por ticker)
- **Periodo:** 1 enero 2020 — 31 diciembre 2024
- **Frecuencia:** Diaria (días hábiles bursátiles)
- **Activos finales:** 48 acciones (~1,258 observaciones por activo)
- **Exclusiones:** ABNB y APP por inicio tardío en mercado

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Requisitos principales

- Python ≥ 3.9
- yfinance
- pandas
- numpy
- scikit-learn
- scipy
- seaborn
- matplotlib
- statsmodels
=======
