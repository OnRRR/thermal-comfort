import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veri setini yükleme
df = pd.read_csv('/Users/onur/JupyterLab-Projects/AI/Turkcell/5yearweatherdata.csv')

# Zaman damgasından saat, gün ve ay bilgilerini çıkarma
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['day'] = pd.to_datetime(df['timestamp']).dt.day
df['month'] = pd.to_datetime(df['timestamp']).dt.month

# Şehir, hava durumu ve mevsim sütunlarını kategorik değişkenlere dönüştürme
df = pd.get_dummies(df, columns=['city', 'weather', 'season'], drop_first=True)

# 'timestamp' sütununu çıkarma
df = df.drop(columns=['timestamp'])

# Korelasyon matrisi oluşturma
corr_matrix = df.corr()

# Sıcaklık ile diğer özellikler arasındaki korelasyonu seçme
corr_with_temp = corr_matrix['temperature'].sort_values(ascending=False)

print("Sıcaklık ile özellikler arasındaki korelasyon:")
print(corr_with_temp)

# Korelasyon matrisini görselleştirme
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Korelasyon Matrisi Isı Haritası')
plt.show()
