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
        # ball_collection = copy.copy(self.contents)
        balls_drawn = []
        if number_of_balls_to_draw > len(self.contents):
            return self.contents
        for x in range(number_of_balls_to_draw):
            random_number = random.randint(0, len(self.contents)-1)
            balls_drawn.append(self.contents[random_number])
            self.contents.pop(random_number)
        return balls_drawn

# def expected_balls_names(expected_balls):
#     expected_names = [] 
#     for key, value in expected_balls.items():
#         for x in range(value):
#             expected_names.append(key)
#     return expected_names

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#     match_count = 0

#     for x in range(num_experiments):
#         matches = False
#         draws = hat.draw(num_balls_drawn)
#         for key, value in expected_balls.items():
#             if draws.count(key) == value:
#                 matches = True
#         if matches == True:
#             match_count + 1

#     result = match_count/num_experiments

#     return result