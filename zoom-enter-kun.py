import threading
import datetime
import webbrowser
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pathlib import Path
import sys, os, random

path_app = os.getcwd()
path = os.path.join(path_app,'url.txt') # pyinstaller でアプリ化したときに動かにゃい
file = open(path,'r')
url = file.read()

def enter_zoom():
    webbrowser.open(url, new=0, autoraise=True)

tk.Tk().withdraw()
time_to_zoom = simpledialog.askstring('時刻入力', '何時にzoomに入りますか (HH:MM)')

scheduled_hour = int(time_to_zoom[0:2]) #例外処理必須
scheduled_min = int(time_to_zoom[3:])

dt = datetime.datetime.today()
scheduled_time = datetime.datetime(dt.year, dt.month, dt.day, scheduled_hour, scheduled_min, 0,0)

now = datetime.datetime.now()
ran_seconds = random.randint(120,300) # 3分〜5分前の間でランダムに入室時刻をずらす。5分前以降に起動した場合の例外処理が必要
delay = (scheduled_time - now).total_seconds() - ran_seconds
threading.Timer(delay, enter_zoom).start()

file.close()

#何時に入ります、的なダイアログを表示したい。