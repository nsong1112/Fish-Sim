from lake import Lake
from lake_manager import LakeManager
from fish import Fish
from fish_school import FishSchool

# 1. Initialize the Lake environment (This instantly builds all cells and layers!)
my_lake = Lake('templates/test_lake.txt')

# 2. Let's verify the environment built correctly
print("--- LAKE GENERATION REPORT ---")
print(f"Lake Dimensions: {my_lake.width_x} cells wide by {my_lake.height_y} cells high.")

# 3. Test a shallow edge cell
edge_cell = my_lake.grid[0][0]
print(f"The cell at (0,0) is {edge_cell.max_depth}m deep and has {len(edge_cell.water_column)} layer(s).")

# 4. Test the deep center cell
center_cell = my_lake.grid[4][4]
print(f"The cell at (4,4) is {center_cell.max_depth}m deep and has {len(center_cell.water_column)} layer(s).")