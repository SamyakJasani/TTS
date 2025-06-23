import streamlit as st
from gtts import gTTS
from io import BytesIO


st.title("🎙️ Text to Speech")

text = st.text_area("Enter text:", "Type your text here...", height=150)

if st.button("Convert and Download"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        tts = gTTS(text=text, lang="en", slow=False)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        st.audio(mp3_fp, format="audio/mp3")
        st.download_button("Download MP3", mp3_fp, file_name="textToSpeech.mp3", mime="audio/mpeg")
