import json
import math
import random

class LakeManager:
    def __init__(self, lake, season_info_path):
        self.climate_data = self.get_season_info(season_info_path)
        self.lake = lake
        self.tick: int = 0

        self.current_season: str = "Spring"
        self.is_raining: bool = False
        self.is_cloudy: bool = False
        self.current_temp: int = 0

    def calculate_weather(self):
        if self.tick % 24 == 0:
            curr_weather_data = self.climate_data[self.current_season]
            weather_roll = random.random()
            
            #rain and clouds
            if weather_roll < curr_weather_data["rain_chance"]:
                self.is_raining = True
                self.is_cloudy = True
            elif weather_roll < curr_weather_data["cloud_chance"]:
                self.is_cloudy = True
            else:
                self.is_cloudy = False
                self.is_raining = False
            
            #temps based on rain and clouds    
            low = curr_weather_data["low_temp"]
            high = curr_weather_data["high_temp"]
            mid = (low + high) // 2 
            
            if self.is_raining:
                self.current_temp = random.randint(low, mid)
            elif self.is_cloudy:
                self.current_temp = random.randint(low + 5, high - 5)
            else:
                self.current_temp = random.randint(mid, high)
                  


    def get_season_info(self,filepath):
        with open(filepath,'r') as file:
            lake_data = json.load(file)

            return lake_data


    def step(self):
        self.calculate_weather()
        print(self)

        