class BarkBehavior():
    def bark(self):
        pass
    
    class QuietBark():
        def bark(self):
            print("(woof)")
    
    class LoudBark():
        def bark(self):
            print("WOOF")

    class NormalBark():
        def bark(self):
            print("Woof")

class RunBehavior():
    def run(self):
        pass
    
    class SlowRun():
        def run(self):
            print("I am running slowly")
    
    class FastRun():
        def run(self):
            print("I am running fast")

class Dog():
    def __init__(self, breed, size=0, weight=0, color="black", bark_behavior=BarkBehavior.NormalBark(), run_behavior=RunBehavior.SlowRun()):
        self._size = size
        self._weight = weight
        self._color = color
        self._bark_behavior = bark_behavior
        self._run_behavior = run_behavior
        self._breed = breed
        self.summary()

    def summary(self):
        print("Size:", self._size, "Weight:", self._weight, "Color:", self._color, "Breed:", self._breed)
        print("Bark:", self._bark_behavior.__class__.__name__, "Run:", self._run_behavior.__class__.__name__)
        print("")

    def bark(self):
        self._bark_behavior.bark()
    
    def run(self):
        self._run_behavior.run()

class Husky(Dog):
    def __init__(self, breed, size, weight, color, bark_behavior, run_behavior):
        Dog.__init__(self, breed, size, weight, color, bark_behavior, run_behavior)
    
    def pullSled(self):
        print("I am pulling a sled")
        
class Bulldog(Dog):
    def __init__(self, breed, size, weight, color, bark_behavior, run_behavior):
        Dog.__init__(self, breed, size, weight, color, bark_behavior, run_behavior)
    
    def fight(self):
        print("I am fighting")

class Poodle(Dog):
    def __init__(self, breed, size, weight, color, bark_behavior, run_behavior):
        Dog.__init__(self, breed, size, weight, color, bark_behavior, run_behavior)
    
    def style(self):
        print("I am getting styled")


if __name__ == "__main__":
    husky = Husky("Husky", 10, 5, "white", BarkBehavior.NormalBark(), RunBehavior.FastRun())
    bulldog = Bulldog("Bulldog", 5, 20, "black", BarkBehavior.LoudBark(), RunBehavior.SlowRun())
    poodle = Poodle("Poodle", 3, 2, "brown", BarkBehavior.QuietBark(), RunBehavior.FastRun())
    newDog = Dog("Labradoodle", 5, 10, "black", BarkBehavior.NormalBark(), RunBehavior.SlowRun())
    
    print("")

    husky.bark()
    bulldog.bark()
    poodle.bark()
    newDog.bark()

    newDog.run()
