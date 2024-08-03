import pandas as pd
import time
import csv 

filepath=''

#data = pd.read_csv(filepath)

#data
    
with open(filepath, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader]   
    
for i in range(1,101):
    print(content[i])
    time.sleep(1)
    print(content[i][1])
    
    
    