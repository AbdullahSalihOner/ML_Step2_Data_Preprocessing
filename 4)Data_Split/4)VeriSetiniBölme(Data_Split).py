import pandas as pd
import numpy as np
import skleran.model_selection import train_test_split 

# Seed değeri ; aynı sonuçları elde etmek için kullanılır, her zaman aynı sonuçları elde etmek istiyorsak aynı seed değerini kullanmalıyız
np.random.seed(0)

boy = np.random.normal(170, 10, 30) # ortalama 170cm, standart sapma 10cm, 30 adet değer üret
kilo = np.random.normal(70, 15, 30) # ortalama 70kg, standart sapma 15kg, 30 adet değer üret

data = pd.DataFrame({'Boy':boy, 'Kilo':kilo})

print("Orjinal Veri: \n", data.head())

x = data[['Boy']] # bağımsız değişken
y = data['Kilo'] # bağımlı değişken

# Veri setini eğitim ve test verisi olarak ayıralım
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=42)

print("Eğitim Verisi: \n", x_train.head())
print("Test Verisi: \n", x_test.head())

print("\n Eğitim Verisi Boyutu: ", x_train.shape)
print("\n Test Verisi Boyutu: ", x_test.shape)