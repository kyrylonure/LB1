import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


current_date = datetime.now()
week_ago_date = current_date - timedelta(days=7)


todayDate = current_date.strftime('%Y%m%d')
lastWeekDate = week_ago_date.strftime('%Y%m%d')

print(todayDate, lastWeekDate)


url = (
    f"https://bank.gov.ua/NBU_Exchange/exchange_site"
    f"?start={lastWeekDate}&end={todayDate}&valcode=usd&json"
)
print(url)


response = requests.get(url)
data = json.loads(response.text)


exchange_data = {entry['exchangedate']: entry['rate'] for entry in data}


plt.figure(figsize=(10, 5))
plt.plot(exchange_data.keys(), exchange_data.values(), marker='o', linestyle='-')
plt.title("Динаміка курсу USD")
plt.xlabel("Дата")
plt.ylabel("Курс (UAH)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
