from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size=0

# this fuction gets called for updating percentage
def progressDownload(stream=None,chunk=None,file_handle=None,remaining=None):
    # gets the pecentage of file that has been downloaded
    file_downloaded=(file_size - file_handle)
    percentage=(file_downloaded/file_size) * 100
    Download_Butn.config(text="{:00.0f} % Downloaded".format(percentage))


def videoDownload():
    global file_size
    try:
        url=urlField.get()
        print(url)
        # changing buttton text

        Download_Butn.config(text='Finding ways to Download...')
        Download_Butn.config(state=DISABLED)

        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return

        yt = YouTube(url,on_progress_callback=progressDownload)
        strms = yt.streams.first()
        file_size=strms.filesize
        vTitle.config(text="Video Title : {}".format(strms.title))
        vTitle.pack(side=TOP)
        print(file_size)

        # till here stuffs.....
        print("Download Started....")
        strms.download(path_to_save_video)

        print("Downloaded....")
        Download_Butn.config(text="Start Download")
        Download_Butn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)

def videoDownloadThread():
    thread=Thread(target=videoDownload)
    thread.start()


# starting GUI building
main=Tk()

#setting the title
main.title("My Youtube Downloader")

# setting the icon
main.iconbitmap('images.ico')

# setting width*height
main.geometry("500x500")

#heading icon
file=PhotoImage(file='images.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)


#url textfield
urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#Download Button
Download_Butn=Button(main,text="Start Download",font=("verdana",20),relief='ridge',command=videoDownloadThread)
Download_Butn.pack(side=TOP,pady=10)

#video title in GUI
vTitle=Label(main,text="video title")

main.mainloop()
