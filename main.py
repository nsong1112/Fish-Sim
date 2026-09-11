from lake import Lake
from lake_manager import LakeManager
from fish import Fish
from fish_school import FishSchool
import pygame

my_lake = Lake('templates/test_lake.txt')
my_lake_manager = LakeManager(my_lake,"va_seasonal_info.json")

clock = pygame.time.Clock()

while True:
    my_lake_manager.step()
    clock.tick(24) #24 hours per second