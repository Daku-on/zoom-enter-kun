#ChatGPT debugging ```sample.py```
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
    def __init__(self) -> None:
        self.path = ''
        self.meeting_url = ''
        self.delay_sec = 0
    
        
    def current_dir(self):
        if getattr(sys, 'frozen', False):
            path_app = os.path.dirname(os.path.abspath(sys.executable))
        else:
            path_app = os.path.dirname(os.path.abspath(__file__))
        
        file_name = 'url.csv'
        self.path = os.path.join(path_app, file_name)
        return self.path
    
    def assign_meeting_key(self,choice):
        self.meeting_url = self.url_data.at[choice,'url']
        return self.meeting_url
    
    def enter_zoom(self):
        browser = webbrowser.get('chrome')
        browser.open_new_tab(self.meeting_url)
        
    def get_time(self, arg1):
        return arg1
    
    def make_delay(self, arg1):
        min_delay_sec = 120
        max_delay_sec = 300
        ran_seconds = random.randint(min_delay_sec,max_delay_sec) 
        # 3分〜5分前の間でランダムに入室時刻をずらす。
        # 5分前以降に起動した場合の例外処理が必要
        now = datetime.datetime.now()
        delay_sec = (arg1 - now).total_seconds()
        if delay_sec > max_delay_sec:
            delay_sec = (arg1 - now).total_seconds() - ran_seconds
        else: 
            delay_sec = 5
        return delay_sec

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.zek = zoom_enter_kun()
        self.zek.url_data = pd.read_csv(self.zek.current_dir(),index_col=0)
        self.time_to_zoom = None
        self.scheduled_time = None
        
        self.master = master
        self.master.title('ミーティングと日時選択')       # ウィンドウタイトル
        self.master.geometry('400x100+500+200') #
