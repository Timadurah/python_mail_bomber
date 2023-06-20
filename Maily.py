import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import mailer_bomb_go
import pandas as pd
import json
import datetime


window = tkinter.Tk()

window.title("Tim.adurah MAIL Bomber")
# window.iconbitmap("C:/xampp/htdocs/tikinta/sms/icon.ico")
# monitor man

today = datetime.date.today()
ttday = today.month
if ttday > 9:
    window.destroy()

# fuction for upload csv


def import_csv_data():

    csv_file_path = askopenfilename()
    df = pd.read_csv(csv_file_path)
    global csv_upload_loop
    csv_upload_loop = df


def enter_data():

    # User info
    sendery = sneder_entry.get().replace(" ", "")
    passwordy = password_entry.get()
    topicy = topic_entry.get()
    html__y = html_entry.get()
    hosty = host_entry.get().replace(" ", "")
    porty = port_entry.get().replace(" ", "")

    if sendery and passwordy and topicy and html__y and hosty and porty:

        res = tkinter.messagebox.askyesno(
            title="Confirmation", message="Do you wish to proceed")
        if res == True:
            for i in csv_upload_loop:
                send_sms_go_res = mailer_bomb_go.mailer_sender(sendery, i, passwordy,
                                                               topicy, html__y, hosty, porty)
                x = json.loads(send_sms_go_res)
                writer = x["mail"] + " status:: " + \
                    x["response"]

                f = open("./SENT.txt", "a")
                f.write(writer + "\n")
                f.close()
            global label
            label = tkinter.Label(
            frame_res, text="#:: "+writer+"\n", fg="pink", font=('cursive 10'))
            label.pack()
        else:
            messagebox.showerror('error', 'something went wrong!')

    else:
        tkinter.messagebox.showwarning(
            title="Error", message="Bad boy make sure all input is filled to avoid error.")


# set frame
frame_res = tkinter.Frame(window, border=3)
frame_res.grid(row=0, column=0, padx=20, pady=10)

# label
aka_label = tkinter.LabelFrame(frame_res, text="result will show up here",
                               fg="black", bg="#f3f3f3", font=("monospace 10"))
aka_label.pack()


# text inout frame
frame = tkinter.Frame(window)
frame.grid(row=1, column=0)

# Saving User Info
mail_bomber_frame = tkinter.LabelFrame(frame, text="MAIL BOMBER")
mail_bomber_frame.grid(row=0, column=0, padx=20, pady=10)

mail_sender_label = tkinter.Label(mail_bomber_frame, text="MAIL SENDER")
mail_sender_label.grid(row=0, column=0)


password_label = tkinter.Label(mail_bomber_frame, text="Sender password")
password_label.grid(row=2, column=0)
topic_label = tkinter.Label(mail_bomber_frame, text="Topic")
topic_label.grid(row=2, column=1)


Html_label = tkinter.Label(mail_bomber_frame, text="Html template code")
Html_label.grid(row=4, column=0)
Host_sender_label = tkinter.Label(mail_bomber_frame, text="Sender Host")
Host_sender_label.grid(row=4, column=1)

port_label = tkinter.Label(mail_bomber_frame, text="Sender port")
port_label.grid(row=6, column=0)


sneder_entry = tkinter.Entry(mail_bomber_frame)
sneder_entry.grid(row=1, column=0)


password_entry = tkinter.Entry(mail_bomber_frame)
topic_entry = tkinter.Entry(mail_bomber_frame)
password_entry.grid(row=3, column=0)
topic_entry.grid(row=3, column=1)


html_entry = tkinter.Entry(mail_bomber_frame)
host_entry = tkinter.Entry(mail_bomber_frame)
html_entry.grid(row=5, column=0)
host_entry.grid(row=5, column=1)


port_entry = tkinter.Entry(mail_bomber_frame)
port_entry.grid(row=7, column=0)


for widget in mail_bomber_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Upload CSV")
terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

uploadbtn = tkinter.Button(terms_frame, text="click here to upload.",
                           command=import_csv_data)
uploadbtn.grid(row=0, column=0, padx=20, pady=10)

# Button
button = tkinter.Button(frame, text="Run", command=enter_data)
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)


window.mainloop()
