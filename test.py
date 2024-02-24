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
            

class Hund():
    def __init__(self, type, größe=0, gewicht=0, farbe="schwarz", bellverhalten = Bellverhalten.NormalBellen(), laufverhalten = Laufverhalten.LangsamLaufen()):
        self._größe = größe
        self._gewicht = gewicht
        self._farbe = farbe
        self._bellverhalten = bellverhalten
        self._laufverhalten = laufverhalten
        self._type = type
        self.summary()

    def summary(self):
        print("Größe:", self._größe, "Gewicht:", self._gewicht, "Farbe:", self._farbe, "Hund:", self._type)
        print("Bellen:", self._bellverhalten.__class__.__name__, "Laufen:", self._laufverhalten.__class__.__name__)
        print("")

    def bellen(self):
        self._bellverhalten.bellen() 
    
    def laufen(self):
        self._laufverhalten.laufen()



class Husky(Hund):
    def __init__(self, type, größe, gewicht, farbe, bellverhalten, laufverhalten):
        Hund.__init__(self, type, größe, gewicht, farbe, bellverhalten, laufverhalten)
        
class Bulldogge(Hund):
    def __init__(self, type, größe, gewicht, farbe, bellverhalten, laufverhalten):
        Hund.__init__(self, type, größe, gewicht, farbe, bellverhalten, laufverhalten)

class Pudel(Hund):
    def __init__(self, type, größe, gewicht, farbe, bellverhalten, laufverhalten):
        Hund.__init__(self, type, größe, gewicht, farbe, bellverhalten, laufverhalten)


if __name__ == "__main__":
    husky = Husky("Husky", 10, 5, "weiß", Bellverhalten.NormalBellen(), Laufverhalten.SchnellLaufen())
    bulldogge = Bulldogge("Bulldogge", 5, 20, "schwarz", Bellverhalten.LautBellen(), Laufverhalten.LangsamLaufen())
    pudel = Pudel("Pudel", 3, 2, "braun", Bellverhalten.LeiseBellen(), Laufverhalten.SchnellLaufen())
    newDog = Hund("Labradudel", 5, 10, "schwarz", Bellverhalten.NormalBellen(), Laufverhalten.LangsamLaufen())
    
    print("")

    husky.bellen()
    bulldogge.bellen()
    pudel.bellen()
    newDog.bellen()

    newDog.laufen()