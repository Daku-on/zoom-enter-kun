import importlib
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

class zoom_enter_kun:
    def __init__(self):
        self.delay_sec = 0
        self.time_to_zoom = None
        self.scheduled_time = None
        self.meeting_url = ''
        self.url_data = None
        self.path = ''
        self.duration = 3*10**3

    def assign_meeting_key(self,choice):
        self.meeting_url = self.url_data.at[choice,'url']
        return self.meeting_url

    def ask_meeting(self,arg1):
        ask_meeting_window = tk.Toplevel()
        ask_meeting_window.geometry('400x100+500+200')
        ask_meeting_window.title('ミーティング選択')   
        which_meeting_window = ttk.Combobox(
            ask_meeting_window, values = list(arg1.index))
        which_meeting_window.pack()
        which_meeting_window.set(arg1.index.values[0])
        
        btn1 = tk.Button(ask_meeting_window, text='決定',command=lambda:[self.assign_meeting_key(which_meeting_window.get()),])
        btn2 = tk.Button(ask_meeting_window, text='削除',command=lambda:[ask_meeting_window.quit(),])
        
        
        btn1.pack()
        btn2.pack()
        ask_meeting_window.mainloop()
        
        return self.meeting_url

    def ask_schedule(self):
        ask_schedule_window = tk.Toplevel()
        ask_schedule_window.withdraw()
        self.time_to_zoom = simpledialog.askstring(
            '時刻入力', '何時にzoomに入りますか (HH:MM)'
            )
        # dt = datetime.strptime("2018/06/05 13:45:06", "%Y/%m/%d %H:%M:%S") 
        # これに変更 http://hxn.blog.jp/archives/9800548.html
        tday = datetime.date.today().strftime('%Y%m%d')                                        
        
        try:
            self.scheduled_time = datetime.datetime.strptime(
                tday + self.time_to_zoom, '%Y%m%d%H:%M'
                )
            return self.scheduled_time
        except:
            if self.time_to_zoom == None:
                return sys.exit()
            else: 
                print('形式が正しくありません。')
                return self.ask_schedule()

    def enter_zoom(self):
        browser = webbrowser.get('chrome')
        browser.open_new_tab(self.meeting_url)
        
    def done_message(self,arg1):
        #ここらへん参照 https://qiita.com/aoirint/items/ca2386b68e8fec16ff53
        done_message_window = tk.Toplevel()
        now = datetime.datetime.now()
        self.scheduled_time = now + datetime.timedelta(seconds = arg1)
        scheduled_time_iso = (self.scheduled_time).isoformat(
            ' ', timespec='seconds')
        
        done_message_window.geometry('400x100+500+200')
        done_message_window.title('完了報告')
        tk.Message(
                done_message_window, font = ("", 22),text=scheduled_time_iso + 'に入室します。',
            padx=1, pady=10
            ).pack()
        duration = (math.ceil(arg1) - 10)*1000
        root.after(duration, root.quit)
        done_message_window.after(duration, done_message_window.destroy)

        done_message_window.mainloop()
        
        # top = tk.Toplevel()
        # top.geometry('400x100+500+200')
        # top.title('完了報告')
        # tk.Message(
        #     top, font = ("", 22),text=scheduled_time_iso + 'に入室します。',
        #     padx=1, pady=10
        #     ).pack()
        # duration = (math.ceil(arg1) - 10)*1000
        # root.after(duration, root.quit)
        # top.after(duration, top.destroy)

        # top.mainloop()
        

    def current_dir(self):
        if getattr(sys, 'frozen', False):
            path_app = os.path.dirname(os.path.abspath(sys.executable))
        else:
            path_app = os.path.dirname(os.path.abspath(__file__))
        
        file_name = 'url.csv'
        self.path = os.path.join(path_app, file_name)
        return self.path
        # pyinstaller でアプリ化したときに動かにゃい。 execは動く。
        # ここも読もうね。多分こっちが最新。https://vucavucalife.com/kivy-app-wo-packaging-by-pyinstaller-on-macos-monterey-m1-macbook/#outline__6_1_1

        # cf. https://qiita.com/typeling1578/items/6e86cfc1febb2cf53141

    def make_delay(self, what_time):
        min_delay_sec = 120
        max_delay_sec = 300
        ran_seconds = random.randint(min_delay_sec,max_delay_sec) 
        # 3分〜5分前の間でランダムに入室時刻をずらす。
        # 5分前以降に起動した場合の例外処理が必要
        now = datetime.datetime.now()
        self.delay_sec = (what_time - now).total_seconds()
        if self.delay_sec > max_delay_sec:
            self.delay_sec = (what_time - now).total_seconds() - ran_seconds
        else: 
            self.delay_sec = 5
        return self.delay_sec
    
    def timer(self):
        threading.Timer(self.delay_sec,self.enter_zoom()).start()
# --------------------------------------------- 
zek = zoom_enter_kun()
root = tk.Tk()
root.withdraw()
with open(zek.current_dir(), encoding="utf8") as url_csv:
    zek.url_data = pd.read_csv(url_csv,skipinitialspace=True,header=0,index_col=0).astype(str)
    zek.ask_meeting(zek.url_data)

zek.what_time = zek.ask_schedule()
zek.timer()
zek.done_message(zek.delay_sec)
# https://stackoverflow.com/questions/30235587/closing-tkmessagebox-after-some-time-in-python?rq=1

sys.exit()