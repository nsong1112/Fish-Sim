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
              weather_roll = random.random()


    def get_season_info(self,filepath):
        with open(filepath,'r') as file:
            lake_data = json.load(file)

            return lake_data


    def step(self):
        self.calculate_weather()

        