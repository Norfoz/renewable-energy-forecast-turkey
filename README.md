# Renewable Energy Forecast — Turkey (2005–2030)

Predicting Turkey's renewable energy ratio using multivariate Linear Regression
with real historical data (2005–2021) and forecasting through 2030.

## Overview

This project analyzes Turkey's renewable energy trends using three key indicators
and builds a machine learning model to forecast future ratios.

## Dataset Features

| Feature | Description |
|---|---|
| `Yil` | Year (2005–2021) |
| `Yenilenebilir_Enerji_Orani` | Renewable energy ratio (%) |
| `Kisi_Basi_GSYH` | GDP per capita (USD) |
| `Kisi_Basi_Elektrik_Tuketimi` | Electricity consumption per capita (kWh) |

## Model

- **Algorithm:** Multivariate Linear Regression
- **Libraries:** scikit-learn, pandas, numpy, matplotlib
- **Input:** Year, GDP per capita, electricity consumption
- **Output:** Renewable energy ratio (%)

## Results

![Forecast](yenilenebilir_enerji_tahmini_GercekvsTahmin.png)

## How to Run

```bash
pip install numpy pandas matplotlib scikit-learn openpyxl
python kod_dosyasi.py
```

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
