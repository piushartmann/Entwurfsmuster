class Hund():
    def __init__(self, größe=0, gewicht=0, farbe="schwarz"):
        self.größe = größe
        self.gewicht = gewicht
        self.farbe = farbe
    def summary(self, Type):
        print("Größe:", self.größe, "Gewicht:", self.gewicht, "Farbe:", self.farbe, "Hund:", Type)
        print("Bellen:", self._bellverhalten.__class__.__name__, "Laufen:", self._laufverhalten.__class__.__name__)

class Bellverhalten():
    def bellen(self):
        pass
    
    class LeiseBellen():
        def bellen(self):
            print("(wuff)")
    
    class LautBellen():
        def bellen(self):
            print("WUFF")

    class NormalBellen():
        def bellen(self):
            print("Wuff")

class Laufverhalten():
    def laufen(self):
        pass
    
    class LangsamLaufen():
        def laufen(self):
            print("Ich laufe langsam")
    
    class SchnellLaufen():
        def laufen(self):
            print("Ich laufe schnell")

class Husky(Hund):
    def __init__(self, größe=0, gewicht=0, farbe="weiß", bellverhalten = Bellverhalten.NormalBellen(), laufverhalten = Laufverhalten.SchnellLaufen()):
        Hund.__init__(self, größe, gewicht, farbe)
        self._bellverhalten = bellverhalten
        self._laufverhalten = laufverhalten
        Hund.summary(self, "Husky")

    def bellen(self):
        self._bellverhalten.bellen() 

    def laufen(self):
        self._laufverhalten.laufen()
        
class Bulldogge(Hund):
    def __init__(self, größe=0, gewicht=0, farbe="schwarz", bellverhalten = Bellverhalten.LautBellen(), laufverhalten = Laufverhalten.LangsamLaufen()):
        Hund.__init__(self, größe, gewicht, farbe)
        self._bellverhalten = bellverhalten
        self._laufverhalten = laufverhalten
        Hund.summary(self, "Bulldogge")

    def bellen(self):
        self._bellverhalten.bellen()

    def laufen(self):
        self._laufverhalten.laufen()

class Pudel(Hund):
    def __init__(self, größe=0, gewicht=0, farbe="braun", bellverhalten = Bellverhalten.LeiseBellen(), laufverhalten = Laufverhalten.LangsamLaufen()):
        Hund.__init__(self, größe, gewicht, farbe)
        self._bellverhalten = bellverhalten
        self._laufverhalten = laufverhalten
        Hund.summary(self, "Pudel")

    def bellen(self): 
        self._bellverhalten.bellen()

    def laufen(self):    
        self._laufverhalten.laufen()

if __name__ == "__main__":
    husky = Husky(10, 5, "weiß", Bellverhalten.NormalBellen())
    bulldogge = Bulldogge(5, 20, "schwarz", Bellverhalten.LautBellen())
    pudel = Pudel(3, 2, "braun", Bellverhalten.LeiseBellen())
    husky.bellen()
    bulldogge.bellen()
    pudel.bellen()