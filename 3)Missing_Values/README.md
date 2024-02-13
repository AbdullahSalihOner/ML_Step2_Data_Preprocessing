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
