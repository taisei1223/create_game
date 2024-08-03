import pandas as pd
import time

filepath=''

data = pd.read_csv(filepath)

data

for i in range(0,100):
    print(i)
    time.sleep(2)