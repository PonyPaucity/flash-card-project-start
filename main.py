from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# words
word_dict = pd.read_csv("data/french_words.csv").to_dict(orient="records") # list of dicts


# canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text='Title', font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text='word', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# buttons
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image)
known_button.grid(row=1, column=1)

window.mainloop()
