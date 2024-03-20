from pypdf import PdfReader
from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os


def convert_file():
    file_path = filedialog.askopenfilename(title="Open PDF File", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save("example.mp3")
        os.system("start example.mp3")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PDF to Audiobook Converter")
window.config(padx=100, pady=50)

open_button = Button(text="Open PDF", command=convert_file)
open_button.grid()

exit_button = Button(window, text = "Exit", command = window.quit)
exit_button.grid()

window.mainloop()