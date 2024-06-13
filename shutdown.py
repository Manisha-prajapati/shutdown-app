from tkinter import *
import os

def restart():
    execute_command("shutdown /r /t 1")

def restart_time():
    execute_command("shutdown /r /t 20")

def logout():
    execute_command("shutdown -l")

def shutdown():
    execute_command("shutdown /s /t 1")

def execute_command(command):
    try:
        os.system(command)
    except Exception as e:
        print("Error executing command:", e)

# Constants
WINDOW_SIZE = "500x500"
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60
BUTTON_FONT = ("Time New Roman", 20, "bold")

# Create the window
st = Tk()
st.title("ShutDown App")
st.geometry(WINDOW_SIZE)
st.config(bg="Blue")

# Create buttons
Button(st, text="Restart", font=BUTTON_FONT, relief=RAISED, cursor="plus", command=restart).place(x=150, y=70, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
Button(st, text="Restart Time", font=BUTTON_FONT, relief=RAISED, cursor="plus", command=restart_time).place(x=150, y=170, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
Button(st, text="Logout", font=BUTTON_FONT, relief=RAISED, cursor="plus", command=logout).place(x=150, y=270, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
Button(st, text="Shutdown", font=BUTTON_FONT, relief=RAISED, cursor="plus", command=shutdown).place(x=150, y=370, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)

# Start the main loop
st.mainloop()