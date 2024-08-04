#%%
#パッケージインストール
import thinker
import random

# %%
#問題定義
alhabet='BCDEFGHIJKLMNOPQRSTUVWXYZ'
question=''

# %%
#数字ランダム取得
#ランダム取得したものとfor文で出したiが一致していれば次を実行
atari= random.randint(0,25)
for i in range(26):
    if i == atari:
        continue
    question += alhabet[i]

# %%    
#thinker の見栄え的なところ
FONT =('メイリオ',24)
root = thinker.Tk()
#画面サイズ
root.geometry('600*400')

# %%
#質問文1
q1= thinker.label(root,text='抜けているアルファベットはどれ',font=FONT)
#質問文2
q2= thinker.label(root,text=question,font=FONT,fg='#80000',bg='#808080')
#解答ボックスの値
e= thinker.Entry(root,font=FONT)
#ボタン
btn=thinker.Button(root,text='解答',font=FONT,command=check)
#あたりか外れか
result= thinker.Label(root,text='',font=FONT)


# %%
#やっている内容
#アルファベット群に存在する文字が入っていると不正解　入っていないものがあれば正解
#アルファベットでない解答だとアルファベットを入れてね
#変数（result）をアップデートする
def check():
    if e.get().upper() in alhabet:
        if e.get().upper() in question:
            result['text']=f'不正解'
        else:
            result['text']=f'正解！'
    else:
        result['text']=f'アルファベットを入力してください'
    result.update()
    





# %%
#文字の大きさとボタン作成
q1.pack(pady=10)
q2.pack(pady=10)
e.pack(pady=10)
btn.pack(pady=10)
result.pack(pady=10)

# %%
root.mainloop







#参考資料
#quiz 作成　https://www.youtube.com/watch?v=f4khchU6F5w
#btn 配置　https://qiita.com/hiratake_0108/items/210d78e8a9f912bfd2cb

