from t2s import T2S
from s2t import S2T
from config import C

class main():
    def __init__(self):
        self.tts = T2S()
        self.stt = S2T()

    def s2t2s(self):
        self.tts.greet()
        x=0
        # you can change the value of variable 'a' depending on the number of question you want to ask
        # or you could put the while in infinite loop for continued conversation, until process is killed.
        a = 2 
        while x < a:
            data = self.stt.process()
            spk = self.tts.Process_t2s(data)
            lst = spk.split(".")
            # You can change the value of 2 here to control the size of response required.Higher the number, 
            # more likely the response will be larger.
            if len(lst) > 2:
                lst = lst[0]+"."+lst[1]+"."
            else:
                lst = lst
            self.tts.speak(lst)
            x=x+1


person = main()
person.s2t2s()
