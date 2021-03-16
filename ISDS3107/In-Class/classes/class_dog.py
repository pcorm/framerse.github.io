class Dog:

    # the __init__ method initializes the object.
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_tricks(self, tricks):
        self.tricks.extend(tricks)

# ***in terminal, change the directory to the current one then type "python"***
# >>> from class_dog import Dog
# >>> d = Dog('Eli')
# >>> type(d)
# <class 'class_dog.Dog'>
# >>> d.name
# 'Eli'
# >>> d.tricks
# []
# >>> d.add_trick("roll over")
# >>> d.add_trick("fetch ball")
# >>> d.tricks
# ['roll over', 'fetch ball']
