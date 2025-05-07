from tkinter import *

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 20
SPEED = 200
BG_COLOR = "#4cad4b"
SNAKE_COLOR = "#d66733"
FOOD_COLOR = "#6743de"
direction = "down"
score = 0

def restart_match():
   score = 0

def center_window(window):
   screen_width = window.winfo_screenwidth()
   screen_height = window.winfo_screenheight()
   x = (screen_width - window.winfo_reqwidth()) // 3
   y = (screen_height - window.winfo_reqheight()) // 5
   window.geometry(f"+{x}+{y}")

window = Tk()
window.title('Sssssnake')

lbl = Label(window, text=f"Score: {score}", font=('Roman', 15), anchor="w")
lbl.pack(padx=5)

cnvs = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
cnvs.pack()

reset = Button(window, text="RESET", fg="red")
reset.pack(padx=10)

window.resizable(False, False)
center_window(window)
window.update()
window.mainloop()
