import datetime
import json
import pandas as pd
import requests

date1 = '2018-01-01'
date2 = '2018-02-01'

mydates = pd.date_range(date1, date2).tolist()

for s_date in mydates:
	#uri="https://lb.api.openprocurement.org/api/0/tenders?offset=" + s_date.strftime("%y-%m-%d")
	#uri="https://public.api.openprocurement.org/api/0/tenders?offset=" + s_date.strftime("%y-%m-%d")
  uri="https://public.api.openprocurement.org/api/0/tenders
	print(uri)
	response = requests.get(uri)
	result = json.loads(response.content)
	for row in result["data"]:
		print(row)
