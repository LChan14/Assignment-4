from animal import Animal

class Fish(Animal):

    def reproduce(self) -> str:
        result = '\nFish reproduction vareis largely,\
            some give birth to live young while others lay eggs.'
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        super().__repr__() + '\nClass: Fish'