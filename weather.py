import requests

# API ключ от OpenWeatherMap.
app_id = '36ab184f139b00c86012421e4ebc8179'

# Ввод названия города.
city_name = input("\nВведите название города: ")

# Получение всех предоставляемых данных о городе.
getting_all_data_about_city = requests.get("http://api.openweathermap.org/data/2.5/find", params={
	'q': city_name,
	'units': 'metric',
	'APPID': app_id
})

# Превращение полученных данных о городе в формат json.
city_data_in_json_format = getting_all_data_about_city.json()['list']

for city_temperatures in city_data_in_json_format:
	temp_now_city = city_temperatures['main']['temp']
	temp_max_city = city_temperatures['main']['temp_max']
	temp_min_city = city_temperatures['main']['temp_min']

# Вывод данных о погоде.
print(f"\nПогода на данный момент: {temp_now_city}")
print(f"Минимальная погода: {temp_min_city}")
print(f"Максимальная погода: {temp_max_city}")