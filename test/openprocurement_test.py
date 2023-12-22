#!/usr/bin/env python

from datetime import datetime
import json
import pandas as pd
import requests

date1 = '2018-01-01'
date2 = '2018-02-01'

mydates = pd.date_range(date1, date2).tolist()

#uri="https://public.api.openprocurement.org/api/0/tenders"
uri="https://public.api.openprocurement.org/api/0/tenders/fd763950ebc14146aaaa168fd7a6c992"
# uri="https://public.api.openprocurement.org/api/2.5/tenders?offset=1434981607.443577"
# uri=f"https://public.api.openprocurement.org/api/0/tenders?offset={datetime.fromisoformat('2015-01-01T00:00:00+02:00').timestamp()}&descending=1&limit=10"
response = requests.get(uri)
#print(response.content)
json_object = json.loads(response.content)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)

# for s_date in mydates:
#     print(s_date.strftime("%y-%m-%d"))
    
	#uri="https://lb.api.openprocurement.org/api/0/tenders?offset=" + s_date.strftime("%y-%m-%d")
	#uri="https://public.api.openprocurement.org/api/0/tenders?offset=" + s_date.strftime("%y-%m-%d")
	#uri="https://public.api.openprocurement.org/api/0/tenders"
	#uri="https://public.api.openprocurement.org/api/0/tenders?offset=2015-01-01T00:00:00+02:00&descending=1&limit=10"
	#uri="https://public.api.openprocurement.org/api/2.5/tenders?offset=1420063200.0&limit=1&descending=1"
	#uri=f"https://public.api.openprocurement.org/api/0/tenders?offset={datetime.fromisoformat('2015-01-01T00:00:00+02:00').timestamp()}&descending=1&limit=10"
	# uri="https://public.api.openprocurement.org/api/2.5/tenders?offset=1434981607.443577"
	# response = requests.get(uri)
	# #print(response.content)
	# json_object = json.loads(response.content)
	# json_formatted_str = json.dumps(json_object, indent=2)
	# print(json_formatted_str)
	#for row in result["data"]:
	#	print(row)