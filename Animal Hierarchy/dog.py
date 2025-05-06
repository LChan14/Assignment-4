from pet import Pet
from mammal import Mammal
from omnivore import Omnivore

class Dog(Mammal,Omnivore,Pet):

    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        self.ears = ears

    def __repr__(self) -> str:
        result = '\nSpecies: Dog'
        result = Mammal.__repr__(self) + result
        result +=  '\n' + Pet.__repr__(self)
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> None:
        result = 'Dogs can produce multiple litters per\
            year, typically having 6-8 puppies per litter.'
        print(super().reproduce() + '\n' + result)

    def move(self) -> None:
        print('I move by running and i have binocular vision')

    def sleep(self) -> None:
        print('Dogs are diurnal animals, typically sleep around 12 to 14 hours a day in short intermittent periods.')

    def eat(self) -> None:
        print('I mostly eat meat, but i can also eat some fruits, vegetables, and grains.')

if __name__ == '__main__':
    # Test Case 1: Initialization
    d1 = Dog(legs=4, ears=2)
    print(d1.legs)  # Expected: 4
    print(d1.ears)  # Expected: 2

    # Test Case 2: __repr__ Method
    #print(d1)  # Expected: Species: Dog (and other parent class details if included)

    # Test Case 3: reproduce Method
    d1.reproduce()  # Expected: Dogs can produce multiple litters per year, typically having 6-8 puppies per litter.

    # Test Case 4: move Method
    d1.move()  # Expected: I move by running and I have binocular vision.

    # Test Case 5: sleep Method
    d1.sleep()  # Expected: Dogs are diurnal animals, typically sleep around 12 to 14 hours a day in short intermittent periods.

    # Test Case 6: eat Method
    d1.eat()  # Expected: I mostly eat meat, but I can also eat some fruits, vegetables, and grains.