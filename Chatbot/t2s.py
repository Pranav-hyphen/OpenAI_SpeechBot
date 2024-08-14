import pyttsx3
from s2t import S2T
from config import C
from datetime import datetime
from openai import OpenAI


class T2S:
    def __init__(self):
        c = C()
        self.client = OpenAI(api_key=c.get_value("openai_api_key"))
        # self.s2t = S2T()
        self.tts = pyttsx3.init()

    def Process_t2s(self,prompt):
        self.prompt = prompt
        self.response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": self.prompt},
         ]
        )
        gptans = self.response.choices[0].message.content.strip()
        return gptans

    def speak(self,gptans):
        self.tts.say(gptans)
        self.tts.runAndWait()

    def greet(self):
        current_hour = datetime.now().time().hour
        if 6 <= current_hour < 12:
            greetings = 'good morning'
        elif 12 <= current_hour < 16:
            greetings = 'good afternoon'
        elif 16 <= current_hour < 20:
            greetings = 'good evening'
        else :
            greetings = 'good night'

        self.tts.say('Hello user')

        print("hello user")
        self.tts.runAndWait()
        print(greetings)
        self.tts.say(greetings)
        self.tts.runAndWait()


