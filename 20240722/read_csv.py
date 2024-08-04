import pandas as pd
import time
import csv
import random 


#data = pd.read_csv(filepath)

#data
#csvファイルを読み取る関数
def read_csv():
    with open(filepath, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        content = [row for row in csvreader]   
    return content

#マックス数値まで値をリストに格納し、数字が入ったリストを取り出すという関数
def create_num_list():
    num_list=[]
    for num in range(1,num_max+1):
        num_list.append(num)
        
    return num_list


#=====================================================================================

#csv のファイルパス導入
filepath="C:/Users/taise/workspace/gamking/onepice_titles.csv"

#csv読み取り関数実行
content=read_csv()

#マックスの数字設定
num_max=100

#リスト作成の関数実行
num_list = create_num_list()



#リストからランダムに取得
i = random.choice(num_list)





print(content[i])
time.sleep(1)
#答え
print(content[i][1])
#問題文
print(content[i][2])
#選択肢1
print(content[i][3])
#選択肢2
print(content[i][4])
#選択肢3
print(content[i][5])
#選択肢4
print(content[i][6])


    
    
    