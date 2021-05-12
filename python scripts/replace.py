import csv

reader = csv.reader(open("./data/Fahrgastzahlen_2019.csv", "r"), delimiter=';')

writer = csv.writer(open("./data/Fahrgastzahlen_2019-2.csv", 'w', newline=''), delimiter=',')
writer.writerows(reader)

print("Delimiter successfully changed")




#import pandas as pd

#newCsv = pd.read_csv('Fahrgastzahlen_2019.csv',sep=';',decimal=',')

#newCsv.to_csv("real-test.csv")