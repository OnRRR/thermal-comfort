import pandas as pd
import numpy as np

# Şehirler ve mevsimlere göre hava durumu ve sıcaklık aralıkları
city_weather_conditions = {
    'Istanbul': {
        'winter': {'temp_range': (0, 10), 'weather': ['clear', 'cloudy', 'rainy', 'snowy', 'stormy']},
        'spring': {'temp_range': (10, 20), 'weather': ['clear', 'cloudy', 'rainy']},
        'summer': {'temp_range': (20, 30), 'weather': ['clear', 'cloudy', 'rainy']},
        'autumn': {'temp_range': (10, 20), 'weather': ['clear', 'cloudy', 'rainy', 'stormy']}
    },
    'Ankara': {
        'winter': {'temp_range': (-5, 5), 'weather': ['clear', 'cloudy', 'snowy']},
        'spring': {'temp_range': (5, 15), 'weather': ['clear', 'cloudy', 'rainy']},
        'summer': {'temp_range': (15, 30), 'weather': ['clear', 'cloudy']},
        'autumn': {'temp_range': (5, 15), 'weather': ['clear', 'cloudy', 'rainy']}
    },
    'Izmir': {
        'winter': {'temp_range': (5, 15), 'weather': ['clear', 'cloudy', 'rainy']},
        'spring': {'temp_range': (15, 25), 'weather': ['clear', 'cloudy', 'rainy']},
        'summer': {'temp_range': (25, 35), 'weather': ['clear', 'cloudy']},
        'autumn': {'temp_range': (15, 25), 'weather': ['clear', 'cloudy', 'rainy']}
    },
    'Bursa': {
        'winter': {'temp_range': (0, 10), 'weather': ['clear', 'cloudy', 'rainy', 'snowy']},
        'spring': {'temp_range': (10, 20), 'weather': ['clear', 'cloudy', 'rainy']},
        'summer': {'temp_range': (20, 35), 'weather': ['clear', 'cloudy', 'rainy']},
        'autumn': {'temp_range': (10, 20), 'weather': ['clear', 'cloudy', 'rainy']}
    },
    'Adana': {
        'winter': {'temp_range': (10, 20), 'weather': ['clear', 'cloudy', 'rainy']},
        'spring': {'temp_range': (20, 30), 'weather': ['clear', 'cloudy', 'rainy']},
        'summer': {'temp_range': (30, 42), 'weather': ['clear', 'cloudy']},
        'autumn': {'temp_range': (20, 30), 'weather': ['clear', 'cloudy', 'rainy']}
    }
}


def get_hourly_temperature(base_temp, hour):
    """
    Günün saatine göre sıcaklık varyasyonu.
    11:00 - 16:00 saatleri arası en sıcak saatlerdir.
    00:00 - 06:00 saatleri arası en soğuk saatlerdir.
    """
    if 11 <= hour <= 16:
        return base_temp + np.random.uniform(3, 7)  # En sıcak saatler
    elif 0 <= hour <= 6:
        return base_temp - np.random.uniform(3, 7)  # En soğuk saatler
    else:
        return base_temp  # Diğer saatler


def get_humidity(weather_condition):
    """
    Hava durumuna göre nem oranını belirler.
    """
    if weather_condition == 'clear':
        return np.random.uniform(20, 50)
    elif weather_condition == 'cloudy':
        return np.random.uniform(40, 70)
    elif weather_condition == 'rainy':
        return np.random.uniform(70, 100)
    elif weather_condition == 'snowy':
        return np.random.uniform(70, 100)
    elif weather_condition == 'stormy':
        return np.random.uniform(80, 100)


def get_season(month):
    """
    Ay bilgisine göre mevsimi belirler.
    """
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:
        return 'autumn'


def generate_weather_data(start_hour, num_hours, start_date):
    data = []
    for hour in range(start_hour, start_hour + num_hours):
        for city, conditions in city_weather_conditions.items():
            timestamp = start_date + pd.Timedelta(hours=hour)
            month = timestamp.month
            season = get_season(month)

            condition_options = conditions[season]
            condition = np.random.choice(condition_options['weather'])
            base_temp = np.random.uniform(*condition_options['temp_range'])
            hour_of_day = hour % 24
            temp = get_hourly_temperature(base_temp, hour_of_day)
            humidity = get_humidity(condition)

            data.append({
                'city': city,
                'temperature': round(temp, 2),
                'humidity': round(humidity, 2),
                'weather': condition,
                'season': season,
                'timestamp': timestamp
            })

    return pd.DataFrame(data)


# 5 yıl için veri üretme (5 yıl * 365 gün * 24 saat)
num_hours = 5 * 365 * 24
batch_size = 24 * 30  # Aylık veri parçası
num_batches = num_hours // batch_size
start_date = pd.Timestamp('2018-01-01')

for batch in range(num_batches):
    df = generate_weather_data(batch * batch_size, batch_size, start_date)
    if batch == 0:
        df.to_csv('5_year_weather_data.csv', index=False)
    else:
        df.to_csv('5_year_weather_data.csv', mode='a', header=False, index=False)

# Veriyi kontrol etme
df = pd.read_csv('5_year_weather_data.csv')
print(df.head())
print(df.tail())
