from project import select_pdf_file, convert_to_audio, play_audio
import pytest
import os


# A valid PDF file path for testing
VALID_PDF_FILE = "text-to-speech.pdf"


def test_select_pdf_file():
    # Test that select_pdf_file function returns a non-empty string
    # when a valid PDF file is selected.
    uploaded_file = select_pdf_file()
    assert uploaded_file != ""


def test_convert_to_audio():
    # Test that convert_to_audio function successfully converts PDF file to speech
    # by checking if "sound.mp3" file is created.
    convert_to_audio(VALID_PDF_FILE)
    assert os.path.exists("sound.mp3")


def test_play_audio():
    # Test that play_audio function executes without raising any errors.
    # Since play_audio function runs an external command, we'll just check if it executes.
    try:
        play_audio()
    except Exception as e:
        pytest.fail(f"play_audio function raised exception: {e}")

