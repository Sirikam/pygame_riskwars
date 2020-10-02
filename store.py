import numpy as np

class Store:

    def __init__(self, name, beermod, winemod, spiritmod, dayclosed):
        self.name = name
        self.beermod = beermod
        self.winemod = winemod
        self.spritmod = spiritmod
        self.dayclosed = dayclosed

    def return_mod(self,int):
        if int ==1:
            return self.beermod
        elif int == 2:
            return self.winemod
        elif int ==3:
            return self.spritmod

    def return_open(self,day):
        if day%self.dayclosed==0:
            return False
        else:
            return True