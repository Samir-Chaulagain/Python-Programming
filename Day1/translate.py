
from gtts import gTTS
from googletrans import Translator
import os
translator = Translator()
text = input("Enter the text to translate and speak: ")
src_lang = "en" # English
dest_lang = "fr" # French
translated_text = Translator().translate(text, src="en", dest="fr")
tts = gTTS(translated_text.text, lang=dest_lang)
tts.save("translated_audio.mp3")
# Play the audio file using the os library
os.system("mpg321 translated_audio.mp3")
