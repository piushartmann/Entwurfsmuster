# PL Informatik – Pius Hartmann
**Erläutern** Sie den Grundgedanken von Entwurfmustern und gehen sie insbesondere auf die Klassifikation Erzeuger-, Struktur-, und Verhaltensmuster ein.

**Implementieren** sie exemplarische ein Entwurfmuster in Python

**Erörtern** sie die Vor- und Nachteile von Entwurfmuster.

Entwurfmuster sind auf der Objektorientierung basierte Lösungsansätze für Probleme, die bei komplexen Projekten eingesetzt werden können, um sie zu abstrahieren. Sie können dadurch besser einzeln angegangen werden. Ein Entwurfsmuster ist eine Schablone, mit deren Hilfe man ein Projekt planen kann, wodurch es übersichtlicher, besser zu verstehen und einfacher zu erweitern ist.
Es gibt drei unterschiedliche Hauptkategorien: Erzeuger-, Struktur-, und Verhaltensmuster. Die Erzeugermuster können ein Objekt auf unterschiedliche Art erstellen, was zu niedriger Code-Redundanz und höherer Flexibilität führt. Die Strukturmuster machen es einfacher, eine Klasse zu designen, die auch bei höherer Komplexität übersichtlich bleiben. Und die Verhaltensmuster erleichtern die Kommunikation und Interaktion zwischen Objekten, indem sie die Kommunikation standardisieren.
Innerhalb der drei Hauptkategorien gibt es Unterkategorien, wie zum Beispiel für die Erzeugungsmuster den „Builder“, für die Strukturmuster etwa den „Adapter“ und für die Verhaltensmuster die „Strategy“.  Für alle drei Hauptkategorien gibt es noch mehr Muster, aus Zeit- und Übersichtsgründen liegt der Fokus in dieser Dokumentation auf diesen drei Beispielen.
Für das weitere Verständnis ist im Folgenden eines von drei in Python implementierten Beispielen näher erläutert. In der Analogie eines Hausbaues, findet man Wände, Fenster, ein Dach und eine Tür. Aber nicht jedes Haus ist gleich. Manche haben eine Garage, einen Garten oder einen Pool. Auch können die Materialien sich von Haus zu Haus unterscheiden, die Wände des einen sind zum Beispiel aus Holz und von einem anderen aus Beton. Auf Python übertragen bedeutet dies, dass man im Konstruktor eines Objektes alle diese Parameter berücksichtigt.
Zur Verständlichkeit und Kürzung der Dokumentation wird hier Pseudocode verwenden. In der Implementierung können Abschnitte anders aussehen.


```
class House():	
    def __init__(walls, windows, door, garage, garden, pool, wallsMaterial, windowsMaterial, doorMaterial, garageMaterial, gardenMaterial, poolMaterial):

house = House(4, 6, 2, True, False, False, "Wood", "Wood", "Wood", "Wood", "Wood", "Wood")
Diese Art der Objekterstellung wird aber für diesen Zweck sehr schnell sehr unübersichtlich. Außerdem müsste man noch in der Klasse zusätzlichen Softwarecode, mit vielen „If statements“ schreiben, der dann zum Beispiel aussieht wie im Folgenden dargestellt:
if garage:
    buildGarage()
```
Daher kann man in dem Fall ein Erstellungsmuster anwenden: Der „Builder“ ist eine separate Klasse, welche hier die Funktion „buildWalls“ hat, welche alles Nötige tut, um die Wände zu bauen. Das Objekt „Haus“ braucht nur noch eine Funktion, durch die die Wände zum Objekt hinzugefügt werden können. In Python könnte das wie im Folgenden dargestellt aussehen.
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
Auch kann man nun verschiedene „Builder“ für unterschiedliche Materialen definieren. Zum Beispiel kann man einen „WoodHouseBuilder“ definieren, der alle Teile des Hauses aus Holz konstruiert, oder einen „ConcreteHouseBuilder“ der alles aus Beton baut. So kann der Code zum Erstellen eines Holzhauses oder eines Hauses aus Beton vereinfacht und übersichtlicher gemacht werden. Die Implementierung für ein Holzhaus könnte wie folgt dargestellt sein.

builder = WoodHouseBuilder()
builder.buildWalls(4)
builder.buildRoof()
builder.buildWindows(6)
builder.buildDoors(2)

Wenn man sich jetzt viele Holzhäuser vorstellt und alle oder viele ihrer Komponenten gleich sind, kann man auch einen Director benutzten, welcher diese standardisierten Abläufe ausführen kann. Dies ist ebenfalls unten dargestellt.
```
class Director():
    def __init__(self):
        self._builder = None

    def buildStandardHouse(self):
        #anweisungen zum bauen eines standard hauses
    
    def buildLuxuryHouse(self):
        #anweisungen zum bauen eines luxus hauses
```
Die großen Vorteile der Entwurfsmuster sind bei richtiger Anwendung ein besseres Verständnis des Softwarecodes. Dies gilt auch für weitere am Projekt beteiligte Softwareentwickler, da die Klassenstruktur immer unverändert bleibt. Dadurch wird auch die Flexibilität und Erweiterbarkeit des Projektes erhöht, da alle Beteiligten das Projekt nachvollziehen und schnell Änderungen und Verbesserungen vornehmen können. Die Flexibilität wird auch dadurch erhöht, dass durch viele Entwurfsmuster die Repetition dramatisch verringert wird. Man muss beispielsweise nur einen Parameter ändern, um ein Verhalten anzupassen ohne den Softwarecode erweitern oder anpassen zu müssen. Komplexe Entwurfmuster können jedoch auch manchmal nicht einfach nachvollziehbar sein, wodurch es eine längere Lernphase geben kann, in der man sich mit den Entwurfmustern vertraut machen muss.

Insgesamt kann eine richtige Implementierung der Entwurfsmuster die Entwicklung beschleunigen und die Zusammenarbeit unterstützen. Jedoch bei weniger Komplexen Projekten sind die Entwurfmuster nicht immer sinnvoll.
Entwurfmustern vertraut machen muss.

### Quellen:

[Philipp hauer design patterns](https://www.philipphauer.de/study/se/design-pattern/strategy.php)

[Refactoring Guru](https://refactoring.guru/)

ChatGPT für Inspiration
