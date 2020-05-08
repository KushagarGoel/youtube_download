"""
Importing pytube
pytube is a python package to download youtube videos.
tkinter is python package to create a GUI in python
"""

# Importing statements
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from pytube import YouTube


# Defining global variables
percent = 0
filename = "C:/Users/kushagar/Downloads/"
file_size = 0


# Get the input from user
def print_text():
    global e
    string = e.get()
    down(string)
    print(string)

# Function to browse the download location
def browsefunc():
    global filename
    filename = filedialog.askdirectory()
    filename = filename + "/"
    pathlabel.config(text=filename)



# To calcuate the %age download left
def percentage(i):
    st = str(i)
    e1.config(text=st + "%")
    if (i == 100):
        e1.config(text="Download complete")


# Showing the progress bar
def show_progress_bar(chunk: bytes, file_handler: None, bytes_remaining: int):
    global file_size
    global percent
    percent = int((100 * (file_size - bytes_remaining)) / file_size)
    #bar()
    #percentage(percent)
    print(percent)


# Function to download youtube videos
def down(string):
    global filename
    print("start")
    yt = YouTube(string)
    yt.register_on_progress_callback(show_progress_bar)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    global file_size
    file_size = yt.filesize
    global top3
    Label(top3, text="File Size: " + str(int((file_size) / (1024 * 1024))) + "MB          ").pack(side=LEFT)
    yt.download(filename)
    print("download complete")



# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    global percent
    global root
    global progress
    progress['value'] = 5
    root.update_idletasks()
    time.sleep(0.01)



# creating tkinter window
root = Tk()

# Pane 1 for getting the input from user
top1 = Frame(root)
top1.pack()
Label(top1, text="Enter the link").pack(side=LEFT)
e = Entry(top1, width=46)
e.pack(side=RIGHT)

# pane 2 to get Browse location
top2 = Frame(root)
top2.pack()
Label(top2, text="Download location: ").pack(side=LEFT)
browsebutton = Button(top2, text="Browse", command=browsefunc)
browsebutton.pack(side=RIGHT)
pathlabel = Label(top2, text=filename)
pathlabel.pack(side=RIGHT)

# Pane 3 for Progress bar widget, file size
top3 = Frame(root)
top3.pack()
e1 = Label(top3)
e1.pack(side=RIGHT)
progress = Progressbar(top3, orient=HORIZONTAL, length=100, mode='determinate')
progress.pack(pady=10, side=RIGHT)


# Pane 4 for Start download Button
top4 = Frame(root)
top4.pack()
Button(top4, text='Start Download', command=print_text).pack(pady=10)

mainloop()

