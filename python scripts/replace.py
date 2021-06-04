import csv

reader = csv.reader(open("./pathToFile/oldFile.csv", "r"), delimiter=';')

writer = csv.writer(open("./pathToFile/newFile.csv", 'w', newline=''), delimiter=',')
writer.writerows(reader)

print("Delimiter successfully changed")