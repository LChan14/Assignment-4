from heterotroph import Heterotroph

class Omnivore(Heterotroph):
    
    def eat(self) -> None:
        super().eat()
        print('I eat anything!')

    def __repr__(self) -> str:
        result = '\nThis organism is an omnivore. It can feed on\
            both plants and other animals.'
        
        return super().__repr__() + result
    
