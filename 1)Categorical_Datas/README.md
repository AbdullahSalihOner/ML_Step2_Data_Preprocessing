### 1)CATEGORICAL DATAS

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
