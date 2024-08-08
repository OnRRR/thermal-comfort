import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Veri setini yükleme
df = pd.read_csv('/Users/onur/JupyterLab-Projects/AI/Turkcell/5yearweatherdata.csv')

# Zaman damgasından saat, gün ve ay bilgilerini çıkarma
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['day'] = pd.to_datetime(df['timestamp']).dt.day
df['month'] = pd.to_datetime(df['timestamp']).dt.month

# Zaman damgası ve şehir bilgilerini birleştirerek benzersiz zaman serisi indeksleri oluşturma
#df['timestamp_city'] = df['timestamp'].astype(str) + '_' + df['city']

# Bu yeni sütunu zaman serisi indeks olarak kullanarak verileri sıralama
df = df.sort_values(by='timestamp')

# Şehir, hava durumu ve mevsim sütunlarını kategorik değişkenlere dönüştürme
df = pd.get_dummies(df, columns=['city', 'weather', 'season'], drop_first=False)

# Sıcaklık sütununu çıkarma ve özellikleri ayırma
temperature = df['temperature'].values
df = df.drop(['timestamp', 'temperature'], axis=1)

# Veriyi ölçeklendirme
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

# Zaman serisi veri hazırlığı
def create_sequences(data, temp, window_size):
    X, y = [], []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i])
        y.append(temp[i])
    return np.array(X), np.array(y)

window_size = 72  # Geçmiş 72 saati kullanmak
X, y = create_sequences(scaled_data, temperature, window_size)

# Veriyi eğitim ve test olarak ayırma
split = int(0.9 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# LSTM Modeli Oluşturma
model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=64))
model.add(Dense(1))

# Modeli Derleme
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.005), loss='mean_squared_error')

# Modeli Eğitme
model.fit(X_train, y_train, epochs=40, batch_size=64, validation_data=(X_test, y_test))

# Tahminler ve Değerlendirme
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')

# Gerçek ve Tahmin Edilen Sıcaklıkları Karşılaştırma Grafiği
plt.figure(figsize=(14, 7))
plt.plot(y_test, label='Gerçek Sıcaklık', color='blue')  # Gerçek sıcaklık için mavi renk
plt.plot(y_pred, label='Tahmin Edilen Sıcaklık', color='red')  # Tahmin edilen sıcaklık için kırmızı renk
plt.xlabel('Zaman Adımı')
plt.ylabel('Sıcaklık')
plt.title('Gerçek vs. Tahmin Edilen Sıcaklıklar')
plt.legend()
plt.show()
