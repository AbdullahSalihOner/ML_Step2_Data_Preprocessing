from sklearn.preprocessing import MinMaxScaler,StandardScaler
import numpy as np

data = np.array([[1.0, 2.0],
                 [4.0, 5.0],
                 [700.0, 800.0]])



#Normalizasyon yaptık
scaler_minmax = MinMaxScaler()
data_normalized = scaler_minmax.fit_transform(data)

#Standartlaştırma yapıyoruz
scaler_standard = StandardScaler()
data_standardized = scaler_standard.fit_transform(data)

# Sonuçları yazdıralım
print("Orjinal Veri:")
print(data)
print("Normalizasyon Sonrası Veri:")
print(data_normalized)
print("Standartlaştırma Sonrası Veri:")
print(data_standardized)