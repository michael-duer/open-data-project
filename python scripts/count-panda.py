import pandas as pd
import csv
from datetime import datetime

csv_file = pd.read_csv('./data/Fahrgastzahlen_2019-2.csv', index_col=False)

#format the 'date' column as date type in the form: "year.month.day"
#csv_file['date'] = pd.to_datetime(csv_file.date, format="%Y.%m.%d", infer_datetime_format = True)
pd.to_datetime(csv_file['date'], format="%d.%m.%Y")
#datetimeobject = datetime.strptime(csv_file['date'],'%d.%m.%Y')

#wrong output!!
#csv_file['date'] = pd.to_datetime(csv_file['date']).dt.strftime('%d.%m.%Y')

#print(csv_file)

#group dates, remove and add up dublicates of transported_people
edited_file = csv_file.groupby(['date'])['transported_people'].agg(['sum'])

#sortierung anpassen so dass datum reihenfolge stimmt
#sortiert = sorted(df1, key=lambda row: row[0], reverse=True)
#df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d/%m/%Y')

#edited_file = sorted(edited_file, key = lambda row: datetime.strptime(row[0], "%d.%m.%Y"))
edited_file.sort_values(by="date", ascending = True, inplace=True)
#export as csv
edited_file.to_csv("./data/frequenz-year2019.csv")

print("Calculation finished!")