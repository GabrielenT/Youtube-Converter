import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from pytube import YouTube
currentVersion = "0.1"

app = Tk()
app.title("YT video Converter")
app.geometry('350x200')

mediaTypes = ["mp3", "mp4"]
qualitySelection = ["360p","480p", "720p", "Max"]
welcome = tk.Label(
    text=("Welcome to the YT converter app v." + currentVersion),
    width='350',
    height=2
)
linkRequestLabel = Label(text="Link to the Youtube video:")
mediaTypeLabel = Label(text="Select media type:")
qualityTypeLabel = Label(text="Select video quality:")
link = StringVar()
userInput = Entry(app, textvariable=link)

mediaSelected = StringVar()
mediaCombo = Combobox(app, textvariable=mediaSelected)
mediaCombo['values'] = mediaTypes

qualitySelected = StringVar()
qualityCombo = Combobox(app, textvariable=qualitySelected)
qualityCombo['values'] = qualitySelection


mediaList = Listbox(app, selectmode=SINGLE, height = len(mediaTypes), width = 50)
for x in mediaTypes: 
    mediaList.insert(END, x)


def convert():
    yt = YouTube(link.get())
    if mediaSelected.get() == "mp3":
        yt.streams.filter(only_audio=True).first().download(filename=f"{yt.title}.mp3")

    if mediaSelected.get() == "mp4":
        pass
        #implement mp4 download


convertButton = Button(app, text = "Convert", command=convert)

welcome.pack()
mediaTypeLabel.pack()
mediaCombo.pack()
qualityTypeLabel.pack()
qualityCombo.pack()
linkRequestLabel.pack()
userInput.pack()
convertButton.pack()
app.mainloop()