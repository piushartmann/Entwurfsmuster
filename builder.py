from abc import ABC, abstractmethod

#design pattern example with a House

class builder():
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    @abstractmethod
    def buildWalls(self) -> None:
        pass
    @abstractmethod
    def buildRoof(self) -> None:
        pass
    @abstractmethod
    def buildWindows(self) -> None:
        pass
    @abstractmethod
    def buildDoors(self) -> None:
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

    def buildWalls(self) -> None:
        self._product.addPart("Wooden Walls")
    
    def buildRoof(self) -> None:
        self._product.addPart("Wooden Roof")

    def buildWindows(self) -> None:
        self._product.addPart("Windows with Wooden Frame")

    def buildDoors(self) -> None:
        self._product.addPart("Wooden Doors")

    def buildGarden(self) -> None:
        self._product.addPart("Garden with Wooden Fence")

    def buildGarage(self) -> None:
        self._product.addPart("Building Wooden Garage")
    
    def buildSwimmingPool(self) -> None:
        self._product.addPart("Building Wooden Swimming Pool")

class StoneHouseBuilder(builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = House()

    @property
    def product(self) -> House:
        product = self._product
        self.reset()
        return product

    def buildWalls(self) -> None:
        self._product.addPart("Stone Walls")
    
    def buildRoof(self) -> None:
        self._product.addPart("Stone Roof")

    def buildWindows(self) -> None:
        self._product.addPart("Windows with Stone Frame")

    def buildDoors(self) -> None:
        self._product.addPart("Stone Doors")

    def buildGarden(self) -> None:
        self._product.addPart("Garden with Stone Fence")

    def buildGarage(self) -> None:
        self._product.addPart("Building Stone Garage")
    
    def buildSwimmingPool(self) -> None:
        self._product.addPart("Building Stone Swimming Pool")

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

    def buildWalls(self) -> None:
        self._product.addPart("Concrete Walls")
    
    def buildRoof(self) -> None:
        self._product.addPart("Concrete Roof")

    def buildWindows(self) -> None:
        self._product.addPart("Windows with Concrete Frame")

    def buildDoors(self) -> None:
        self._product.addPart("Concrete Doors")

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

    def buildStandartHouse(self) -> None:
        self.builder.buildWalls()
        self.builder.buildRoof()
        self.builder.buildWindows()
        self.builder.buildDoors()
    
    def buildLuxuryHouse(self) -> None:
        self.builder.buildWalls()
        self.builder.buildRoof()
        self.builder.buildWindows()
        self.builder.buildDoors()
        self.builder.buildGarden()
        self.builder.buildGarage()
        self.builder.buildSwimmingPool()

if __name__ == "__main__":
    director = Director()
    builder = WoodHouseBuilder()
    director.builder = builder

    print("Standard House:")
    director.buildStandartHouse()
    builder.product.listParts()

    builder = ConcreteHouseBuilder()
    director.builder = builder

    print("\n\nLuxury House:")
    director.buildLuxuryHouse()
    builder.product.listParts() 