from lake_column import LakeCell

class Lake:
    def __init__(self, template_file_path):
        self.grid = []
        
        self.width_x = 0
        self.height_y = 0
        
        # Automatically build the lake when the object is created
        self.build_lake_from_text(template_file_path)
        
    def build_lake_from_text(self, file_path):
        try:
            with open(file_path, 'r') as file:
                # Enumerate gives us 'y' (the row number) automatically starting at 0
                for y, line in enumerate(file):
                    row = []
                    
                    # .strip() removes newlines, .split(',') breaks it into a list
                    depth_strings = line.strip().split(',')
                    
                    # Enumerate gives us 'x' (the column number)
                    for x, depth_str in enumerate(depth_strings):
                        cell_depth = float(depth_str.strip())
                        
                        # Create the 3D cell based on the depth number
                        new_cell = LakeCell(x, y, max_depth=cell_depth, substrate_type="mud")
                        row.append(new_cell)
                    
                    self.grid.append(row)
                    
            # Set the dimensions based on what was actually read
            self.height_y = len(self.grid)
            if self.height_y > 0:
                self.width_x = len(self.grid[0])
                
        except FileNotFoundError:
            print(f"ERROR: Could not find the file '{file_path}'. Check your spelling and folder location!")

    def get_cell(self,x,y):
        return self.grid[y][x]