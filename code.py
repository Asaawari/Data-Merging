import csv
import pandas as pd

dataset1 = []
dataset2 = []

with open("stars.csv",'r') as f:
    csvReader = csv.reader(f)    
    for i in csvReader:
        dataset1.append(i)
        
with open("sorted_data.csv",'r') as f:
    csvReader = csv.reader(f)    
    for i in csvReader:
        dataset2.append(i)

header = dataset1[0]

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

planet_data = []

for i in planet_data1:
    planet_data.append(i)

for j in planet_data2:
    planet_data.append(j)

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("final.csv",'a+') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(header)   
    csvWriter.writerows(planet_data)