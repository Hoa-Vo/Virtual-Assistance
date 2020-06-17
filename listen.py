import speech_recognition

ear=speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    print("Listening")
    audio=ear.listen(mic)

try:
    user=ear.recognize_google(audio)
except:
    user=" "

print(user)
