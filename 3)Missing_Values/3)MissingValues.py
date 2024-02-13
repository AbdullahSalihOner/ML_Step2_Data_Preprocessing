import pandas as pd
import numpy as np  

# Veri setini okuyalım
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [5, np.nan, np.nan, 8, 10],
        'C': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

print("Orjinal Veri: \n", df)

# A ve B sütunlarındaki eksik değerleri ortalama ile dolduralım
df['A'].fillna(df['A'].mean(), inplace=True) # inplace=True ile df üzerinde değişiklik yapmış oluyoruz
df['B'].fillna(df['B'].mean(), inplace=True)

#yeniden yazdıralım
print("Ortalama ile doldurulmuş veri: \n", df)

#%% Eksik verileri median ile doldurma  
df['A'].fillna(df['A'].median(), inplace=True) 
print("Median ile doldurulmuş veri: \n", df)

#%% Eksik verileri mod ile doldurma
df['A'].fillna(df['A'].mode()[0], inplace=True)
print("Mod ile doldurulmuş veri: \n", df)

#%% Önceki ve Sonraki Değerler ile Doldurma

# Önceki değer ile doldurma
df['A'].fillna(method='ffill', inplace=True)
print("Önceki değer ile doldurulmuş veri: \n", df)

# Sonraki değer ile doldurma
df['A'].fillna(method='bfill', inplace=True)
