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
