from tkinter import *
import requests
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime


def tk_frame():
    root = Tk()

    def get_weather():
        try:
            city = cityField.get()
            key = 'key'
            url = 'http://api.openweathermap.org/data/2.5/weather'
            params = {'APPID': key, 'q': city, 'units': 'metric'}
            result = requests.get(url, params)
            weather = result.json()
            tf = TimezoneFinder()
            tz = pytz.timezone(tf.timezone_at(lng=weather['coord'].get('lon'), lat=weather['coord'].get('lat')))
            tzcurrenttime = datetime.now(tz).strftime("%b %d, %H:%M:%S")
            info['text'] = f'{str(tzcurrenttime)}\n {str(weather["name"])}: {round(weather["main"]["temp"])}°C '
        except KeyError:
            cityField.delete(0, END)
            cityField.insert(0, "")
            info.configure(text='Incorrect input.\n Please, try again')

    root['bg'] = '#494E4C'
    root.title('Weather tool')
    root.geometry('300x250')
    root.resizable(width=False, height=False)
    frame_font = ('Roboto', 11, 'bold')
    frame_top = Frame(root, bg='#80A792', bd=3)
    frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
    frame_bottom = Frame(root, bg='#80A792', bd=3)
    frame_bottom.place(relx=0.15, rely=0.50, relwidth=0.7, relheight=0.16)
    cityField = Entry(frame_top, bg='#F4F5F3', font=frame_font)
    cityField.pack()
    cityField.focus()
    btn = Button(frame_top, text='Get info', fg='#F4F5F3', bg='#9CA792', font=frame_font, command=get_weather)
    btn.pack()
    root.bind('<Return>', lambda event=None: btn.invoke())
    info = Label(frame_bottom, text='Weather result', fg='#F4F5F3', bg='#80A792', font=frame_font)
    info.pack()
    root.mainloop()

tk_frame()
