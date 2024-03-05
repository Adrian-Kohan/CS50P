# Text to Speech Converter Documentation
#### Video Demo:  <URL https://youtu.be/CQJQRgCFGug?si=WbaWKsfSpMV4Ryoe>
#### Description:

**Introduction**

The Text to Speech Converter is a Python script designed to bridge the gap between written content and auditory experiences. Whether you’re a student, researcher, or simply someone who prefers listening over reading, this application empowers you to transform PDF documents into spoken words. Let’s delve deeper into its functionality and usage.

**Motivation**

Imagine having a lengthy research paper, an e-book, or a lecture transcript in PDF format. Reading through pages of text can be time-consuming and visually exhausting. That’s where our Text to Speech Converter comes to the rescue! By converting written content into audio, it opens up new possibilities:

Accessibility: Individuals with visual impairments can access textual information effortlessly.
Multitasking: Listen to academic papers or literature while commuting, exercising, or doing household chores.
Language Learning: Improve pronunciation and comprehension by hearing the text spoken aloud.
Customization: Adjust the speech rate, pitch, and language to suit your preferences.

**Dependencies**

Before diving into the technical details, let’s briefly discuss the essential dependencies:

**Tkinter:**

Tkinter is Python’s standard GUI toolkit.
It provides a set of tools for creating windows, buttons, labels, and other interactive elements in a user-friendly manner.
Our application relies on Tkinter to build the user interface.

**gTTS (Google Text-to-Speech):**

gTTS is a powerful library that converts text into speech.
It interfaces with Google’s Text-to-Speech API, allowing us to generate audio files from plain text.
Our application uses gTTS to create the spoken output.

**PyPDF2:**

PyPDF2 is a Python library specifically designed for working with PDF files.
It enables us to extract text content from PDFs.
Our application uses PyPDF2 to read and process the selected PDF file.


**Functionality**

**Main Function (main())**

Initializes the GUI window:

Sets the window title to “Text to Speech.”
Defines the window dimensions (550x450 pixels).
Configures the background color.
Sets up the following components within the window:
A label displaying “Select a PDF file.”
A canvas for visual elements (such as an image).
Two buttons: “Select PDF” and “Play Audio.”
Invokes the Tkinter main loop to display the GUI.

**Upload File Function (upload_file())**

Opens a file dialog:

Allows users to select a PDF file.
If a file is chosen, it triggers the convert_to_audio() function.
If no file is selected, it displays an error message.


**Convert Function (convert_to_audio(pdf_file))**

Reads the selected PDF file:

Creates a PDF reader object using PyPDF2.
Extracts text from each page of the PDF and concatenates it into a single string.
Converts text to speech:
Utilizes gTTS to convert the extracted text to speech in English.
Saves the generated audio as “sound.mp3.”
Displays a success message upon completion.

**Play Function (play_audio())**

Plays the generated audio:

Uses the default system player to play the “sound.mp3” file.

**Usage**

Run the script.

Click the “Select PDF” button to choose a PDF file.
After selecting the file, click the “Play Audio” button to convert the text to speech and play the audio.
A success message will confirm that the conversion is complete, and the audio will play using the system’s default player.

**Note**

Ensure that all required dependencies (Tkinter, gTTS, PyPDF2) are installed.
The script assumes that the PDF file contains extractable text (as opposed to scanned images).
The generated audio file is saved as “sound.mp3.”
