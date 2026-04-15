from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()

    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fbe1c05acafa3f78cf7c539fef58291f").json()
    w_lable1.config(text=data["weather"][0]["main"])

    wb_lable1.config(text=data["weather"][0]["description"])
    temp_lable1.config(text=str(int(data["main"]["temp"]-273.15)))
    Pressure_lable1.config(text=data["main"]["pressure"])                                                             

win = Tk()
win.title("Weather Forcast")
win.config(bg = "black")
win.geometry("500x540")

name_lable = Label(win,text="Weather App",font=("Time New Romen",40,"bold"))
                  
name_lable.place(x=25, y=50, height=50,width=450)

city_name = StringVar()
list_name = [('Andhra Pradesh'),
                'Arunachal Pradesh',
                ('Assam'),
                ('Bihar'),
                ('Chhattisgarh'),
                ('Delhi'),
                ('Goa'),
                ('Gujarat'),
                ('Haryana'),
                ('Himachal Pradesh'),
                ('Jammu and Kashmir'),
                ('Jharkhand'),
                ('Karnataka'),
                ('Kerala'),
                ('Madhya Pradesh'),
                ('Maharashtra'),
                ('Manipur'),
                ('Meghalaya'),
                ('Mizoram'),
                ('Nagaland'),
                ('Orissa'),
                ('Punjab'),
                ('Rajasthan'),
                ('Sikkim'),
                ('Tamil Nadu'),
                ('Tripura'),
                ('Uttar Pradesh'),
                ('Uttarakhand'),
                ('West Bengal'),
               ]

com = ttk.Combobox(win,text="Weather App", values=list_name,font=("Time New Romen",20,"bold"), textvariable=city_name)
com.place(x=25, y=120, height=50,width=450)




w_lable = Label(win,text="Weather climate",font=("Time New Romen",20))

w_lable.place(x=25,y=260,height=50,width=210)


w_lable1 = Label(win,text="",font=("Time New Romen",20))

w_lable1.place(x=250,y=260,height=50,width=210)




wb_lable = Label(win,text="Weather Description",font=("Time New Romen",16))

wb_lable.place(x=25,y=330,height=50,width=210)



wb_lable1 = Label(win,text="",font=("Time New Romen",16))

wb_lable1.place(x=250,y=330,height=50,width=210)


temp_lable = Label(win,text="Temperature",font=("Time New Romen",20))

temp_lable.place(x=25,y=400,height=50,width=210)


temp_lable1 = Label(win,text="",font=("Time New Romen",14))

temp_lable1.place(x=250,y=400,height=50,width=210)



Pressure_lable = Label(win,text="Pressure",font=("Time New Romen",20))

Pressure_lable.place(x=25,y=470,height=50,width=210)


Pressure_lable1 = Label(win,text="",font=("Time New Romen",20))

Pressure_lable1.place(x=250,y=470,height=50,width=210)


done_button= Button(win,text="Done", font=("Time New Romen",20,"bold"), command=data_get)
done_button.place(y=190, height=50,width=100,x=200)

win.mainloop()