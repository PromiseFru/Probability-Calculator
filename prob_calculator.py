import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for x in range(value):
                self.contents.append(key)

hat = Hat(red=4, black = 2)
print(hat.contents)

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
