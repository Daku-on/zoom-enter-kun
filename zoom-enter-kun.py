import imp
import threading
import datetime
import webbrowser
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pathlib import Path
import sys
import os
import random

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
        print('形式が正しくありません。')
        return ask_schedule()

def enter_zoom():
    webbrowser.open(url, new=0, autoraise=True)
    
def done_message(delay_sec):
    #ここらへん参照 https://qiita.com/aoirint/items/ca2386b68e8fec16ff53
    now = datetime.datetime.now()
    scheduled_time = now + datetime.timedelta(seconds = delay_sec)
    scheduled_time_iso = (scheduled_time).isoformat(
        ' ', timespec='seconds')
    root = tk.Tk()
    root.withdraw()
    #root.attributes('-topmost',True)
    
    top = tk.Toplevel()
    top.geometry('400x100+500+200')
    top.title('完了報告')
    tk.Message(
        top, font = ("", 22),text=scheduled_time_iso + 'に入室します。',
        padx=1, pady=10
        ).pack()
    WELCOME_DURATION = 10000
    # root.after(WELCOME_DURATION,root.destroy)
    top.after(WELCOME_DURATION,top.destroy)
    # root.after(2*WELCOME_DURATION, root.destroy())
    top.mainloop()
    

def current_dir():
    if getattr(sys, 'frozen', False):
        path_app = os.path.dirname(os.path.abspath(sys.executable))
    else:
        path_app = os.path.dirname(os.path.abspath(__file__))
    
    file_name = 'url.txt'
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
file = open(current_dir(),'r')
url = file.read()
file.close()

what_time = ask_schedule()
threading.Timer(make_delay(what_time), enter_zoom).start()
done_message(make_delay(what_time))
# https://stackoverflow.com/questions/30235587/closing-tkmessagebox-after-some-time-in-python?rq=1

sys.exit()