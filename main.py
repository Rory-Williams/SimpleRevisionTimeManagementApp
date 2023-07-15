from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Timer Program')

# window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW) #add padding to window component

my_label = Label(text='Timer', font=('Arial',24,'bold'), fg=GREEN, bg=YELLOW)
my_label.grid(column=2,row=1)
my_label.config(padx=20, pady=20)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
canvas.grid(column=2,row=2)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

tick = ' '
tick_label = Label(text=tick, font=('Arial',16,'bold'), fg=GREEN, bg=YELLOW)
tick_label.grid(column=2,row=4)
tick_label.config(padx=20, pady=20)

cont = True
def but_go():
    global REPS
    global cont
    global tick
    cont = True
    REPS += 1
    work = WORK_MIN*60
    lbreak = LONG_BREAK_MIN*60
    sbreak = SHORT_BREAK_MIN*60

    if not REPS%8:
        time_funct(4)
        my_label.config(text='long rest', fg=RED)
    elif not REPS%2:
        time_funct(2)
        my_label.config(text='rest', fg=PINK)
    else:
        time_funct(5)
        my_label.config(text='work', fg=GREEN)

    if REPS%2 == 0:
        tick += '✔'
        tick_label.config(text=tick)


def but_reset():
    global cont
    global REPS
    print('click reset')
    cont = False
    REPS = 0
    time_funct(0)
    my_label.config(text='TIMER', fg=GREEN)
    tick = ' '
    tick_label.config(text=tick)

button_go = Button(text='Start', command=but_go)
button_go.grid(column=1,row=3)
button_go.config(padx=20, pady=20)
button_reset = Button(text='Reset', command=but_reset)
button_reset.grid(column=3,row=3)
button_reset.config(padx=20, pady=20)



def add_zero(string):
    if len(string) < 2:
        return '0'+string
    else:
        return string

def time_funct(total_secs):
    global cont
    if total_secs > 0 and cont:
        window.after(1000, time_funct, total_secs-1)
    elif cont:
        but_go()
    print('timing')
    mins = total_secs//60
    secs = total_secs%60
    secs_string = add_zero(str(secs))
    mins_string = add_zero(str(mins))
    canvas.itemconfig(timer_text, text=f'{mins_string}:{secs_string}')



window.mainloop()