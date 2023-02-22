from gtts import gTTS

# Replace the text with your own text
text = "Hello, this is a test."

# Initialize the TTS engine
tts = gTTS(text=text, lang="ja")

# Save the audio file as an MP3
tts.save("test.mp3")

from playsound import playsound
playsound("test.mp3")