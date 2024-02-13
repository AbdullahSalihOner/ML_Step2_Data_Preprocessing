<h1>MachineLearning_Step2_Data_Preprocessing</h1>


# DATA PREPROCESSING

[### 1)CATEGORICAL DATAS](./1)Categorical_Datas)


1.LabelEncoder

LabelEncoder, veri setindeki kategorik (kategori) değerleri sayısal değerlere dönüştürmek için kullanılan bir sınıftır. Bu, makine öğrenimi algoritmalarının kategorik verilerle çalışabilmesini sağlar.

LabelEncoder'ı kullanmak için öncelikle `sklearn.preprocessing` modülünü içe aktarmamız gerekmektedir. Ardından, bir LabelEncoder nesnesi oluşturarak veri setimizi dönüştürebiliriz.

İşte bir örnek:

```python
from sklearn.preprocessing import LabelEncoder

# Örnek veri seti
categories = ['kırmızı', 'mavi', 'yeşil', 'kırmızı', 'sarı']

# LabelEncoder nesnesi oluşturma
encoder = LabelEncoder()

# Kategorik değerleri dönüştürme
encoded_categories = encoder.fit_transform(categories)

print(encoded_categories)

```

Bu kodda, `categories` listesi içindeki kategorik değerlerin her biri bir sayısal değere dönüştürülür. Çıktı olarak, dönüştürülmüş kategorik değerlerin bir listesi elde edilir:

```
[1 0 2 1 3]

```

LabelEncoder, kategorik değerleri alfabetik sıraya göre sıralayarak dönüştürür. Yani, 'kırmızı' değeri 1'e, 'mavi' değeri 0'a, 'yeşil' değeri 2'ye ve 'sarı' değeri 3'e dönüştürülür.

Dönüştürme işleminden sonra, elde edilen sayısal değerler makine öğrenimi algoritmalarında kullanılabilir. Örneğin, bu dönüştürülmüş verileri bir sınıflandırma algoritmasıyla eğitebilirsiniz.

LabelEncoder'ın dikkate alınması gereken bir noktası, dönüştürme işlemi sırasında kategorik değerlerin sıralamasının önemli olmasıdır. Eğer kategorik değerlerin sıralaması önemli değilse, One-Hot Encoding gibi diğer dönüştürme yöntemlerini kullanmanız daha uygun olabilir.

2.OneHotEncoder

OneHotEncoder, her bir kategorik özelliği ayrı bir sütun olarak temsil eden bir kodlama yapısı oluşturur. Bu kodlama yapısı, her bir kategori değeri için 0 veya 1 değerlerini içeren bir vektör olarak ifade edilir. Bu sayede, kategorik verilerin sayısal formata dönüştürülmesi sağlanır.

Örneğin, bir veri setinde "renk" adında bir kategorik özelliğimiz olsun ve bu özellik "kırmızı", "mavi" ve "yeşil" gibi üç farklı kategori değerine sahip olsun. OneHotEncoder kullanarak bu özelliği dönüştürdüğümüzde, "renk_kırmızı", "renk_mavi" ve "renk_yeşil" gibi üç ayrı sütun oluşturulur. Her bir sütun, ilgili kategori değerine ait örnekler için 0 veya 1 değerlerini içerir.

OneHotEncoder'ın kullanımı genellikle veri ön işleme aşamasında gerçekleştirilir. Bu dönüşüm, kategorik verilerin makine öğrenimi algoritmalarına giriş olarak kullanılabilmesini sağlar.

```python
from sklearn.preprocessing import OneHotEncoder

categrories = ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']  
data1 = pd.DataFrame(categrories, columns=['renkler'])
ohe = OneHotEncoder(sparse=False) # OneHotEncoder nesnesi oluşturma
 
# OneHotEncoder'ı uygulama 
encoded_data = ohe.fit_transform(data1[['renkler']]) 
# OneHotEncoder'dan sütun isimlerini almak 
column_names = ohe.get_feature_names_out(input_features=['renkler']) 
# Dönüştürülen verileri bir DataFrame'e dönüştürme ve sütun isimlerini ayarlama
encoded_df = pd.DataFrame(encoded_data, columns=column_names) 

print(data1)
```

3.get_dummies()

`get_dummies()` fonksiyonu, kategorik verileri içeren bir veri kümesini alır ve bu kategorik verileri sayısal değerlere dönüştürür. Bu dönüşüm, kategorik verilerin her bir benzersiz değeri için yeni bir sütun oluşturarak gerçekleştirilir. Bu yeni sütunlar, kategorik verinin her bir değeri için 1 veya 0 değerlerini alır.

Örneğin, bir veri kümesinde "renk" adında bir kategorik sütununuz olduğunu düşünelim ve bu sütunun değerleri "kırmızı", "mavi" ve "yeşil" olsun. `get_dummies()` fonksiyonunu kullanarak bu sütunu dönüştürebilirsiniz. Sonuç olarak, "renk_kırmızı", "renk_mavi" ve "renk_yeşil" adında üç yeni sütun oluşturulur. Her bir sütun, ilgili renk değerine sahip olan satırlar için 1 değerini alırken, diğer satırlar için 0 değerini alır.

Bu dönüşüm, makine öğrenimi modelleri gibi sayısal veri gerektiren algoritmalarla çalışırken faydalı olabilir. Kategorik verileri sayısal değerlere dönüştürerek, bu verileri modelin anlayabileceği bir formata getirmiş olursunuz.

`get_dummies()` fonksiyonu, pandas kütüphanesinin bir parçasıdır ve pandas DataFrame nesneleri üzerinde kullanılabilir. Fonksiyon, varsayılan olarak tüm kategorik sütunları dönüştürür, ancak belirli sütunları da seçmek için parametreler kullanılabilir. Ayrıca, dönüşüm sonucunda oluşan sütunların isimlerini özelleştirmek için de parametreler sağlanabilir.

Özetlemek gerekirse, `get_dummies()` fonksiyonu, kategorik verileri sayısal değerlere dönüştürmek için kullanılan bir fonksiyondur ve pandas kütüphanesinin bir parçasıdır. Bu dönüşüm, her bir kategorik değer için yeni sütunlar oluşturarak gerçekleştirilir.

```python
import pandas as pd
df = pd.DataFrame({'renk': ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']})
one_hot_encoded_df = pd.get_dummies(df, columns=['renk']) # get_dummies() fonksiyonunu kullanarak One-Hot Encoding uygulama
#get_dummies() fonksiyonu, kategorik verileri One-Hot Encoding'e dönüştürür
print(one_hot_encoded_df)
```

## 2)DATA SCALING(Ölçeklendirme)

1.MinMaxScaler(Normalizasyon)

MinMaxScaler, bir özellik ölçeklendirme tekniği olan Min-Max Normalleştirme'yi uygulayan bir sınıftır. Bu teknik, veri setindeki tüm özelliklerin değerlerini belirli bir aralığa (genellikle 0 ile 1 arasında) ölçeklendirir. Bu, özellikler arasındaki potansiyel ölçek farklılıklarını giderir ve algoritmanın daha iyi performans göstermesine yardımcı olabilir.

MinMaxScaler'ı kullanmak için öncelikle `sklearn.preprocessing` modülünü içe aktarmamız gerekmektedir. Ardından, bir MinMaxScaler nesnesi oluşturarak veri setimizi ölçeklendirebiliriz.

İşte bir örnek:

```python
from sklearn.preprocessing import MinMaxScaler

# Örnek veri seti
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]

# MinMaxScaler nesnesi oluşturma
scaler = MinMaxScaler()

# Veri setini ölçeklendirme
scaled_data = scaler.fit_transform(data)

print(scaled_data)

```

Bu kodda, `data` listesi içindeki değerler MinMaxScaler kullanılarak 0 ile 1 arasında ölçeklendirilir. Çıktı olarak, ölçeklendirilmiş değerlerin bir listesi elde edilir:

```
[[0.   0.  ]
 [0.25 0.25]
 [0.5  0.5 ]
 [1.   1.  ]]

```

MinMaxScaler, özellikle veri setindeki özelliklerin değerlerinin çok farklı ölçeklere sahip olduğu durumlarda kullanışlıdır. Bu ölçeklendirme tekniği, özellikler arasındaki bu ölçek farklılıklarını giderir ve algoritmanın daha iyi performans göstermesine yardımcı olabilir. Ancak, MinMaxScaler'ın dikkate alınması gereken bir noktası, veri setindeki aykırı değerlerin ölçeklendirme sonucunu büyük ölçüde etkileyebileceğidir. Bu nedenle, MinMaxScaler kullanmadan önce aykırı değerlerin nasıl işleneceğine karar vermek önemlidir.

2.StandartScaler(**Standardizasyon)**

`StandardScaler`, bir özellik ölçeklendirme tekniği olan Standartlaştırma'yı uygulayan bir sınıftır. Bu teknik, veri setindeki tüm özelliklerin değerlerini, özelliklerin ortalamasının 0 ve standart sapmasının 1 olacak şekilde ölçeklendirir. Bu, özellikler arasındaki potansiyel ölçek farklılıklarını giderir ve algoritmanın daha iyi performans göstermesine yardımcı olabilir.

`StandardScaler`'ı kullanmak için öncelikle `sklearn.preprocessing` modülünü içe aktarmamız gerekmektedir. Ardından, bir `StandardScaler` nesnesi oluşturarak veri setimizi ölçeklendirebiliriz.

İşte bir örnek:

```python
from sklearn.preprocessing import StandardScaler

# Örnek veri seti
data = [[0, 0], [0, 0], [1, 1], [1, 1]]

# StandardScaler nesnesi oluşturma
scaler = StandardScaler()

# Veri setini ölçeklendirme
scaled_data = scaler.fit_transform(data)

print(scaled_data)

```

Bu kodda, `data` listesi içindeki değerler `StandardScaler` kullanılarak standartlaştırılır. Çıktı olarak, standartlaştırılmış değerlerin bir listesi elde edilir:

```
[[-1. -1.]
 [-1. -1.]
 [ 1.  1.]
 [ 1.  1.]]

```

`StandardScaler`, özellikle veri setindeki özelliklerin değerlerinin çok farklı ölçeklere sahip olduğu durumlarda kullanışlıdır. Bu ölçeklendirme tekniği, özellikler arasındaki bu ölçek farklılıklarını giderir ve algoritmanın daha iyi performans göstermesine yardımcı olabilir. Ancak, `StandardScaler`'ın dikkate alınması gereken bir noktası, veri setindeki aykırı değerlerin ölçeklendirme sonucunu büyük ölçüde etkileyebileceğidir. Bu nedenle, `StandardScaler` kullanmadan önce aykırı değerlerin nasıl işleneceğine karar vermek önemlidir.

## 3)MISSING VALUES

**`fillna`** metodu, pandas kütüphanesinde bulunan ve eksik verileri (genellikle NaN olarak gösterilir) doldurmak için kullanılan bir fonksiyondur. Bu metod, çeşitli parametrelerle kullanılarak eksik verileri farklı yollarla doldurmanıza olanak tanır. İşte en yaygın kullanılan eksik veri doldurma yöntemleri:

### **Ortalama ile Doldurma (Mean Imputation)**

- **Nasıl Çalışır?**: Eksik değerler, o sütundaki diğer değerlerin ortalaması ile doldurulur.
- **Kullanımı**: **`dataframe['column'].fillna(dataframe['column'].mean(), inplace=True)`**
- **Uygulama Alanı**: Sayısal veriler için uygundur, ancak aykırı değerlerin etkisi altında kalabilir.

### **Mod ile Doldurma (Mode Imputation)**

- **Nasıl Çalışır?**: Eksik değerler, o sütundaki en sık rastlanan değer (mod) ile doldurulur.
- **Kullanımı**: **`dataframe['column'].fillna(dataframe['column'].mode()[0], inplace=True)`**
- **Uygulama Alanı**: Kategorik veriler için idealdir.

### **Medyan ile Doldurma (Median Imputation)**

- **Nasıl Çalışır?**: Eksik değerler, o sütundaki medyan değeri (orta değer) ile doldurulur.
- **Kullanımı**: **`dataframe['column'].fillna(dataframe['column'].median(), inplace=True)`**
- **Uygulama Alanı**: Sayısal veriler için uygundur, özellikle aykırı değerlerin ortalama üzerinde büyük etkisi olduğu durumlarda tercih edilir.

### **Önceki Değer ile Doldurma (Forward Fill)**

- **Nasıl Çalışır?**: Eksik değer, hemen önceki satırdaki değer ile doldurulur.
- **Kullanımı**: **`dataframe['column'].fillna(method='ffill', inplace=True)`**
- **Uygulama Alanı**: Zaman serisi verilerinde veya sıralı verilerde kullanışlıdır.

### **Sonraki Değer ile Doldurma (Backward Fill)**

- **Nasıl Çalışır?**: Eksik değer, hemen sonraki satırdaki değer ile doldurulur.
- **Kullanımı**: **`dataframe['column'].fillna(method='bfill', inplace=True)`**
- **Uygulama Alanı**: Zaman serisi verilerinde veya sıralı verilerde kullanışlıdır.

Her bir yöntemin etkinliği, veri setinizin yapısına ve eksik verilerin doğasına bağlıdır. Ayrıca, eksik veri doldurma işlemleri yaparken veri setinizin gerçek dağılımını değiştirebileceğinizi ve bu nedenle modelinizin performansını etkileyebileceğinizi unutmamak önemlidir. Bu yüzden, hangi yöntemin kullanılacağına karar verirken veri setinin özelliklerini ve eksik verilerin potansiyel etkilerini dikkate almak önemlidir.

## 4)DATA SPLIT

`train_test_split` fonksiyonu, veri setini eğitim ve test setlerine ayırmak için kullanılır. Bu, makine öğrenmesi modellerini eğitmek ve değerlendirmek için genellikle kullanılan bir tekniktir.

`train_test_split` fonksiyonu, `sklearn.model_selection` modülünün bir parçasıdır. Fonksiyon, ilk olarak veri setini alır ve belirtilen oranlarda rastgele eğitim ve test setlerine ayırır. Varsayılan olarak, veri setinin %75'i eğitim seti ve %25'i test seti olacak şekilde ayrılır.

İşte bir örnek:

```python
from sklearn.model_selection import train_test_split

# Örnek veri seti
X = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
y = [0, 1, 2, 3, 4]

# Veri setini eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)

```

Bu kodda, `X` ve `y` listeleri `train_test_split` fonksiyonuna verilir ve veri seti, %80'i eğitim seti ve %20'si test seti olacak şekilde ayrılır. Çıktı olarak, eğitim ve test setlerine ayrılmış `X` ve `y` değerlerinin listeleri elde edilir.

`train_test_split` fonksiyonu, modelin genelleme yeteneğini değerlendirmek için kullanılır. Model, eğitim seti üzerinde eğitilir ve test seti üzerinde test edilir. Bu, modelin görmediği veriler üzerinde nasıl performans gösterdiğini görmemizi sağlar, bu da modelin gerçek dünya verileri üzerinde nasıl performans göstereceği hakkında bir fikir verir.
