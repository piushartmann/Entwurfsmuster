# PL Informatik – Pius Hartmann
Erläutern Sie den Grundgedanken von Entwurfmustern und gehen sie insbesondere auf die Klassifikation Erzeuger-, Struktur-, und Verhaltensmuster ein.
Implementieren sie exemplarische ein Entwurfmuster in Python
Erörtern sie die Vor- und Nachteile von Entwurfmuster.

Entwurfmuster sind auf der Objektorientierung basierte Lösungsansätze für Probleme, die bei komplexen Projekten eingesetzt werden können, um Probleme zu abstrahieren, damit sie einzeln angegangen werden können. Ein Entwurfsmuster ist eine Schablone, mit der man Probleme besser angehen kann, wodurch das Projekt übersichtlicher, besser zu verstehen wird und einfacher zu erweitern
Es gibt drei unterschiedliche Hauptkategorien: Erzeuger-, Struktur-, und Verhaltensmuster. Die Erzeuger können ein Objekt auf unterschiedliche Art erstellen, was zu höher Code wieder Verwendbarkeit und Flexibilität führt. Die Strukturmuster machen es einfacher eine Klasse zu designen, die auch bei höherer Komplexität übersichtlich bleiben. Und die Verhaltensmuster erleichtern die Kommunikation und Interaktion zwischen Objekten, indem sie die Kommunikation standardisieren.
Innerhalb der drei Hauptkategorien gibt es Unterkategorien, wie zum Beispiel für die Erzeugungsmuster den „Builder“, für die Strukturmuster etwa den „Adapter“ und für die Verhaltensmuster die „Strategy“.  Für alle drei Hauptkategorien gibt es noch mehr, aber ich werde mich aus Zeit und übersichtsgründen auf diese drei Beispiele Fokussieren. 
In Python habe ich diese drei Beispiele implementiert, ich werde hier eines genauer erläutern. Zum Beispiel wollen wir ein Haus bauen. Um ein Haus zu bauen, braucht man Wände, Fenster, ein Dach und eine Tür. Aber nicht jedes Haus ist gleich, manche haben eine Garage, einen Garten oder einen Pool. Auch können die Materialien sich von Haus zu Haus unterscheiden, die Wände des einen sind zum Beispiel aus Holz und von einem anderen aus Beton. Nun kann man Kann man Code schreiben, der im Konstruktor eines Objektes alle diese Parameter berücksichtigt. Zur Verständlichkeit benutze ich Pseudocode in diesem Dokument, also der echte Code in meiner Implementierung ist anders und der Code hier würde so nicht funktionieren. 
```
class House():	
    def __init__(walls, windows, door, garage, garden, pool, wallsMaterial, windowsMaterial, doorMaterial, garageMaterial, gardenMaterial, poolMaterial):

house = House(4, 6, 2, True, False, False, "Wood", "Wood", "Wood", "Wood", "Wood", "Wood")
Diese Objekt Erstellung, wird aber sehr schnell sehr unübersichtlich, da man zusätzlich auch noch Code schreiben muss, der dann zum Beispiel die Garage baut:
if garage:
    buildGarage()
```
Daher kann man in dem Fall ein Erstellungsmuster anwenden: Der „Builder“ ist eine separate Klasse, welche zum Beispiel die Funktion „buildWalls“ hat, welche alles Nötige tut, um die Wände zu bauen, und das Haus Objekt braucht nur noch eine Funktion, sodass die Wände zu dem Objekt hinzugefügt werden können.
```
class House():
    def __init__(self):
        self.parts = []

    def addPart(self, part):
        self.parts.append(part)

class builder():
    def __init__(self):
        self._house = House()

    def buildWalls(self, number=4):
        self._house.addPart(f"{number} Walls")
```
Auch kann man nun verschiedene Builder für unterschiedliche Materialen, so kann man einen „WoodHouseBuilder“ haben, der alle Teile des Hauses aus Holz Konstruieren kann, oder einen „ConcreteHouseBuilder“ der alles aus Beton baut. So kann der Code zum erstellen eines Holz Hauses vereinfacht und übersichtlicher gemacht werden:
builder = WoodHouseBuilder()
builder.buildWalls(4)
builder.buildRoof()
builder.buildWindows(6)
builder.buildDoors(2)

Wenn man jetzt zum Beispiel viele Holzhäuser baut und alle oder viele ihrer Komponenten gleich sind, kann man auch einen Director benutzten, dass ist eine weitere Klasse, die die Builder anweisen kann was er bauen soll.
```
class Director():
    def __init__(self):
        self._builder = None

    def buildStandardHouse(self):
        #anweisungen zum bauen eines standard hauses
    
    def buildLuxuryHouse(self):
        #anweisungen zum bauen eines luxus hauses
```
Die großen Vorteile, wenn man die Entwurfmuster richtig anwendet, sind ein besseres Verständnis von Code, auch für andere Entwickler, da die Struktur immer gleichbleibt. Dadurch wird auch die Flexibilität und Erweiterbarkeit des Projektes erhöht, da alle beteiligten das Projekt verstehen können und schnell Änderungen und Verbesserungen vornehmen können. Die Flexibilität wird auch dadurch erhöht, dass durch viele Entwurfsmuster die Repetition dramatisch verringert wird. Man muss also nur zum Beispiel einen Parameter ändern, um ein Verhalten zu ändern und nicht viel neuen Code schreiben. Einige Entwurfmuster können zu Beginn allerdings nicht intuitiv sein, wodurch es eine längere Lernphase geben kann, in der man sich mit den Entwurfmustern vertraut machen muss.

