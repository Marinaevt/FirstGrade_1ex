import random
import math
def GenFormula():
    formulas = []
    temp = ''
    latextemp = ''
    znak1 = ['math.sqrt', 'math.exp', 'math.log', 'math.cos', 'math.sin', 'math.tan']
    LaTeXznak1 = ['sqrt', '\exp', '\ln', '\cos', '\sin', '\\tan']
    znak2 = ['+', '-', '*', '/', '**']
    LaTeXznak2 = ['+', '-', '*', '^', '\\frac']
    letters = ['x', 'y', 'z', str(random.randint(2, 10))]
    num = random.randint(2, 4)
    for i in range(num):
        middle = random.randint(0, 4)
        top = random.randint(0, 3)
        bottom = random.randint(0, 3)
        topleft = random.randint(0, 5)
        topright = random.randint(0, 5)
        bottomleft = random.randint(0, 5)
        bottomright = random.randint(0, 5)
        num1 = random.randint(0, 3)
        num2 = random.randint(0, 3)
        num3 = random.randint(0, 3)
        num4 = random.randint(0, 3)
        #'(' + +')'
        temp += '(' + '(' + '(' + znak1[topleft] + '(' + str(letters[num1]) + ')' + ')' + znak2[top] + '(' + znak1[topright] + '(' + str(letters[num2]) + ')' + ')' + ')' + znak2[middle] + '(' + znak1[bottomleft] + '(' + str(letters[num3]) + ')' + ')' + znak2[bottom] + '(' + znak1[bottomright] + '(' + str(letters[num4]) + ')' + ')' + ')'
        if middle != 4:
            latextemp += '{' + '{' + '{' + LaTeXznak1[topleft] + '{' + str(letters[num1]) + '}' + '}' + LaTeXznak2[top] + '{' + LaTeXznak1[topright] + '{' + str(letters[num2]) + '}' + '}' + '}' + LaTeXznak2[middle] + '{' + LaTeXznak1[bottomleft] + '{' + str(letters[num3]) + '}' + '}' + LaTeXznak2[bottom] + '{' + LaTeXznak1[bottomright] + '{' + str(letters[num4]) + '}' + '}' + '}'
        elif middle == 4:
            latextemp += LaTeXznak2[middle] + '{' + '{' + LaTeXznak1[topleft] + '{' + str(letters[num1]) + '}' + '}' + LaTeXznak2[top] + '{' + LaTeXznak1[topright] + '{' + str(letters[num2]) + '}' + '}' + '}' + '{' + LaTeXznak1[bottomleft] + '{' + str(letters[num3]) + '}' + '}' + LaTeXznak2[bottom] + '{' + LaTeXznak1[bottomright] + '{' + str(letters[num4]) + '}' + '}' + '}'
        if i != num-1:
            znakmiddle = random.randint(0, 2)
            temp += str(znak2[znakmiddle])
            latextemp += '  '  + str(LaTeXznak2[znakmiddle])
    formulas.append(temp)
    formulas.append(latextemp)
    return formulas


#print(str(GenFormula()[0]))
x = 2
y = 10
z = 4.5
print((((math.tan(x))+(math.exp(x)))*(math.log(4))*(math.sin(y)))-(((math.sqrt(x))+(math.exp(x)))/(math.log(4))-(math.log(y)))+(((math.tan(y))-(math.cos(z)))*(math.sqrt(4))*(math.sin(4)))-(((math.cos(y))-(math.sin(y)))+(math.sqrt(z))+(math.log(z))))