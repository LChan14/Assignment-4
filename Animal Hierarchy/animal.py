from abc import ABCMeta, abstractmethod

class Animal(object, metaclass=ABCMeta):
    '''Abstract class for all animals'''
    
    def __init__(self, legs = 0, fins = 0, wings = 0) -> None:
        self.legs = legs
        self.fins = fins
        self.wings = wings

    @abstractmethod
    def move(self):
        '''Abstract method for moving'''
        pass

    @abstractmethod
    def sleep(self):
        '''Abstract method for sleeping'''
        pass

    @abstractmethod
    def eat(self):
        '''Abstract method for eating'''
        pass

    def reproduce(self) -> str:
        return 'Members of this kingdom reproduce\
            by finding a mate of the same species.'
    
    def __repr__(self) -> str:
        return 'Kingdom: Animalia'
    