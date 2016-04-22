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
    return str((((math.exp(x))+(math.exp(z)))/(math.log(z))**(math.tan(2)))-(((math.sin(x))*(math.tan(y)))+(9*(y))**(math.sin(x)))+(((math.exp(z))*(math.exp(z)))-(math.exp(z))+(math.log(x))))

def check(reply, clue):
    if abs(float(clue) - float(reply)) < 1:
        return 1
    return 0
