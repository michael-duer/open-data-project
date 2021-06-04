import pandas as pd
from datetime import datetime

csv_file = pd.read_csv('./data/Fahrgastzahlen_2019.csv', index_col=False)

#format the 'date' column as date type in the form: "day.month.year"
pd.to_datetime(csv_file['date'], format="%d.%m.%Y")

#group dates, remove and add up dublicates of transported_people
edited_file = csv_file.groupby(['date'])['transported_people'].agg(['sum'])

#export as csv
edited_file.to_csv("./data/test.csv")

print("Calculation finished!")