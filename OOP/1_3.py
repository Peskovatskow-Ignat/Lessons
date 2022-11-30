class Animal():

    def __init__(self, vid, voice):
        self.vi = vid
        self.vo = voice

    def GOLOS(self):
        print('Животное говорит', self.vo)

Egnyt = Animal('Барящек', 'Кушать хочется')
Egnyt.GOLOS()
print(Egnyt.vi)
katikovka = Animal('Птичка', 'курлык - курлык')
print(katikovka.vi)
katikovka.GOLOS()