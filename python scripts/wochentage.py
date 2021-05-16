from datetime import datetime
import csv

#init reader
csv_read = open('./data/year2020.csv', 'r')
reader = csv.reader(csv_read)

#init writer
with open('heatmap2020.csv', 'w', newline='') as csv_write:
    writer = csv.writer(csv_write, delimiter=',', quoting = csv.QUOTE_MINIMAL)

    next(reader) #skip header in read file
    writer.writerow(['day,month,value']) #write header
 
    for row in reader:
        date = datetime.strptime(row[0], '%d.%m.%Y') #parse date
        weekday = date.weekday()
        month = date.month
        value = row[1]
        writer.writerow([str(weekday), str(month), str(value)])

print('File generated!')