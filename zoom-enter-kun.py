import threading
import datetime
import webbrowser
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pathlib import Path
import sys, os, random

def ask_schedule():
    tk.Tk().withdraw()
    time_to_zoom = simpledialog.askstring('時刻入力', '何時にzoomに入りますか (HH:MM)')
    # dt = datetime.strptime("2018/06/05 13:45:06", "%Y/%m/%d %H:%M:%S") これに変更 http://hxn.blog.jp/archives/9800548.html
    try:
        scheduled_time = datetime.strptime(ask_schedule.time_to_zoom, '%H:%M')
    except:
        print('形式が正しくありません。')
    return time_to_zoom

def enter_zoom():
    webbrowser.open(url, new=0, autoraise=True)
    
def done_message(delay_sec):
    now = datetime.datetime.now()
    scheduled_time = (now + datetime.timedelta(seconds = delay_sec)).isoformat(' ')
    top = tk.Toplevel()
    top.title('完了報告')
    tk.Message(top, text=scheduled_time + 'に入室します。', padx=20, pady=20).pack()
    WELCOME_DURATION = 10000
    top.after(WELCOME_DURATION, top.destroy)
    tk.mainloop()

def current_dir():
    if getattr(sys, 'frozen', False):
        path_app = os.path.dirname(os.path.abspath(sys.executable))
    else:
        path_app = os.path.dirname(os.path.abspath(__file__))
    
    file_name = 'url.txt'
    path = os.path.join(path_app, file_name)
    return path # pyinstaller でアプリ化したときに動かにゃい。 execは動く。
    # ここも読もうね。多分こっちが最新。https://vucavucalife.com/kivy-app-wo-packaging-by-pyinstaller-on-macos-monterey-m1-macbook/#outline__6_1_1

    # cf. https://qiita.com/typeling1578/items/6e86cfc1febb2cf53141

def make_delay(scheduled_time):
    #ここらへんintとdatetime型でごっちゃってる
    min_delay_sec = 120
    max_delay_sec = 300
    ran_seconds = random.randint(min_delay_sec,max_delay_sec) # 3分〜5分前の間でランダムに入室時刻をずらす。5分前以降に起動した場合の例外処理が必要
    now = datetime.datetime.now()
    delay = (scheduled_time - now).total_seconds()
    if delay > max_delay_sec:
        delay = (scheduled_time - now).total_seconds() - ran_seconds
    else: 
        delay = 5
    return delay
# ---------------------------------------------    
file = open(current_dir.path,'r')
url = file.read()
file.close()

ask_schedule()
make_delay(ask_schedule.time_to_zoom)
threading.Timer(make_delay.delay, enter_zoom).start()
done_message(make_delay.delay)
# https://stackoverflow.com/questions/30235587/closing-tkmessagebox-after-some-time-in-python?rq=1
