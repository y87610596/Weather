import requests
import datetime


latitude = float(input("Input latitude:"))
longitude = float(input("Input longitude:"))

searched_date = str(input("Input date:"))

if not searched_date:
    searched_date = datetime.date.today() + datetime.timedelta(days=1)
    searched_date = str(searched_date)

filename = "weather.txt"
precip = 0
record_found = False

with open(filename, "r") as file:
    for line in file:
        latitude_record, longitude_record, date, precip_record = line.strip().split(",")
        latitude_record = float(latitude_record)
        longitude_record = float(longitude_record)
        if latitude_record == latitude and longitude_record == longitude and date == searched_date:
            precip = float(precip_record)
            record_found = True
            break

if not record_found:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

    response = requests.get(url)

    print(response.json())

    data = response.json()

    for key, value in data.items():
        if key == 'daily':
            dic = value
            for k, v in dic.items():
                if k == 'precipitation_sum':
                    precipitation = v
                    precip = float(precipitation[0])
                    break

    with open(filename, "a") as file:
        line = [f"{latitude},{longitude},{searched_date},{precip}\n"]
        file.writelines(line)

print(precip)
while True:
    if precip == 0:
            print("It will not rain.")
    elif precip > 0:
            print(f"It will rain, precipitation value:{precip}")
    elif precip < 0:
            print("I don't know")
    break




