from cgitb import text
from tkinter import *

# --------------------- FUNCTIONS ---------------------


# ---------------------- UI SETUP ----------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flash_card = Canvas(
    width=800, height=520, highlightthickness=0, background=BACKGROUND_COLOR
)
card_front = PhotoImage(file="images/card_front.png")
flash_card.create_image(400, 260, image=card_front)
flash_card.grid(column=0, columnspan=2, row=0)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, borderwidth=0)
correct_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=1, row=1)

window.mainloop()
