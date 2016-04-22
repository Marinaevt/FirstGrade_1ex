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
    return str((((math.tan(x))**(8*(3)))*(math.exp(3))*(math.tan(y)))+(((math.sin(3))*(math.cos(z)))*(math.exp(3))*(math.log(3)))+(((math.cos(z))**(8*(z)))-(math.exp(y))+(math.sqrt(3))))

def check(reply, clue):
    if abs(float(clue) - float(reply)) < 1:
        return 1
    return 0
