import csv

with open('./test.csv', 'r') as read_file:
    csv_reader = csv.reader(read_file, delimiter=',')

    #declare counters
    aa_counter = 0
    bb_counter = 0
    cc_counter = 0

    #create temp array of all names
    name = []
#    for row in csv_reader:                  #cant use reader more than once
#        name.append(row[0])
    #remove headings
#    name.pop(0)
    #create array for unique names and delete duplicates
    name_unique = []
#    [name_unique.append(elements) for elements in name if elements not in name_unique]

    print(name_unique)

    #iterate over rows amd count occurrence
    for row in csv_reader:

       # while(row[0] == name_unique[0]):
        #    counter += int(row[1])
       # add all elements where row[0] is same

        if row[0] == 'aa':
            aa_counter += int(row[1])
            print('Test',aa_counter)
        if row[0] == 'bb':
            bb_counter += int(row[1])
        if row[0] == 'cc':
            cc_counter += int(row[1])
        
    #print counters
    print("AA:", aa_counter)
    print("BB:", bb_counter)
    print("CC:", cc_counter)

#write counters in new file
with open('./test-write.csv', 'w', newline='') as write_file:
    csv_writer = csv.writer(write_file)
    
    csv_writer.writerow(['name', 'number'])
    csv_writer.writerow(['aa', aa_counter])
    csv_writer.writerow(['bb', bb_counter])
    csv_writer.writerow(['cc', cc_counter])
    