from store import Store

class Maptile:

    def __init__(self, tileid, students, Store, neigbours, terrain):
        self.tileid = tileid
        self.students = students
        self.store = Store
        self.nb = neigbours
        self.terrain = terrain

    def return_tileid(self):
        return self.tileid

    def return_students(self):
        return self.students

    def return_store(self):
        return self.store

    def return_nb(self):
        return self.nb

    def return_terrain(self):
        return
