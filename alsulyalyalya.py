print('Курсы валют по ЦР РФ')
import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
print ('Доллар -', data['Valute']['USD']['Value'], 'Рублей')
print ('Евро -', data['Valute']['EUR']['Value'], 'Рублей')
s = int(input())
print("ввели число", (s))
print('Доллар -', round(s*data['Valute']['USD']['Value']), 'рублей')
print('Евро -', round(s*data['Valute']['EUR']['Value']), 'рублей')

print('За 1 Рубль-', round(s/data['Valute']['USD']['Value']), 'Долларов')
print('За 1 Рубль -', round(s/data['Valute']['EUR']['Value']),'Евро')























