from city import City
from biome import Biome
class World:
    def __init__(self, name="", cities=[], biomes=[], landX=0, landY=0) -> None:
        self.name = name
        self.cities = cities
        self.biomes = biomes
        worldbox = []
        for Y in range(landY):
            worldbox.append([])  # adds an empty box into the worldbox to fill with biomes
            for X in range(landX):
                worldbox[Y].append(Biome())  # inserts an empty biome
        self.landmass = worldbox
    
    def __str__(self) -> str:
        output = ""
        output += self.name
        output += "\n"
        for Y in range(len(self.landmass)):
            for X in range(len(self.landmass[Y])):
                output += str(self.landmass[Y][X])
            output += "\n"
        return output