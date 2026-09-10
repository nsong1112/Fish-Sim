import json
import math
import random

class LakeManager:
    def __init__(self, lake, season_info_path):
        self.day_info = {} #info to be used each simulation day to prevent unnecessary work

        self.climate_data = self.get_season_info(season_info_path)
        self.lake = lake
        self.tick: int = 0

        self.current_season: str = "Winter"
        self.is_raining: bool = False
        self.is_cloudy: bool = False
        self.current_temp: int = 0

    def calculate_weather(self):
        curr_weather_data = self.climate_data[self.current_season]
        weather_roll = random.random()
        
        #rain and clouds, change weather to be hourly later on
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

    #store info needed for the day
    def get_day_info(self,tick_num):
        days_passed = tick_num // 24
        day_of_year = days_passed % 365

        if day_of_year < 79:
            self.current_season = "Winter"
        elif day_of_year < 172:
            self.current_season = "Spring"
        elif day_of_year < 265:
            self.current_season = "Summer"
        elif day_of_year < 355:
            self.current_season = "Fall"
        else:
            self.current_season = "Winter"

        season_info = self.climate_data[self.current_season]

        first_light = season_info["first_light"]
        last_light = season_info["last_light"]
        mu = (first_light + last_light)/2
        sigma = (last_light - first_light)/6

        #uses standard gaussian equation
        def get_sun_intenity(hour):
            if hour < first_light or hour > last_light:
                return 0
            return math.exp(-((hour - mu)**2) / (2 * sigma**2))

        self.day_info["get_sun_intensity"] = get_sun_intenity
    
    def get_season_info(self,filepath):
        with open(filepath,'r') as file:
            lake_data = json.load(file)

            return lake_data

    def step(self):
        hour_of_day = self.tick % 24
        if hour_of_day == 0:
            self.get_day_info(self.tick)
            self.calculate_weather()
       # self.get_sun_intensity(hour_of_day)
        self.sun_intensity = self.day_info["get_sun_intensity"](hour_of_day)
        self.tick += 1


        