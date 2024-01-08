from city import City
from biome import Biome
from random import randint
class World:
    def __init__(self, name="", landX=0, landY=0, biomes=[], cities=[]) -> None:
        self.name = name
        self.cities = cities
        self.biomes = biomes
        worldbox = []
        for Y in range(landY):
            worldbox.append([])  # adds an empty box into the worldbox to fill with biomes
            for X in range(landX):
                worldbox[Y].append(Biome())  # inserts an empty biome
        self.landmass = worldbox
        self.populate_biomes()
        
    
    # displays the world as a grid of symbols that represent the biomes
    def __str__(self) -> str:
        output = ""
        output += self.name
        output += "\n"
        for Y in range(len(self.landmass)):
            for X in range(len(self.landmass[Y])):
                output += str(self.landmass[Y][X])
            output += "\n"
        return output
    
    # initialy converts all empty biomes into biomes with actual effects, assuming there are biomes in the World
    def populate_biomes(self) -> str:
        if len(self.biomes) == 0:
            return "Failed to populate, no biomes present"
        for Y in range(len(self.landmass)):
            for X in range(len(self.landmass[Y])):
                selection = randint(0, len(self.biomes) -1)
                self.landmass[Y][X] = Biome(self.biomes[selection])
        return ""