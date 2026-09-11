import requests
import tkinter as tk
import io
from PIL import Image, ImageTk

def load_image_from_url(url):
    response = requests.get(url)
    image_bytes = io.BytesIO(response.content)

    pil_image = Image.open(image_bytes)

    return ImageTk.PhotoImage(pil_image)

url = "http://api.weatherapi.com/v1/forecast.json"

params = {
    "key": "86bdf513c90245d993f171514260209",
    "q": "New York, NY",
    "days": "1",
    "aqi": "no",
    "alerts": "no"
}

states = {
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY"
}

root = tk.Tk()
root.geometry("500x550")

root["bg"] = "#16263C"

title_label = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 26, "bold"),
    bg="#16263C",
    fg="white",
)
title_label.pack(padx=15)

location = "New York, NY"

location_label = tk.Label(
    root,
    text=location,
    font=("Arial", 20),
    bg="#16263C",
    fg="#CCCBCB"
)
location_label.pack(pady=10)

image_label = tk.Label(
    root,
    bg="#16263C",
    fg="white")
image_label.pack()

temperature = tk.Label(
    root,
    font=("Arial", 26, "bold"),
    bg="#16263C",
    fg="white"
)
temperature.pack()

input_value = tk.Entry(root, font=("Arial", 16))
input_value.pack(padx=15)
def change_location(event):
    global location

    if event.keysym != "Return":
        return

    value = input_value.get().lower().strip()

    global params
    params["q"] = value
    response = requests.get(url, params=params)
    data = response.json()
    city = data["location"]["name"]
    state = states[data["location"]["region"].lower()]
    
    location = f"{city}, {state}"

    location_label.configure(text=location)

    get_weather(location)

def get_weather(city):
    global params
    params["q"] = city
    response = requests.get(url, params=params)
    data = response.json()

    iconfile = load_image_from_url("https:" + data["current"]['condition']['icon'])
    condition = data['current']['condition']['text']
    temp = int(data["current"]["temp_f"])
    feels = int(data["current"]["feelslike_f"])
    humidity = int(data["current"]["humidity"])
    wind = int(data["current"]["gust_mph"])
    high = int(data["forecast"]['forecastday'][0]['day']['maxtemp_f'])
    low = int(data["forecast"]['forecastday'][0]['day']['mintemp_f'])
    image_label.configure(image=iconfile)
    image_label.image = iconfile
    temperature.configure(text=f"{temp}°F")

value = input_value.get()
root.bind("<Key>", change_location)

root.mainloop()