class Fish:
    def __init__(self,species,x,y,layer):
        self.species: str = species
        self.x: int = x
        self.y: int = y
        self.layer: int = layer
        self.radius: int = 1 #large fish can span multiple cells

        self.age: float = 0.0
        self.detection_radius: int = 0
        self.energy: float = 100.0
        self.fitness: float = 1.0 #max fitness is 1.0, used to determine max potential size, reproductive success, etc...
        self.living: bool = True #dead fish will either be targeted by bottom dwellers or decompose and release nutrients
        self.length: float = 0.0 #measured in inches
        self.weight: float = 0.0 #measured in pounds

    #uses surrounding environment and own stats to "make decisions"
    def step(self,lake):
        if self.living:
             if self.energy <= 0:
                self.living = False