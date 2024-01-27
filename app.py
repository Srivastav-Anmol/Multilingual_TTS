import streamlit as st
from gtts import gTTS  
import pygame
from io import BytesIO


def text_to_speech(text,lang):
    tts = gTTS(text=text, lang=lang)  # You can specify the language here, e.g., lang='en' for English
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()


def main():
    st.title("File to Speech Demo")
    target_language = st.selectbox("Select Your Preferred Language", ["en", "es", "fr", "de", "ja", "ko", "zh-CN"])
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file is not None: # if file is uploaded.
        file_contents = uploaded_file.read()
        try:
            text_to_speech(file_contents.decode('utf-8'),target_language)
            st.text("Captions:")
            st.write(file_contents.decode('utf-8'))  
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            uploaded_file.seek(0)


if __name__ == "__main__":
    main()
