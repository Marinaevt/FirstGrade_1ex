import random
import math

def generate():
    num_tests = 10
    random.seed()
    tests = []
    for k in range(num_tests):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        z = random.uniform(1, 100)
        tests.append("{} {} {}".format(x, y, z))
    return tests
