"""
Flash Card Game Project
"""

from tkinter import Tk, Canvas, PhotoImage, Button
import random
import pandas as pd

# --------------------- FUNCTIONS ---------------------

try:
    dataset = pd.read_csv("data/words_to_learn.csv")
    print("Words to learn")
except FileNotFoundError:
    print("Full set")
    dataset = pd.read_csv("data/french_words.csv")

words_dict = dataset.to_dict(orient="records")

front_language = dataset.columns[0]
back_language = dataset.columns[1]

CURRENT_WORD = {}


def get_word():
    """Gets a new french word from the buttons"""
    global CURRENT_WORD, FLIP

    CURRENT_WORD = random.choice(words_dict)

    window.after_cancel(FLIP)

    flash_card.itemconfig(card_title, text=f"{front_language}", fill="black")
    flash_card.itemconfig(
        card_word, text=f"{CURRENT_WORD[f'{front_language}']}", fill="black"
    )
    flash_card.itemconfig(card_image, image=card_front)

    FLIP = window.after(3000, flip_card)


def flip_card():
    """Flips the card to the back language"""
    global CURRENT_WORD

    flash_card.itemconfig(card_image, image=card_back)
    flash_card.itemconfig(card_title, text=f"{back_language}", fill="white")
    flash_card.itemconfig(
        card_word, text=f"{CURRENT_WORD[f'{back_language}']}", fill="white"
    )


def knows_word():
    """User press the check button"""
    global CURRENT_WORD

    words_dict.remove(CURRENT_WORD)
    new_df = pd.DataFrame(data=words_dict)
    new_df.to_csv("data/words_to_learn.csv", index=False, mode="w")

    get_word()


def doesnot_knows_word():
    """User press the cross button"""
    get_word()


# ---------------------- UI SETUP ----------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


FLIP = window.after(3000, flip_card)

flash_card = Canvas(
    width=800, height=523, highlightthickness=0, background=BACKGROUND_COLOR
)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = flash_card.create_image(400, 263, image=card_front)
card_title = flash_card.create_text(
    400, 150, text="Language", font=("Arial", 40, "italic")
)
card_word = flash_card.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
flash_card.grid(column=0, columnspan=2, row=0)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, borderwidth=0)
correct_button.config(command=knows_word)
correct_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.config(command=doesnot_knows_word)
wrong_button.grid(column=1, row=1)

get_word()

window.mainloop()
