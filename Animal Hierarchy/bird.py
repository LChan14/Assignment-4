from animal import Animal

class Bird(Animal):

    def reproduce(self) -> str:
        result = '\nBirds typically reproduce by hatching eggs and incubating their eggs.'
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        super().__repr__() + '\nClass: Bird'
        

    

    