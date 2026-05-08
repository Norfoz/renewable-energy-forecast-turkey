import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

DOSYA_ADI = "veri_seti.xlsx"

df = pd.read_excel(DOSYA_ADI)

print("Sütunlar:", list(df.columns))
print(df.head())


df["Yil"] = pd.to_numeric(df["Yil"], errors="coerce")
df["Yenilenebilir_Enerji_Orani"] = pd.to_numeric(df["Yenilenebilir_Enerji_Orani"], errors="coerce")
df["Kisi_Basi_GSYH"] = pd.to_numeric(df["Kisi_Basi_GSYH"], errors="coerce")
df["Kisi_Basi_Elektrik_Tuketimi"] = pd.to_numeric(df["Kisi_Basi_Elektrik_Tuketimi"], errors="coerce")

print("\nEksik değer sayıları:\n", df.isna().sum())

df = df.dropna()

print("Model Performansı:")

# 3 ADET GERÇEK VERİ GRAFİĞİ (Şekil 1-2-3)
# ================================
plt.figure()
plt.plot(df["Yil"], df["Yenilenebilir_Enerji_Orani"])
plt.xlabel("Yıl")
plt.ylabel("Yenilenebilir Enerji Oranı (%)")
plt.title("Türkiye'de Yenilenebilir Enerji Oranının Yıllara Göre Değişimi")
plt.show()

plt.figure()
plt.plot(df["Yil"], df["Kisi_Basi_GSYH"])
plt.xlabel("Yıl")
plt.ylabel("Kişi Başı GSYH (USD)")
plt.title("Türkiye'de Kişi Başı GSYH'nin Yıllara Göre Değişimi")
plt.show()

plt.figure()
plt.plot(df["Yil"], df["Kisi_Basi_Elektrik_Tuketimi"])
plt.xlabel("Yıl")
plt.ylabel("Kişi Başı Elektrik Tüketimi (kWh)")
plt.title("Türkiye'de Kişi Başı Elektrik Tüketiminin Yıllara Göre Değişimi")
plt.show()


# MODEL KUR (Çok değişkenli Linear Regression)
# ================================
X = df[["Yil", "Kisi_Basi_GSYH", "Kisi_Basi_Elektrik_Tuketimi"]]
y = df["Yenilenebilir_Enerji_Orani"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"\nModel Performansı -> R2: {r2:.4f} | RMSE: {rmse:.4f}")


# 2022–2030 İÇİN GİRDİLERİ ÜRET (trend varsayımı)
# ================================
years_future = np.arange(2022, 2031)

gsyh_growth = df["Kisi_Basi_GSYH"].diff().mean()
elec_growth = df["Kisi_Basi_Elektrik_Tuketimi"].diff().mean()

last_gsyh = df["Kisi_Basi_GSYH"].iloc[-1]
last_elec = df["Kisi_Basi_Elektrik_Tuketimi"].iloc[-1]

future_gsyh = [last_gsyh + i * gsyh_growth for i in range(1, len(years_future) + 1)]
future_elec = [last_elec + i * elec_growth for i in range(1, len(years_future) + 1)]

future_X = pd.DataFrame({
    "Yil": years_future,
    "Kisi_Basi_GSYH": future_gsyh,
    "Kisi_Basi_Elektrik_Tuketimi": future_elec
})

print("\n2022–2030 için oluşturulan tahmini girdiler:")
print(future_X)


# 2022–2030 YENİLENEBİLİR ENERJİ ORANI TAHMİNİ
# ================================
future_pred = model.predict(future_X)

tahmin_df = pd.DataFrame({
    "Yil": years_future,
    "Tahmini_Yenilenebilir_Enerji_Orani": future_pred
})

print("\n2022–2030 Tahmin Sonuçları:")
print(tahmin_df)

np.random.seed(42)

future_gsyh = np.array(future_gsyh) * (1 + np.random.normal(0, 0.02, len(future_gsyh)))
future_elec = np.array(future_elec) * (1 + np.random.normal(0, 0.015, len(future_elec)))

future_X = pd.DataFrame({
    "Yil": years_future,
    "Kisi_Basi_GSYH": future_gsyh,
    "Kisi_Basi_Elektrik_Tuketimi": future_elec
})

tahmin_df = pd.DataFrame({
    "Yil": years_future,
    "Tahmini_Yenilenebilir_Enerji_Orani": model.predict(future_X)
})


# GERÇEK + TAHMİN GRAFİĞİ (Şekil 4)
# ================================
plt.figure()
plt.plot(df["Yil"], df["Yenilenebilir_Enerji_Orani"], label="Gerçek Değerler (2005–2021)")
plt.plot(tahmin_df["Yil"], tahmin_df["Tahmini_Yenilenebilir_Enerji_Orani"],
         linestyle="--", label="Tahmin (2022–2030)")
plt.xlabel("Yıl")
plt.ylabel("Yenilenebilir Enerji Oranı (%)")
plt.title("Türkiye'de Yenilenebilir Enerji Oranı: Gerçek ve Tahmin")
plt.legend()
plt.show()