from abc import ABC, abstractmethod

#design pattern example with a House

class builder():
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    @abstractmethod
    def buildWalls(self, number) -> None:
        pass
    @abstractmethod
    def buildRoof(self) -> None:
        pass
    @abstractmethod
    def buildWindows(self, number) -> None:
        pass
    @abstractmethod
    def buildDoors(self, number) -> None:
        pass
    @abstractmethod
    def buildGarden(self) -> None:
        pass
    def buildGarage(self) -> None:
        pass
    def buildSwimmingPool(self) -> None:
        pass

class House():
    def __init__(self):
        self.parts = []

    def addPart(self, part):
        self.parts.append(part)
    
    def listParts(self):
        print(f"House parts: {', '.join(self.parts)}", end="")

class WoodHouseBuilder(builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = House()

    @property
    def product(self) -> House:
        product = self._product
        self.reset()
        return product

    def buildWalls(self, number) -> None:
        self._product.addPart(f"Wooden {number} Walls")
    
    def buildRoof(self) -> None:
        self._product.addPart("Wooden Roof")

    def buildWindows(self, number) -> None:
        self._product.addPart(f"{number} Windows with Wooden Frame")

    def buildDoors(self, number) -> None:
        self._product.addPart(f"{number} Wooden Doors")

    def buildGarden(self) -> None:
        self._product.addPart("Garden with Wooden Fence")

    def buildGarage(self) -> None:
        self._product.addPart("Building Wooden Garage")
    
    def buildSwimmingPool(self) -> None:
        self._product.addPart("Building Wooden Swimming Pool")

class ConcreteHouseBuilder(builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = House()

    @property
    def product(self) -> House:
        product = self._product
        self.reset()
        return product

    def buildWalls(self, number=4) -> None:
        self._product.addPart(f"Concrete {number} Walls")
    
    def buildRoof(self) -> None:
        self._product.addPart("Roof")

    def buildWindows(self, number=4) -> None:
        self._product.addPart(f"{number} Windows embedded in Concrete")

    def buildDoors(self, number=4) -> None:
        self._product.addPart(f"{number} Concrete Doors")

    def buildGarden(self) -> None:
        self._product.addPart("Garden with Concrete Fence")

    def buildGarage(self) -> None:
        self._product.addPart("Building Concrete Garage")
    
    def buildSwimmingPool(self) -> None:
        self._product.addPart("Building Concrete Swimming Pool")

class Director():
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> builder:
        return self._builder

    @builder.setter
    def builder(self, builder: builder) -> None:
        self._builder = builder

    def buildStandardHouse(self) -> None:
        self.builder.buildWalls(4)
        self.builder.buildRoof()
        self.builder.buildWindows(6)
        self.builder.buildDoors(2)
    
    def buildLuxuryHouse(self) -> None:
        self.builder.buildWalls(8)
        self.builder.buildRoof()
        self.builder.buildWindows(20)
        self.builder.buildDoors(6)
        self.builder.buildGarden()
        self.builder.buildGarage()
        self.builder.buildSwimmingPool()

if __name__ == "__main__":
    director = Director()
    builder = WoodHouseBuilder()
    director.builder = builder

    print("Standard House:")
    director.buildStandardHouse()
    builder.product.listParts()

    builder = ConcreteHouseBuilder()
    director.builder = builder

    print("\n\nLuxury House:")
    director.buildLuxuryHouse()
    builder.product.listParts()