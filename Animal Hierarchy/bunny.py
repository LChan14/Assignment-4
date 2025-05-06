from pet import Pet
from mammal import Mammal
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    '''Class for bunnies'''
    
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        # Mammal.__init__(self, legs) -> More Spreific, says which class to use
        self.ears = ears

    def __repr__(self) -> str:
        result = '\nSpecies: Bunny'
        result = Mammal.__repr__(self) + result # Kingdom, Class, Species info
        result +=  '\n' + Pet.__repr__(self)# From Pet
        return result + '\n' + Herbivore.__repr__(self) # From Herbivore
    
    def reproduce(self) -> None:
        result = 'Bunnies can produce multiple litters per\
            year, potentially having 3-8 kits per litter.'
        
        print(super().reproduce() + '\n' + result)
        
    def move(self) -> None:
        print('I move by hopping and i can see behind me')

    def sleep(self) -> None:
        print('Bunnies are nocturnal animals, typically sleep around 12 to 14 hours a day in short intermittent periods.')
    
    def eat(self) -> None:
        print('I mostly eat fresh hay and  grass with some leafy greens and a few pellets and only be given fruit and root vegetables like carrots as an occasional treat.')

if __name__ == '__main__':
    b1 = Bunny()
    print(b1.legs)
    print(b1.ears)
    #print(b1)

    print()
    print(b1.reproduce())

    print()
    print(b1.move())

    print()
    print(b1.eat())

    print()
    print(b1.pet())