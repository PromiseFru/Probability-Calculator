import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for x in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls_to_draw):
        ball_collection = copy.deepcopy(self.contents)
        balls_drawn = []
        if number_of_balls_to_draw > len(ball_collection):
            return ball_collection
        for x in range(number_of_balls_to_draw):
            random_number = random.randint(0, len(ball_collection)-1)
            balls_drawn.append(ball_collection[random_number])
            ball_collection.pop(random_number)
        return balls_drawn

hat = Hat(red=4, black = 2)
print(hat.draw(4))

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
