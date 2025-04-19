import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="EchoScipt    ")
st.title("Welcome to EchoScipt")
st.header("A 'Text to Speech' WebApp by Harsh Gupta")

# User input
text = st.text_input("Enter text to convert to speech:")

# Language selection
language = st.selectbox("Select Language", ["English", "Hindi"])

# Convert and Play Button
if st.button("Convert and Play"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        # Set language code
        lang_code = 'en' if language == "English" else 'hi'

        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name

        # Generate speech using gTTS
        try:
            tts = gTTS(text=text, lang=lang_code)
            tts.save(filename)

            # Play audio in browser
            st.audio(filename, format="audio/mp3")

            # Download button
            with open(filename, "rb") as audio_file:
                audio_bytes = audio_file.read()

            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="speech.mp3",
                mime="audio/mp3"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")

        # Optional: Delete the temp file afterwards
        if os.path.exists(filename):
            os.remove(filename)
