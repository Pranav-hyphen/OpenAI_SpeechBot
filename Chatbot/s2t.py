import speech_recognition as sr

listener = sr.Recognizer()

class S2T:
    def __init__(self):
        self.listener = sr.Recognizer()

    def process(self):
        try:
            with sr.Microphone() as source :
                self.listener.energy_threshold = 10000
                self.listener.adjust_for_ambient_noise(source,1.2)
                print("Speak now....")
                voice = self.listener.listen(source)
                data = self.listener.recognize_google(voice,language="en_gb")
                print(data) 
            prompt = data
            if prompt.lower() in ["quit","bye","goodbye"] :
                prompt = 'BYE'
                print("Bye have a great time")
            return prompt  
        except Exception as ex:
            print(f"Exception caught! {ex}")
            return "Pardon me! Can you speak a little louder?"
        


