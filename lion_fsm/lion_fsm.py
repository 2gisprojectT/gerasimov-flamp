__author__ = 'vi.gerasimov'


class Lion():
    __isHungry = True

    def __init__(self, isHungry):
        if type(isHungry) is not bool:
            raise ValueError('isHungry must be a bool')
        self.__isHungry = isHungry

    def get(self, anything):
        return {
            'antelope': lambda: self.__eat() if self.__isHungry else self.__sleep(),
            'hunter': lambda: self.__run(),
            'tree': lambda: self.__sleep() if self.__isHungry else self.__look()
        }.get(str(anything).lower(), lambda: 'Brr... Give me what I know!')()

    def __sleep(self):
        self.__isHungry = not self.__isHungry
        return 'Lion is sleeping. Lion is hungry.'

    def __run(self):
        self.__isHungry = True
        return 'Lion is running. Lion is hungry.'

    def __eat(self):
        self.__isHungry = False
        return 'Lion is eating. Lion is full.'

    def __look(self):
        self.__isHungry = True
        return 'Lion is looking. Lion is hungry.'