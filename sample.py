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
        app.time_to_zoom = arg1
        return app.time_to_zoom
    
    def get_scheduled_time(self):
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
                return self.create_ask_time_dialog()
    
    def make_delay(self, arg1):
        min_delay_sec = 120
        max_delay_sec = 300
        ran_seconds = random.randint(min_delay_sec,max_delay_sec) 
        # 3分〜5分前の間でランダムに入室時刻をずらす。
        # 5分前以降に起動した場合の例外処理が必要
        now = datetime.datetime.now()
        self.delay_sec = (arg1 - now).total_seconds()
        if self.delay_sec > max_delay_sec:
            self.delay_sec = (arg1 - now).total_seconds() - ran_seconds
        else: 
            self.delay_sec = 5
        return self.delay_sec
    
    def timer(self):
        threading.Timer(self.delay_sec,self.enter_zoom()).start()

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.data = zek.url_data
        self.time_to_zoom = None
        self.scheduled_time = None
        
        self.master.title('ミーティングと日時選択')       # ウィンドウタイトル
        self.master.geometry('400x100+500+200') # ウィンドウサイズ(幅x高さ)

        # ボタンの作成
        btn_modeless = tk.Button(
            self.master, 
            text = "ミーティング選択",   # ボタンの表示名
            command = self.create_ask_meeting_dialog  # クリックされたときに呼ばれるメソッド
            )
        btn_modeless.pack()

        btn_modal = tk.Button(
            self.master, 
            text = "時刻設定",      # ボタンの表示名
            command = self.create_ask_time_dialog    # クリックされたときに呼ばれるメソッド
            )
        btn_modal.pack()

    def create_ask_meeting_dialog(self):
        '''モードレスダイアログボックスの作成'''
        ask_meeting_dialog = tk.Toplevel(self)
        ask_meeting_dialog.title("ミーティング選択")   # ウィンドウタイトル
        ask_meeting_dialog.geometry("300x200+800+200")        # ウィンドウサイズ(幅x高さ)
        ask_meeting_dialog.grab_set()        # モーダルにする
        ask_meeting_dialog.focus_set()       # フォーカスを新しいウィンドウをへ移す
        ask_meeting_dialog.transient(self.master)
        
        which_meeting_window = ttk.Combobox(
            ask_meeting_dialog, values = list(self.data.index))
        which_meeting_window.pack()
        which_meeting_window.set(self.data.index.values[0])
        
        btn1 = tk.Button(
            ask_meeting_dialog, text='決定',command=lambda:[zek.assign_meeting_key(which_meeting_window.get()),ask_meeting_dialog.withdraw])
                
        btn1.pack()
        
        app.wait_window(ask_meeting_dialog)

    def create_ask_time_dialog(self):
        '''モーダルダイアログボックスの作成'''
        ask_time_dialog = tk.Toplevel(self)
        ask_time_dialog.title("時刻設定") # ウィンドウタイトル
        ask_time_dialog.geometry("300x200+400+200")   # ウィンドウサイズ(幅x高さ)
        # モーダルにする設定
        ask_time_dialog.grab_set()        # モーダルにする
        ask_time_dialog.focus_set()       # フォーカスを新しいウィンドウをへ移す
        ask_time_dialog.transient(self.master)   # タスクバーに表示しない
        usr_input = tk.Entry(ask_time_dialog)
        usr_input.grid(row = 2, column = 1)
        ask_time_label = ttk.Label(
            ask_time_dialog, text='何時にzoomに入りますか (HH:MM)')
        ask_time_label.grid(row = 1, column = 1)
        btn1 = tk.Button(
            ask_time_dialog, text='決定',
            command=lambda: [zek.get_time(usr_input.get()),ask_time_dialog.withdraw]) #ここをさらに scheduled_time づくりまで持ってく。list化する
        btn1.grid(row=3,column=1)
        # ダイアログが閉じられるまで待つ
        app.wait_window(ask_time_dialog) 
        

if __name__ == "__main__":
    root = tk.Tk()
    zek = zoom_enter_kun()
    with open(zek.current_dir(), encoding="utf8") as url_csv:
        zek.url_data = pd.read_csv(url_csv,skipinitialspace=True,header=0,index_col=0).astype(str)
    
    app = Application(master = root)
    app.mainloop()
    zek.make_delay(app.scheduled_time)
    zek.timer()