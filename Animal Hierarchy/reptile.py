from animal import Animal

class Reptile(Animal):

    def reproduce(self) -> str:
        result = '\nReptiles reproduce by laying eggs, typically\
            on land rather than water.'
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        super().__repr__() + '\nClass: Reptile'