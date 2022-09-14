import threading
import datetime
import webbrowser
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pathlib import Path
import sys, os, random


if getattr(sys, 'frozen', False):
    path_app = os.path.dirname(os.path.abspath(sys.executable))
else:
    path_app = os.path.dirname(os.path.abspath(__file__))
# cf. https://qiita.com/typeling1578/items/6e86cfc1febb2cf53141
file_name = 'url.txt'
path = os.path.join(path_app, file_name) # pyinstaller でアプリ化したときに動かにゃい。 execは動く。
# ここも読もうね。多分こっちが最新。https://vucavucalife.com/kivy-app-wo-packaging-by-pyinstaller-on-macos-monterey-m1-macbook/#outline__6_1_1
file = open(path,'r')
url = file.read()

def enter_zoom():
    webbrowser.open(url, new=0, autoraise=True)

tk.Tk().withdraw()
time_to_zoom = simpledialog.askstring('時刻入力', '何時にzoomに入りますか (HH:MM)')

# dt = datetime.strptime("2018/06/05 13:45:06", "%Y/%m/%d %H:%M:%S") これに変更 http://hxn.blog.jp/archives/9800548.html
scheduled_hour = int(time_to_zoom[0:2]) #例外処理必須
scheduled_min = int(time_to_zoom[3:5])

dt = datetime.datetime.today()
scheduled_time = datetime.datetime(dt.year, dt.month, dt.day, scheduled_hour, scheduled_min, 0,0)

now = datetime.datetime.now()

#ここらへんintとdatetime型でごっちゃってる
min_delay_sec = datetime.timedelta(seconds = 120)
max_delay_sec = datetime.timedelta(seconds = 300)
ran_seconds = random.randint(min_delay_sec,max_delay_sec) # 3分〜5分前の間でランダムに入室時刻をずらす。5分前以降に起動した場合の例外処理が必要

delay = (scheduled_time - now).total_seconds()
if delay > max_delay_sec.total_seconds():
    delay = (scheduled_time - now).total_seconds() - ran_seconds
else: 
    delay = datetime.timedelta(seconds = 5)
threading.Timer(delay, enter_zoom).start()

file.close()

scheduled_time = (now + datetime.timedelta(seconds = delay)).isoformat(' ')
tk.messagebox.showinfo('完了報告', scheduled_time + 'に入室します。')