def check(reply, clue):
    if abs(float(clue) - float(reply)) < 1:
        return 1
    return 0
