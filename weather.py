from tkinter import *
from PIL import ImageTk, Image
import requests

HEIGHT = 650
WIDTH = 450


root = Tk()
root.title("Weather ")
root.iconbitmap('ic.ico')
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


# API key : d97dd2dfd8d75bd9862f7f4e71096463
# api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}


def format_resp(weather,city):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        # print(weather)

        fin_str = 'Name:%s \nConditions:%s \nTemperature (°C):%s' % (
            name, desc, str(temp))

    except:
        fin_str = 'Your search %s \ndid not match any document.' % (city)

    return fin_str


def get_weather(event):
    city=entry.get()
    # this is the API key
    weather_key = 'd97dd2dfd8d75bd9862f7f4e71096463'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parm = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    # using the get funtion from the request module to interact the webpage
    response = requests.get(url, params=parm)
    weather = response.json()

    print(weather)

    # this for images to display for the given city name.
    try:
        i_id = weather['weather'][0]['icon']
    except:
        i_id = ""
    
    label['text'] = format_resp(weather,city)

    idicon = i_id + '.png'
    
    if idicon in day:
        photo = ImageTk.PhotoImage(Image.open(idicon))
        labelphoto.delete("all")
        labelphoto.create_image(0, 0, anchor='nw', image=photo)
        labelphoto.image = photo
    elif idicon in night:
        photo = ImageTk.PhotoImage(Image.open(idicon))
        labelphoto.delete("all")
        labelphoto.create_image(0, 0, anchor='nw', image=photo)
        labelphoto.image = photo


bg_image = ImageTk.PhotoImage(Image.open("background3.jpg"))
day = ['01d.png', '02d.png', '03d.png', '04d.png',
       '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png',
         '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']


bg_label = Label(image=bg_image)
bg_label.place(relheight=1, relwidth=1)

search_ima = PhotoImage(file='search3.png')

frame_input = Frame(root, bg="#99b3e6", bd=3)
frame_input.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.85, anchor='n')

entry = Entry(frame_input, font=('courier', 22,'bold'), bg="grey", fg='white')
entry.place(relheight=1, relwidth=0.628)

button = Button(frame_input,image=search_ima,bg="white")
button.bind("<Button-1>",get_weather)
button.place(relx=0.65, relheight=1, relwidth=0.35)

frame_output = Frame(root, bg="#99b3e6", bd=3)
frame_output.place(relx=0.05, rely=0.25, relheight=0.55,
                   relwidth=0.90)

label = Label(frame_output, bg="grey", fg='white', font=(
    'courier', 16), anchor='nw', justify='left', bd=4)
label.place(relheight=1, relwidth=1)

labelphoto = Canvas(label, bg='grey', bd=0, highlightthickness=0)
labelphoto.place(relx=0.5, rely=0.5, relheight=0.35, relwidth=0.35, anchor='n')


root.mainloop()
