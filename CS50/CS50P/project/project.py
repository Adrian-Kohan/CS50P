from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os
import PyPDF2
from tkinter import messagebox

FONT = ("Times New Roman", 30, "bold")


def select_pdf_file():
    try:
        # opening a pdf file
        f_types = [('PDF files', '*.pdf')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        if filename:
            convert_to_audio(filename)
        else:
            messagebox.showinfo(title="Oops", message="Please select a PDF file!")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {str(e)}")


def convert_to_audio(pdf_file):
    try:
        # creating a pdf file
        pdf = open(pdf_file, 'rb')

        # creating a pdf reader object
        pdf_reader = PyPDF2.PdfReader(pdf)

        text = ""
        # creating page objects
        for page in pdf_reader.pages:

            # extracting text from page
            text += page.extract_text()

        # closing the pdf file
        pdf.close()

        print(text)

        # Language in which you want to convert
        language = 'en'

        # Passing the text and language to the engine,
        speech = gTTS(text=text, lang=language, slow=False)
        # Saving the converted audio in a mp3 file
        speech.save("sound.mp3")
        messagebox.showinfo(title="Success", message="Conversion complete! You can play it now.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Conversion failed: {str(e)}")


def play_audio():
    try:
        # Play converted file
        os.system("sound.mp3")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Playback failed: {str(e)}")

def main():
    # Window Setup
    window = Tk()
    window.title("Text to Speech")
    window.geometry("550x450")
    window.config(padx=50, pady=50, bg="#EEEEEE")

    # Label Setup
    label = Label(width=20, text="Select a PDF file", font=FONT, fg="#3A98B9", background="#EEEEEE")
    label.grid(column=0, row=0)

    # Canvas Setup
    canvas = Canvas(width=400, height=224, bg="#EEEEEE", highlightthickness=0)
    img = PhotoImage(file="tts.png")
    canvas.create_image(200, 112, image=img)
    canvas.grid(column=0, row=1)

    # Buttons Setup
    button_select = Button(text='Select PDF', font=("Times New Roman", 15), width=15, command=select_pdf_file)
    button_select.grid(row=2, column=0)

    button_play = Button(text='Play Audio', font=("Times New Roman", 15), width=15, command=play_audio)
    button_play.grid(row=4, column=0)

    # Run the window's main loop
    window.mainloop()

if __name__ == "__main__":
    main()