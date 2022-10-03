import importlib
from shutil import which
import threading
import datetime
from urllib.request import HTTPPasswordMgrWithDefaultRealm
import webbrowser
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.simpledialog as simpledialog
from pathlib import Path
import sys
import os
import random
import math
import csv
import pandas as pd

# def meeting_key_get(window):
#     global meeting_key
#     meeting_key = window.get()  
#     return meeting_key
global meeting_key
def assign_meeting_key(choiced):
    meeting_key = choiced
    return meeting_key

def ask_meeting(url_list):
    
    root = tk.Tk()
    root.title('ミーティング選択')
    choice = tk.StringVar()
    which_meeting_window = ttk.Combobox(
        root, textvariable=choice, values = list(url_list.index))
    which_meeting_window.bind("<<ComboboxSelected>>",assign_meeting_key(choice))
    which_meeting_window.pack()
    #which_meeting_window.set(list(url_list.iat[1,0]))
    
    btn = tk.Button(root, text='決定',command=lambda: root.destroy)
    # btn.bind('<ButtonPress>',meeting_key_get(which_meeting_window))
    btn.pack()
    root.mainloop()
    
    
    return meeting_key

def ask_schedule():
    tk.Tk().withdraw()
    time_to_zoom = simpledialog.askstring(
        '時刻入力', '何時にzoomに入りますか (HH:MM)'
        )
    # dt = datetime.strptime("2018/06/05 13:45:06", "%Y/%m/%d %H:%M:%S") 
    # これに変更 http://hxn.blog.jp/archives/9800548.html
    tday = datetime.date.today().strftime('%Y%m%d')                                        
    
    try:
        scheduled_time = datetime.datetime.strptime(
            tday + time_to_zoom, '%Y%m%d%H:%M'
            )
        return scheduled_time
    except:
        if time_to_zoom == None:
            sys.exit()
        else: 
            print('形式が正しくありません。')
            return ask_schedule()

def enter_zoom(meeting_url):
    webbrowser.open(meeting_url, new=0, autoraise=True)
    
def done_message(delay_sec):
    #ここらへん参照 https://qiita.com/aoirint/items/ca2386b68e8fec16ff53
    now = datetime.datetime.now()
    scheduled_time = now + datetime.timedelta(seconds = delay_sec)
    scheduled_time_iso = (scheduled_time).isoformat(
        ' ', timespec='seconds')
    root = tk.Tk()
    root.withdraw()
    
    top = tk.Toplevel()
    top.geometry('400x100+500+200')
    top.title('完了報告')
    tk.Message(
        top, font = ("", 22),text=scheduled_time_iso + 'に入室します。',
        padx=1, pady=10
        ).pack()
    duration = (math.ceil(delay_sec) - 10)*1000
    root.after(duration, root.quit)
    top.after(duration, top.destroy)

    top.mainloop()
    

def current_dir():
    if getattr(sys, 'frozen', False):
        path_app = os.path.dirname(os.path.abspath(sys.executable))
    else:
        path_app = os.path.dirname(os.path.abspath(__file__))
    
    file_name = 'url.csv'
    path = os.path.join(path_app, file_name)
    return path 
    # pyinstaller でアプリ化したときに動かにゃい。 execは動く。
    # ここも読もうね。多分こっちが最新。https://vucavucalife.com/kivy-app-wo-packaging-by-pyinstaller-on-macos-monterey-m1-macbook/#outline__6_1_1

    # cf. https://qiita.com/typeling1578/items/6e86cfc1febb2cf53141

def make_delay(what_time):
    min_delay_sec = 120
    max_delay_sec = 300
    ran_seconds = random.randint(min_delay_sec,max_delay_sec) 
    # 3分〜5分前の間でランダムに入室時刻をずらす。
    # 5分前以降に起動した場合の例外処理が必要
    now = datetime.datetime.now()
    delay = (what_time - now).total_seconds()
    if delay > max_delay_sec:
        delay = (what_time - now).total_seconds() - ran_seconds
    else: 
        delay = 5
    return delay
# ---------------------------------------------    
with open(current_dir(), encoding="utf8") as url_csv:
    url_data = pd.read_csv(url_csv,skipinitialspace=True,header=0,index_col=0).astype(str)
    meeting_key = ask_meeting(url_data)
    meeting_url = url_data.at[meeting_key,'url']

what_time = ask_schedule()
threading.Timer(make_delay(what_time), enter_zoom(meeting_url)).start()
done_message(make_delay(what_time))
# https://stackoverflow.com/questions/30235587/closing-tkmessagebox-after-some-time-in-python?rq=1

sys.exit()