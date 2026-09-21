import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

try:
    os.mkdir("temp")
except:
    pass

st.subheader("Atención Acudiente")
st.write('Esta es una app para enseñarle a tus hijos a leer.'  
         ' Antes que nada, asegurate de que tu hijo/a ya sepa como mínimo distinguir las letras del alfabeto.' 
         ' La idea es que el pueda escribir las letras, palabras o frases que ve, y el programa se las leera.'   
         ' NOTA: Esta aplicación no reemplaza los estudios escolares, solo funciona como una ayuda y/o refuerzo.' 
         '  '
        
        )
           
st.title("Conversión de Texto a Audio")
image = Image.open('IMG_1037.jpeg')
st.image(image, width=350)
        
st.markdown(f"Escribe:")
text = st.text_area("Texto")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("Convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tu audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;800&family=Comic+Neue:wght@400;700&display=swap');

.stApp {
    background-color: #FFF6E9;
    background-image: radial-gradient(#FFE3B3 1.5px, transparent 1.5px);
    background-size: 22px 22px;
}

h1, h2, h3, .stMarkdown h1, .stMarkdown h2 {
    font-family: 'Baloo 2', cursive !important;
    color: #6B4226 !important;
}
h1 { color: #E4572E !important; }

p, li, label, div[data-testid="stMarkdownContainer"], .stMarkdown {
    font-family: 'Comic Neue', cursive !important;
    font-size: 1.15rem !important;
    color: #4A3728 !important;
}

div[data-testid="stImage"] img {
    border-radius: 18px;
    border: 6px solid #FFD447;
    box-shadow: 4px 4px 0px #E4572E;
}

textarea, .stTextArea textarea {
    font-family: 'Comic Neue', cursive !important;
    font-size: 1.1rem !important;
    background-color: #FFFDF7 !important;
    color: #4A3728 !important;
    caret-color: #4A3728 !important;
    border: 3px solid #A9CBA4 !important;
    border-radius: 16px !important;
}

div[data-baseweb="select"] > div {
    border: 3px solid #A9CBA4 !important;
    border-radius: 16px !important;
    background-color: #FFFDF7 !important;
    font-family: 'Comic Neue', cursive !important;
}

.stButton button {
    font-family: 'Baloo 2', cursive !important;
    background-color: #F7B32B !important;
    color: #4A3728 !important;
    border: 3px solid #E4572E !important;
    border-radius: 20px !important;
    padding: 8px 24px !important;
    box-shadow: 3px 3px 0px #E4572E;
}
.stButton button:hover {
    background-color: #FFD447 !important;
}

audio {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)
