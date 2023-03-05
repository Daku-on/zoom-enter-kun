import tkinter as tk
import tkinter.ttk as ttk
import datetime
import pandas as pd
import webbrowser

class ZoomEnterKun:
    def __init__(self):
        self.url_data = pd.read_csv('url.csv', index_col=0)

    def assign_meeting_key(self, choice):
        return self.url_data.at[choice, 'url']


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.zek = ZoomEnterKun()
        self.master = master
        self.master.title('Zoom Enter Kun')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Meeting URL dropdown menu
        url_label = tk.Label(self, text='Meeting URL:')
        url_label.pack(side='left')
        self.url_choice = ttk.Combobox(self, values=self.zek.url_data.index.tolist())
        self.url_choice.pack(side='left')
        self.url_choice.current(0)  # set initial selection

        # Meeting time entry
        time_label = tk.Label(self, text='Meeting time (HH:MM):')
        time_label.pack(side='left')
        self.time_entry = tk.Entry(self)
        self.time_entry.pack(side='left')

        # Submit button
        self.submit_button = tk.Button(self, text='Enter Zoom', command=self.enter_zoom)
        self.submit_button.pack(side='bottom')

    def enter_zoom(self):
        choice = self.url_choice.current()
        meeting_url = self.zek.assign_meeting_key(choice)
        meeting_time = self.time_entry.get() #make this datetime type!
        try:
            scheduled_time = datetime.datetime.strptime(meeting_time, '%H:%M')
        except ValueError:
            print('Invalid time format. Please enter time in HH:MM format.')
            return
        now = datetime.datetime.now()
        time_to_zoom = scheduled_time.replace(year=now.year, month=now.month, day=now.day)
        if now > time_to_zoom:
            time_to_zoom = time_to_zoom + datetime.timedelta(days=1)
        delay_sec = (time_to_zoom - now).total_seconds()
        self.master.destroy()
        # Open Zoom meeting URL in default browser
        webbrowser.open_new_tab(meeting_url)
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
