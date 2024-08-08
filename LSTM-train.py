import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Veri setini yükleme
df = pd.read_csv('/Users/onur/JupyterLab-Projects/AI/Turkcell/5yearweatherdata.csv')

# Zaman damgasından saat, gün ve ay bilgilerini çıkarma
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['day'] = pd.to_datetime(df['timestamp']).dt.day
df['month'] = pd.to_datetime(df['timestamp']).dt.month

# Şehir, hava durumu ve mevsim sütunlarını kategorik değişkenlere dönüştürme
df = pd.get_dummies(df, columns=['city', 'weather', 'season'], drop_first=True)

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

window_size = 72  # Geçmiş 24 saati kullanmak
X, y = create_sequences(scaled_data, temperature, window_size)

# Veriyi eğitim ve test olarak ayırma
split = int(0.9 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# LSTM Modeli Oluşturma
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=50))
model.add(Dense(1))

# Modeli Derleme
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.004), loss='mean_squared_error')

# Modeli Eğitme
model.fit(X_train, y_train, epochs=30, batch_size=64, validation_data=(X_test, y_test))

# Tahminler ve Değerlendirme
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
