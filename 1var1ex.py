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
    return str((((math.exp(x))**(9*(y)))+(math.log(x))*(math.sqrt(z)))+(((math.exp(x))*(math.sin(y)))-(math.exp(3))+(math.sqrt(y))))

def check(reply, clue):
    if abs(float(clue) - float(reply)) < 1:
        return 1
    return 0
