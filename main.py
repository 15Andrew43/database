import requests
import json
import pandas as pd


for i in range(1, 5):
	with open(f'page{i}.html', 'r') as file:
		f = file.read()
		f = f[f.find("[{\"id\":\"pl") : ]
		f = f[: f.rfind("\"id\":\"pl")-2]
		f += ']'
		with open(f'res{i}.txt', 'w') as out_file:
			out_file.write(f)


char_numbers = []
digit_numbers = []
plane_models = []
plane_ids = [] # random
departure_dates = []
departure_times = []
arrival_dates = []
arrival_times = []


departureLocal_dates = []
departureLocal_times = []

arrivalLocal_dates = []
arrivalLocal_times = []


stationTos = []
stationFroms = []
companys = []


n_plane_id = 1488


for i in range(1, 5):
	with open(f'res{i}.txt', 'r') as file:
		f = file.read()
		# print(f)
		json_files = json.loads(f)
		for json_file in json_files:
			try:
				number = json_file['number']
				

				plane_model = json_file['transport']['model']['title']
				

				plane_id = n_plane_id
				n_plane_id += 1 

				departure_date = json_file['departure'].split('T')[0]
				departure_time = json_file['departure'].split('T')[1].split('+')[0]

				arrival_date = json_file['arrival'].split('T')[0]
				arrival_time = json_file['arrival'].split('T')[1].split('+')[0]

				departureLocal_date = json_file['departureLocalDt'].split('T')[0]
				departureLocal_time = json_file['departureLocalDt'].split('T')[1].split('+')[0]				

				arrivalLocal_date = json_file['arrivalLocalDt'].split('T')[0]
				arrivalLocal_time = json_file['arrivalLocalDt'].split('T')[1].split('+')[0]				

				stationTo = json_file['stationTo']['title']

				stationFrom = json_file['stationFrom']['title']

				company = json_file['company']['title']
			except:
				continue


			char_numbers.append(number.split()[0])
			digit_numbers.append(number.split()[1])

			plane_models.append(plane_model)

			plane_ids.append(plane_id)

			departure_dates.append(departure_date)
			departure_times.append(departure_time)

			arrival_dates.append(arrival_date)
			arrival_times.append(arrival_time)

			stationTos.append(stationTo)

			stationFroms.append(stationFrom)

			companys.append(company)





# for i in (
# 			char_numbers,
# digit_numbers,
# plane_models,
# plane_ids,
# departures,
# arrivals,
# stationTos,
# stationFroms,
# companys
# 	):
# 	print(len(i))


df = pd.DataFrame({
		'char_numbers' : char_numbers,
		'digit_numbers' : digit_numbers,
		'plane_models': plane_models,
		'plane_ids' : plane_ids,
		'departure_dates' : departure_dates,
		'departure_times' : departure_times,
		'arrival_dates' : arrival_dates,
		'arrival_times' : arrival_times,



		'stationTos' : stationTos,
		'stationFroms' : stationFroms,
		'companys' : companys
	})

print(df)

df.to_csv('dataframe.csv')
# dict_keys(['id', 'startDate', 'number', 'departureEventKey', 
# 			'stops', 'duration', 'arrivalEventKey', 'transport', 
# 			'title', 'arrivalLocalDt', 'stationTo', 'arrival', 
# 			'isThroughTrain', 'departureEvent', 'company', 
# 			'suburbanFacilities', 'departureLocalDt', 'isInterval', 
# 			'arrivalEvent', 'tariffsKeys', 'thread', 'departure', 
# 			'stationFrom', 'isMetaSegment', 'isDynamic', 'isGone', 
# 			'timezoneFrom', 'timezoneTo'])


# {'model': {'title': 'Airbus A320'}, 'code': 'plane', 'id': 2, 'title': 'Самолёт'}

# {
# 	'settlementId': 213, 
# 	'title': 'Шереметьево', 
# 	'country': {
# 					'code': 'RU', 
# 					'id': 225
# 				}, 
# 	'mainSubtype': 'plane', 
# 	'timezone': 'Europe/Moscow', 
# 	'popularTitle': 'Шереметьево', 
# 	'pageType': 'plane', 'id': 9600213
# }


# print(json_file[5].keys())


# print(json_file[5]['stationTo']['title'])
# print(json_file[5]['stationFrom']['title'])

# print()

# print(json_file[9]['queryingPrices'])

print('good!')