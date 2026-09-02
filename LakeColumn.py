import math

#each LakeCell will have multiple WaterLayers (dependent on depth)
class WaterLayer:
    def __init__(self, depth_level):
        self.depth_level: int = depth_level #marks the position of the top of the layer
        self.layer_height: float = 1.0 #measured in meters
        self.num_fish: int = 0
        self.oxygen_conc: float = 0.0
        self.plankton_density: float = 0.0
        self.sunlight_pen: float = 0.0
        self.temperature: float = 0.0 #measured in (tbd)
        self.vegetation_density:float = 0.0

class LakeCell:
    def __init__(self, x, y, max_depth, substrate_type):
        self.x: int = x
        self.y: int = y
        self.max_depth: float = max_depth
        self.substrate_type: str = substrate_type
        self.water_column: list[WaterLayer] = []

        num_layers = math.ceil(self.max_depth)
        for depth in range(num_layers):
         self.water_column.append(WaterLayer(depth))
         if depth == int(self.max_depth):
            self.water_column[depth].range = self.max_depth-depth