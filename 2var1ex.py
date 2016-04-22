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
    return str((((math.sqrt(x))+(math.tan(z)))+(math.cos(z))+(math.exp(y)))*(((math.sin(9))+(math.log(x)))-(math.tan(9))*(math.log(x)))-(((math.sin(y))-(11*(9)))*(math.exp(y))**(math.sin(x))))

def check(reply, clue):
    if abs(float(clue) - float(reply)) < 1:
        return 1
    return 0
