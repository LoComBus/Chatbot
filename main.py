import tkinter
import tkinter as tk
import openai
from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
import time



black = '#170522'
green = '#35C08F'
beige = '#F1F2E4'
dark_red = '#C60C30'
red = '#E84A58'
white = '#FFFFFF'


font = "Helvetica 14"
font_bold = "Helvetica 13 bold"
title = "Futura 24 bold"

openai.api_key="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"
model_engine = "text-davinci-003"

class Chat_app:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self._load_most_asked_questions()



    def run(self):
        self.window.mainloop()


    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=393, height=852, bg=dark_red)


        # head label
        head_label = Label(self.window, bg=red, fg=black, text="Ask Anna Anything", font=title, pady=15)
        head_label.place(relwidth=1, relheight=0.1)


        #image thing
        image = Image.open("Anna_bot2.png")
        resized_image = image.resize((50, 50))
        self.converted_image = ImageTk.PhotoImage(resized_image)

        label = tk.Label(head_label, image=self.converted_image, bg = red)
        label.place(x=10,y=12)



        # tiny divider
        line = Label(self.window, width=380, bg=black)
        line.place(relwidth=1, rely=0.1, relheight=0.012)


        # text widget
        self.text_widget = Text(self.window, bg=white, fg=black, font=font, padx=10, pady=10, wrap=WORD)
        self.text_widget.place(relheight=0.9, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.window)
        scrollbar.place(relheight=0.84, relx=0.974,rely=0.083)
        scrollbar.configure(command=self.text_widget.yview)

        # attach scrollbar to text widget
        self.text_widget.config(yscrollcommand=scrollbar.set)

        # bottom label
        bottom_label = Label(self.window, bg=red, height=60, width=50)
        bottom_label.place(relwidth=1,rely=0.9)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=beige, fg=black)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.01, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # most asked button
        most_asked_button = Button(bottom_label, text="Most Asked", width=20, bg=beige, fg=black,
                                   command=self._most_asked, pady=10)
        most_asked_button.place(relx = 0.77, rely = 0.01, relheight = 0.06, relwidth = 0.22)

    def play_sound(self):
        playsound('boten_anna.mp3', block=False)




    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        self.msg_entry.delete(0, END)
        self._get_bot_response(msg)

    def _insert_message(self, msg, sender):
        if not msg:
            return
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.text_widget.see(END)

    def _get_bot_response(self, user_input):
        prompt = f"{user_input}\nAnna:"
        response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1000)
        text = response.choices[0].text
        self._insert_message(text.strip(), "Anna")
        


    def _most_asked(self):
        # create a pop-up box
        popup = Toplevel()
        popup.title("Most Asked Questions")
        popup.geometry("300x300")
        popup.configure(bg=dark_red)

        # display most asked questions in the pop-up box
        for question in self.most_asked_questions:
            label = Label(popup, text=question, font=font_bold, bg=dark_red, fg=beige)
            label.pack(pady=5)


    def _load_most_asked_questions(self):
        # load most asked questions from a file or database
        self.most_asked_questions = ["What is a good café in copenhagen?", "What is a regular danish dish?", "What is Sankthansaften?","What is mit-id?","How do i fix my årsopgørelse?"]





Chat_app().run()
