from abc import ABC
from hexmap.map import MapUnit


class Maptile(MapUnit, ABC):

    def __init__(self, movement, students, spirit, wine, beer, terrain, grid):
        super().__init__(grid)
        self.movement = movement
        self.students = students
        self.terrain = terrain
        self.spirit = spirit
        self.wine = wine
        self.beer = beer

    def return_students(self):
        return self.students

    def return_store(self):
        return self.store

    def return_terrain(self):
        return self.terrain

    def return_spirit(self):
        return self.spirit

    def return_wine(self):
        return self.wine

    def return_beer(self):
        return self.beer
