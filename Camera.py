import time
import tkinter
from tkinter import *
import logging
import boto3
from botocore.exceptions import ClientError

import cv2
from PIL import Image, ImageTk

f = open("C:/Users/Theo/Desktop/rootkey.CSV", "r").read()
f = f.split("=")
ACCESS_KEY = f[1]
SECRET_KEY = f[3]
master = Tk()


class App:
    def __init__(self, video_source=0):
        self.appName = "camera"
        self.window = master
        self.window.title("camera")
        self.video_source = video_source

        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.window, text=self.appName, font=15
                           , bg='blue', fg='white').pack(side=TOP, fill=BOTH)
        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height, bg='red')
        self.canvas.pack()

        self.btn_snapshot = Button(self.window, text="snapshot", width=30, bg="goldenrod2", activebackground='red',
                                   command=self.snapshot)
        self.btn_gallery = Button(self.window, text="gallery", width=30, bg="goldenrod2", activebackground='red',
                                  command=gallery)

        self.btn_snapshot.pack(side=tkinter.LEFT, padx=(50, 10))
        self.btn_gallery.pack(side=tkinter.RIGHT, padx=(10, 50))
        self.update()
        self.window.mainloop()

    def snapshot(self):
        check, frame = self.vid.getFrame()
        if check:
            image = "IMG-" + time.strftime("%m-%d-%H-%M") + ".jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            msg = Label(self.window, text='image saved ' + image, bg='black', fg='green').place(x=430, y=510)
            Upload_file(image, "testbucket1235234")

    def update(self):
        isTrue, frame = self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.window.after(15, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to find camera")

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                return isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return isTrue, None
        else:
            return None

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


def Upload_file(file_name, bucket, object_name=None):
    global s3
    if object_name is None:
        object_name = file_name
        # Upload the file
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)

    try:
        response = s3.upload_file(file_name, bucket, object_name, )
    except ClientError as e:
        logging.error(e)
        return False
    return True


def Download_file():
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    objs = s3.list_objects_v2(Bucket='testbucket1235234')['Contents']
    return objs


def gallery():
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    newWindow = Toplevel(master)
    newWindow.title("Gallery ")
    newWindow.geometry("1000x1000")
    photos = Download_file()
    canvas = Canvas(newWindow)
    scrollbar = Scrollbar(newWindow, orient=VERTICAL, command=canvas.yview)
    frame = tkinter.Frame(canvas)
    for photo in photos:
        fh = s3.get_object(Bucket='testbucket1235234', Key=photo['Key'])['Body']
        test = ImageTk.PhotoImage(file=fh)
        label1 = tkinter.Label(frame, image=test)
        label1.image = test
        label1.pack(pady=10)
    canvas.create_window(0, 0, anchor='nw', window=frame)
    scrollbar.pack(side=RIGHT)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scrollbar.set)

    canvas.pack(fill='both', expand=True, side='left')
    scrollbar.pack(fill='y', side='right')
    mainloop()


App()
