#参考資料
#https://daeudaeu.com/tkinter_quiz/
#https://www.earthlink.co.jp/engineerblog/technology-engineerblog/7744/
#



#01_ライブラリインポート
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

#02_メインウィンドウ作成
root = tk.Tk()

#03_メインウィンドウのタイトルを変更
root.title("Tkinter test")

#04_メインウィンドウを640x480にする
root.geometry("640x480")

#05_ボタン定義
button = tk.Button(root, text="ボタン")

#06_ボタン型作り
frame = ttk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

#ボタン配置
button.pack()
