from pet import Pet
from bird import Bird
from heterotroph import Heterotroph

class Parrot(Bird, Heterotroph, Pet):
    
    def __init__(self, legs = 2, wings = 2, colour = 'yellow'):
        super().__init__(legs)
        self.wings = wings
        self.colour = colour

    def __repr__(self) -> str:
        result = '\nSpecies: Dog'
        result = Bird.__repr__(self) + result
        result +=  '\n' + Pet.__repr__(self)
        return result + '\n' + Heterotroph.__repr__(self)
    
    def reproduce(self) -> None:
        result = 'Parrots often take a few days to lay a full clutch of eggs. This can be as many as three to four eggs.'
        print(super().reproduce() + '\n' + result)

    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb and even use a unique method called "beakiation" to traverse narrow branches.')

    def sleep(self) -> None:
        print('Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day.')

    def eat(self) -> None:
        print('I eat other organisms instead of generating my own food.')
        print('I eat anything!')
        print('I eat both plants and animal matter. My natural diet includes a variety of foods like seeds, nuts, fruits, vegetables flowers, buds, and insects.')
        
if __name__ == '__main__':

    p1 = Parrot()
    
    print(p1.legs)
    print(p1.wings)
    print(p1.colour)

    p1.eat()
    
    p1.move()
    
    p1.sleep()
    
    p1.reproduce()

    legs = int(input('Enter the number of legs for the parrot: '))
    wings = int(input('Enter the number of wings for the parrot: '))
    colour = input('Enter the colour of the parrot: ')
    p2 = Parrot(legs=legs, wings=wings, colour=colour)

    print('\nUser Parrot Details:')
    print(f'Legs: {p2.legs}')
    print(f'Wings: {p2.wings}')
    print(f'Colour: {p2.colour}')


