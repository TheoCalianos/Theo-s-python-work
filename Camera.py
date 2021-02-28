import time
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



class App:
    def __init__(self, video_source=0):
        self.appName = "camera"
        self.window = Tk()
        self.window.title("camera")
        self.video_source = video_source

        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.window, text=self.appName, font=15
                           , bg='blue', fg='white').pack(side=TOP, fill=BOTH)
        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height, bg='red')
        self.canvas.pack()

        self.btn_snapshot = Button(self.window, text="snapshot", width=30, bg="goldenrod2", activebackground='red',
                                   command=self.snapshot)
        self.btn_snapshot.pack()
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
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


App()
