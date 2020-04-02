import requests
from bs4 import BeautifulSoup
import dialogs
import json
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = "https://www.pref.wakayama.lg.jp/prefg/000200/covid19.html"
url2 = 'https://corona-stats.online/Japan?format=json'

r = requests.get(url, headers=headers)
r2 = requests.get(url2, headers=headers)

jdata = json.loads(r2.text)
soup = BeautifulSoup(r.content, "html.parser")

tables = soup.findAll("table")[1]
rows = tables.findAll("tr")[2]

corona_val_list = list()

for i, val in enumerate(rows.findAll("td")):
    corona_val_list.append(int(val.text))

pref_data = "和歌山" #+ soup.select("#content > div > h5:nth-child(13) > strong")[0].text
positive = "現在陽性の方：" + str(corona_val_list[0])
infected = "新規感染者：" + str(corona_val_list[-2])
total = "累計：" +  str(corona_val_list[-1])

jp_data = '日本'
jp_positive = '現在陽性の方：' + str(jdata['data'][0]['active'])
jp_infected = "新規感染者：" + str(jdata['data'][0]['todayCases'])
jp_total = "累計：" + str(jdata['data'][0]['cases'])

dtext = jp_data+'\n\n'+jp_positive+'\n'+jp_infected+'\n'+jp_total+'\n\n'
dtext2 = pref_data+'\n\n'+positive+'\n'+infected+'\n'+total

text = dtext+dtext2
now = datetime.datetime.now()

dialogs.text_dialog(
	title='COVID-19 '+str(now.month)+'/'+str(now.day),
  text = text
  )
