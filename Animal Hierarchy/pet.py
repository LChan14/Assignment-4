from abc import ABCMeta

class Pet (object, metaclass=ABCMeta):
    '''Abstract class for all pets'''

    def __init__(self, legs = 0) -> None:
        self.legs = legs

    def pet(self) -> str:
        '''Abstract method for petting'''
        return 'You can pet this animal.'
    
    def __repr__(self) -> str:
        return 'This animal is a pet.'