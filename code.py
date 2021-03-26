import csv
import pandas as pd

dataset1 = []
dataset2 = []

with open("bright_stars.csv",'r', encoding="utf8") as f:
    csvReader = csv.reader(f)    
    for i in csvReader:
        dataset1.append(i)
        
with open("dwarf_stars.csv",'r', encoding="utf8") as f:
    csvReader = csv.reader(f)    
    for i in csvReader:
        dataset2.append(i)

header1 = dataset1[0]
header2 = dataset2[0]

headers = header1+header2

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

planet_data = []

for i in planet_data1:
    planet_data.append(i)

for j in planet_data2:
    planet_data.append(j)

with open("final.csv",'w', encoding="utf8") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)   
    csvWriter.writerows(planet_data)