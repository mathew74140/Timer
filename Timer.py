from tkinter import *

sample = Tk()
# property
sample.geometry("500x200")
sample.resizable(False, False)
sample.title('Timer')

# variables
timer = None
hour = 0
min = 0
sec = 0


def update_labels():
    """Update all time labels in proper format"""
    lbl_h.config(text=hour)
    lbl_min.config(text=f"{min:02d}")
    lbl_sec.config(text=f"{sec:02d}")


# === Functions for Up/Down buttons ===
def fun_up_h():
    global hour
    hour += 1
    update_labels()


def fun_down_h():
    global hour
    if hour > 0:
        hour -= 1
        update_labels()


def fun_up_min():
    global min
    if min < 59:  # max 59
        min += 1
        update_labels()


def fun_down_min():
    global min
    if min > 0:
        min -= 1
        update_labels()


def fun_up_sec():
    global sec
    if sec < 59:  # max 59
        sec += 1
        update_labels()


def fun_down_sec():
    global sec
    if sec > 0:
        sec -= 1
        update_labels()


# === Timer logic ===
def countdown():
    global timer, sec, min, hour
    but_start.config(state=DISABLED)  # prevent multiple timers

    if hour == 0 and min == 0 and sec == 0:
        but_reset.config(state=DISABLED)
        but_stop.config(state=DISABLED)
        return
    else:
        but_stop.config(state=NORMAL)
        but_reset.config(state=DISABLED)

    if sec == 0:
        if min == 0:
            if hour > 0:
                hour -= 1
                min = 59
                sec = 59
        else:
            min -= 1
            sec = 59
    else:
        sec -= 1

    update_labels()
    timer = lbl_sec.after(1000, countdown)


def stop():
    global timer
    if timer:
        but_reset.config(state=NORMAL)
        lbl_sec.after_cancel(timer)
        timer = None


def reset():
    global sec, min, hour, timer
    if timer:
        lbl_sec.after_cancel(timer)
        timer = None
    sec, min, hour = 0, 0, 0
    update_labels()
    but_start.config(state=NORMAL)
    but_reset.config(state=DISABLED)
    but_stop.config(state=DISABLED)


# === Widgets ===
lbl_hshow = Label(text='h', font='arial 15 bold')
lbl_hshow.place(x=175, y=10)

but_up_h = Button(text="^", font='arial 20', command=fun_up_h)
but_up_h.place(x=170, y=40, width=30, height=30)

lbl_h = Label(text='0', font='arial 25 bold')
lbl_h.place(x=175, y=70)

but_down_h = Button(text="\/", font='arial 13 bold', command=fun_down_h)
but_down_h.place(x=170, y=110, width=30, height=30)

label1 = Label(text=':', font='arial 25 bold')
label1.place(x=197, y=68)

lbl_minshow = Label(text='min', font='arial 15 bold')
lbl_minshow.place(x=210, y=10)

but_up_min = Button(text="^", font='arial 20', command=fun_up_min)
but_up_min.place(x=210, y=40, width=40, height=30)

lbl_min = Label(text='00', font='arial 25 bold')
lbl_min.place(x=210, y=70)

but_down_min = Button(text="\/", font='arial 13 bold', command=fun_down_min)
but_down_min.place(x=210, y=110, width=40, height=30)

label2 = Label(text=':', font='arial 25 bold')
label2.place(x=252, y=68)

lbl_secshow = Label(text='sec', font='arial 15 bold')
lbl_secshow.place(x=270, y=10)

but_up_sec = Button(text="^", font='arial 20', command=fun_up_sec)
but_up_sec.place(x=270, y=40, width=40, height=30)

lbl_sec = Label(text='00', font='arial 25 bold')
lbl_sec.place(x=270, y=70)

but_down_sec = Button(text="\/", font='arial 13 bold', command=fun_down_sec)
but_down_sec.place(x=270, y=110, width=40, height=30)

but_start = Button(text='Start', font='arial 15', command=countdown)
but_start.place(x=100, y=150)

but_stop = Button(text='Stop', font='arial 15', state=DISABLED, command=stop)
but_stop.place(x=190, y=150)

but_reset = Button(text='Reset', font='arial 15', state=DISABLED, command=reset)
but_reset.place(x=290, y=150)

update_labels()
sample.mainloop()
