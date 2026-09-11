class FishSchool:
    def __init__(self,species,x,y,layer,population):
        self.species: str = species
        self.x: int = x
        self.y: int = y
        self.layer: int = layer
        self.population: int = population
        self.radius: int = 1 #used for consumption calculations, schools can span multiple cells

        self.detection_radius: int = 1
        self.avg_age: float = 0.0
        self.avg_energy: float = 100.0
        self.avg_fitness: float = 0.0
        self.living = True
        self.avg_length: float = 0.0
        self.avg_weight: float = 0.0

    def step(self,lake):
        if self.population <= 0:
            self.living = False #since its a school, destroy once no individuals remain
