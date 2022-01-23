"""
Flash Card Game Project
"""
from tkinter import Tk, Canvas, PhotoImage, Button
import random
from webbrowser import get
import pandas as pd

# --------------------- FUNCTIONS ---------------------

dataset = pd.read_csv("data/french_words.csv")
words_dict = dataset.to_dict(orient="records")
word = random.choice(words_dict)["French"]


def get_word():
    """Gets a new french word from the buttons"""
    new_word = random.choice(words_dict)["French"]
    flash_card.itemconfig(card_title, text="French")
    flash_card.itemconfig(card_word, text=f"{new_word}")


# ---------------------- UI SETUP ----------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flash_card = Canvas(
    width=800, height=523, highlightthickness=0, background=BACKGROUND_COLOR
)
card_front = PhotoImage(file="images/card_front.png")
flash_card.create_image(400, 263, image=card_front)
card_title = flash_card.create_text(
    400, 150, text="Language", font=("Arial", 40, "italic")
)
card_word = flash_card.create_text(400, 263, text=f"word", font=("Arial", 60, "bold"))
flash_card.grid(column=0, columnspan=2, row=0)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, borderwidth=0)
correct_button.config(command=get_word)
correct_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.config(command=get_word)
wrong_button.grid(column=1, row=1)

get_word()
window.mainloop()
