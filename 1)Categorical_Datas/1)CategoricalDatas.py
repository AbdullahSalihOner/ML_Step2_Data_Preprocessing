from sklearn.preprocessing import LabelEncoder
import pandas as pd 

categrories = ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']
data = pd.DataFrame(categrories, columns=['renkler']) # Veri oluşturma 
label_encoder = LabelEncoder() # LabelEncoder nesnesi oluşturma

# kategorik verileri sayısal verilere dönüştürme
data['encoded'] = label_encoder.fit_transform(data['renkler']) # LabelEncoder'ı uygulama 


#%%


from sklearn.preprocessing import OneHotEncoder

categrories = ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']  
data1 = pd.DataFrame(categrories, columns=['renkler'])
ohe = OneHotEncoder(sparse=False) # OneHotEncoder nesnesi oluşturma
 
encoded_data = ohe.fit_transform(data1[['renkler']]) # OneHotEncoder'ı uygulama 
column_names = ohe.get_feature_names_out(input_features=['renkler']) # OneHotEncoder'dan sütun isimlerini almak 
encoded_df = pd.DataFrame(encoded_data, columns=column_names) # Dönüştürülen verileri bir DataFrame'e dönüştürme ve sütun isimlerini ayarlama

print(data1)

#%%

import pandas as pd
df = pd.DataFrame({'renk': ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']})
one_hot_encoded_df = pd.get_dummies(df, columns=['renk']) # get_dummies() fonksiyonunu kullanarak One-Hot Encoding uygulama
#get_dummies() fonksiyonu, kategorik verileri One-Hot Encoding'e dönüştürür
print(one_hot_encoded_df)


