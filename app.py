from bs4 import BeautifulSoup
import requests
from tkinter import *
import tkinter.font as font

root = Tk()
root.title('Weather')
root.configure(background='light green')
root.geometry('420x300')
cityNameLabel = Label(root, text="Please Enter Your City Name:", font='Times 16 bold italic').pack()
cityNameEntry = Entry(root, width=14, font=('times 15'))
cityNameEntry.pack(padx=10, pady=5)
degreeLabel = Label(root, text="Please Choose:", font='Times 16 bold italic').pack(padx=0, pady=5)
choosed = StringVar()
choosed.set("Choose")


def save():
    global city
    global value
    city = cityNameEntry.get()
    value = choosed.get()
    procces()

myFont1 = font.Font(size=9, weight="bold")

degreeMenu = OptionMenu(root, choosed, " celsius ", " farenheit ")
degreeMenu.config(height= 2, width=8, bg='light blue')
degreeMenu['font'] = myFont1
degreeMenu.pack(padx=10, pady=0)

def procces():
    address = """https://www.google.com/search?q={}+weather+{}&oq={}+weather+{}&aqs=chrome..69i57j0i13j0i8i13i30j0i390l4.14288j1j7&client=ubuntu&sourceid=chrome&ie=UTF-8""".format(city, value, city, value)
    source = requests.get(address)
    soup = BeautifulSoup(source.content, 'html.parser')
    global cityName, date, degree
    cityName = soup.find('span', class_='BNeawe tAd8D AP7Wnd')
    date = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
    degree = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    status()

def myDelete():
    try:
        weatherStatus.destroy()
        labelError.destroy()
    except Exception:
        weatherStatus.destroy()
    confirmButton['state']=NORMAL
    deleteButton['state']=DISABLED

def status():
    global weatherStatus
    try:
        weatherStatus = Label(root, text="the weather in {} on {} is {}".format(cityName.text, date.text, degree.text))
        weatherStatus.pack()
    except Exception:
        global labelError
        labelError = Label(root, text='city not found')
        labelError.pack()
    confirmButton['state']=DISABLED
    deleteButton['state']=NORMAL

myFont = font.Font(size=9, weight="bold")

confirmButton = Button(root, text="Confirm", bg='green', fg='#ffffff', height= 2, width=9, command=save)
confirmButton['font'] = myFont
confirmButton.pack(padx=5, pady=5)
deleteButton = Button(root, text="Delete!", bg='red',fg='#ffffff', height= 2, width=9, command=myDelete)
deleteButton['font'] = myFont
deleteButton.pack(padx=5, pady=2)

root.mainloop()