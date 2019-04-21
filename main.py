import tkinter as tk
import RPi.GPIO as GPIO
# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
#
#
root = tk.Tk()

v = tk.IntVar()
v.set(0)  # initialising the choice to 0 - RED
languages = [
    ("Red"),
    ("White"),
    ("Blue"),
    ("Exit")
]

def ShowChoice():
    print(v.get())
    res = v.get()
    if res == 0:
        red()
    elif res == 1:
        white()
    elif res == 2:
        blue()
    else:
        killIt()

def off():
    GPIO.output(7, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)

def red():
    off()
    GPIO.output(18, GPIO.HIGH)

def white():
    off()
    GPIO.output(15, GPIO.HIGH)

def blue():
    off()
    GPIO.output(7, GPIO.HIGH)

def killIt():
    root.destroy()

tk.Label(root,
         text="""Select a LED:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
red()
root.mainloop()
GPIO.cleanup()
