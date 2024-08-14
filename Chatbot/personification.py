from t2s import T2S
from s2t import S2T
from config import C

class Personification():
    def __init__(self):
        self.tts = T2S()
        self.stt = S2T()

    def s2t2s(self):
        self.tts.greet()
        x=0
        a = 2 # you can change the value of variable 'a' depending on size of response required
        while x < a:
            data = self.stt.process()
            spk = self.tts.Process_t2s(data)
            lst = spk.split(".")
            if len(lst) > 2:
                lst = lst[0]+"."+lst[1]+"."
            else:
                lst = lst
            self.tts.speak(lst)
            x=x+1


person = Personification()
person.s2t2s()
