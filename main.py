# This is a sample Python script.
# pip install SpeechRecognition
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import speech_recognition as sr

# FILE = 'audio.wav'
# FILE = 'astro.wav'
FILE = './wav/15.wav'

r = sr.Recognizer()
with sr.AudioFile(FILE) as source:
    audio = r.record(source)  # read the entire audio file

#source = sr.AudioFile(FILE).__enter__()
#audio = r.record(source)

try:
    text = r.recognize_google(audio, language='ru-RU')
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



'''
class TestWith:
    def __enter__(self):
        print('Вход')
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выход')


with TestWith() as test:
    print('Выполнение кода внутри with')
    print(test)
'''