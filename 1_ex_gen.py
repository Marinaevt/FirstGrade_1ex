import math
import random

def GenFormula():
    formulas = []
    temp = ''
    latextemp = ''
    step = random.randint(2, 12)
    znak1 = ['math.sqrt', 'math.exp', 'math.log', 'math.cos', 'math.sin', 'math.tan', str(step) + '*']
    LaTeXznak1 = ['sqrt', '\exp', '\ln', '\cos', '\sin', '\\tan', str(step) + '*']
    znak2 = ['+', '-', '*', '**', '/']
    LaTeXznak2 = ['+', '-', '*', '^', '\\frac']
    letters = ['x', 'y', 'z', str(random.randint(2, 10))]
    num = random.randint(2, 3)
    for i in range(num):
        middle = random.randint(0, 4)
        if middle == 3:
            bottom = random.randint(0, 2)
            bottomleft = 6
            bottomright = 6
        else:
            bottom = random.randint(0, 3)
            bottomleft = random.randint(0, 6)
            bottomright = random.randint(0, 6)
        top = random.randint(0, 3)
        if top == 3:
            topright = 6
        else:
            topright = random.randint(0, 6)
        topleft = random.randint(0, 5)
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
            latextemp += str(LaTeXznak2[znakmiddle])
    formulas.append(temp)
    formulas.append(latextemp)
    return formulas


#fileformulaname = str(i) + "varFormula1ex.txt"
f2 = open('formulas.txt', 'w')
numVar = 2
for i in range(numVar):
    filevarname = str(i) + "var1ex.txt"
    f1 = open(filevarname, 'w')
    fgen = open('1_ex_test_gen.py', 'r')
    fsol = open('solvefile.txt', 'r')
    fcheck = open('checkfile.txt', 'r')
    for line in fgen:
        f1.write(line)
    f1.write('\n')
    for line in fsol:
        f1.write(line)
    formula = GenFormula()
    f1.write('    ' + 'return str(' + str(formula[0]) + ')' + '\n')
    f2.write(str(formula[1]) + '\n')
    f1.write('\n')
    for line in fcheck:
        f1.write(line)
    f1.close()
    fgen.close()
    fsol.close()
    fcheck.close()
f2.close()



