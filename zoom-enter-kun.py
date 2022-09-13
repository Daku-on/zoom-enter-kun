import threading
import datetime
import webbrowser
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pathlib import Path
import sys, os

path_app = os.getcwd()
path = os.path.join(path_app,'url.txt')
file = open(path,'r')
url = file.read()

def enter_zoom():
    webbrowser.open(url, new=0, autoraise=True)

tk.Tk().withdraw()
time_to_zoom = simpledialog.askstring('時刻入力', '何時にzoomに入りますか (HH:MM)')

scheduled_hour = int(time_to_zoom[0:2]) #例外処理必須
scheduled_min = int(time_to_zoom[3:])

dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
scheduled_time = datetime.datetime(dt.year, dt.month, dt.day, scheduled_hour, scheduled_min, 0,0)

now = datetime.datetime.now()
delay = (scheduled_time - now).total_seconds()
threading.Timer(delay, enter_zoom).start()

file.close()