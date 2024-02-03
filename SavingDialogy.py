import speech_recognition as sr
import pyttsx3
from chatGPT import GPT

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150) # встановлення швидкості відтворення
        self.engine.setProperty('voice', 'C:/Users/JeFan/Desktop/розробка сайтів/сайтобудівництво')  # встановлення голосу

        self.r = sr.Recognizer() # розпізнавання голосу
        self.gpt = GPT()

    def listen(self):
        while True:
            with sr.Microphone() as source:
                print('Говоріть:')
                audio = self.r.listen(source)

            try:
                text = self.r.recognize_google(audio, language='uk-UA')
                print('Розпізнане запитання:', text)  # виведення розпізнаного запитання
                yield text
            except sr.UnknownValueError:
                print('Мова не розпізнана')
            except sr.RequestError:
                print('Помилка сервера розпізнавання')

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def create_file(self, question, answer):
        with open('question_answer.txt', 'w',encoding='utf-8') as file:
            file.write('Питання: ' + question + '\n')
            file.write('Відповідь: ' + answer + '\n')

    def run(self):
        for task in self.listen():
            answer = self.gpt.request(task)
            self.say(answer) # озвучування відповіді
            self.create_file(task, answer)  # створення файлу з питанням та відповіддю

if __name__ == '__main__':
    sara = Assistant()
    sara.run()