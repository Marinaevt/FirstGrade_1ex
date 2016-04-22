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

def solve(dataset):
    x, y, z = dataset.split()
    x, y, z = float(x), float(y), float(z)
    return str((((math.log(8))**(6*(x)))-(math.sqrt(8))*(math.cos(y)))*(((math.tan(z))*(math.sin(8)))+(math.sin(y))**(math.sin(y)))+(((math.tan(y))-(math.sin(8)))-(math.sin(8))+(math.cos(8))))

def check(reply, clue):
    if abs(float(clue) - float(reply)) < 1:
        return 1
    return 0
