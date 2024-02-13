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
