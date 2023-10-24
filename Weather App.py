import tkinter as tk
from tkinter import messagebox
import requests
def fetch_weather():
    city = city_entry.get()
    api_key = "75127e28b99d01529c7c26144931d599"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        if 'main' in data and 'weather' in data:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']
            result_label.config(text=f"Temperature: {temperature}°C, Humidity: {humidity}%, Weather: {weather_description}")
        else:
            messagebox.showerror("Error", "Failed to fetch weather data. Check the city name.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
app = tk.Tk()
app.title("Charitha's Weather App")
city_label = tk.Label(app, text="Enter city:")
city_entry = tk.Entry(app)
fetch_button = tk.Button(app, text="Fetch Weather", command=fetch_weather)
result_label = tk.Label(app, text="Weather information will be displayed here.")
city_label.pack()
city_entry.pack()
fetch_button.pack()
result_label.pack()
app.mainloop()
