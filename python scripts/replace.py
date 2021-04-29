import csv

reader = csv.reader(open("Fahrgastzahlen_2019_2020.csv", "r"), delimiter=';')

writer = csv.writer(open("Fahrgastzahlen_2.csv", 'w'), delimiter=',')
writer.writerows(reader)

print("Delimiter successfully changed")




#import pandas as pd

#newCsv = pd.read_csv('Fahrgastzahlen_2019.csv',sep=';',decimal=',')

#newCsv.to_csv("real-test.csv")