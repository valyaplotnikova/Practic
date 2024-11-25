import json

import requests
import pandas as pd
import matplotlib.pyplot as plt


weather_data = {
    'city': ['Москва', 'Санкт Петербург', 'Сочи', 'Нижний Новгород', 'Екатеринбург'],
    'weather': [],
    'temp': [],
    'humidity': [],
    'wind': []
}


for city in weather_data['city']:
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+
                        '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')
    data = response.json()
    weather_data['weather'].append(data['weather'][0]['description'])
    weather_data['temp'].append(data['main']['temp'])
    weather_data['humidity'].append(data['main']['humidity'])
    weather_data['wind'].append(data['wind']['speed'])

with open('weather.json', 'w') as file:
    file.write(json.dumps(weather_data))

df = pd.DataFrame(weather_data)
df.to_excel('weather.xlsx', index=False)


df = pd.read_excel('weather.xlsx', sheet_name='Sheet1')

print(df.head(3))
mean_value = df['temp'].mean()
print(f"Среднее значение температуры по городам: {mean_value}")

plt.figure(figsize=(10, 6))
plt.bar(df['city'], df['temp'])
plt.xlabel('Город')
plt.ylabel('Температура (°C)')
plt.title('Температура по городам')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['city'], df['humidity'])
plt.xlabel('Город')
plt.ylabel('Влажность (%)')
plt.title('Влажность по городам')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['city'], df['wind'])
plt.xlabel('Город')
plt.ylabel('Скорость ветра (м/с)')
plt.title('Скорость ветра по городам')
plt.show()
