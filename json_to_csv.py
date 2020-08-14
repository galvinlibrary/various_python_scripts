
# Python program to convert 
# JSON file to CSV 
  
  
import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open(r'C:\Users\tfluhr\Downloads\iit_works3.json') as json_file: 
    data = json.load(json_file) 
  
item_rec = data['items'] 
  
# now we will open a file for writing 
data_file = open(r'C:\Users\tfluhr\Downloads\iit_works_new.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for item in item_rec: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = item.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(item.values()) 
  
data_file.close() 
