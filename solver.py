import numpy as np

numberOfEquations = 0
Adata = []
Bdata = []


def intvalidation(integer):
    try:
        intinteger = int(integer)
        if intinteger <= 2:
            print("Must have more than 2 equations, this program handles 3 variables.")
            menu()
        else:
            equationsolver(intinteger)

    except ValueError:
        print("Must input an integer.")
        menu()
        return None


def coefficientvalidation(integer):
    try:
        return int(integer)

    except ValueError:
        print("Must input an integer.")
        return None


def menu():
    print("3-variable Simultaneous equation solver using gaussian elimination, to 2 dp.")
    numeqinput = input("input number of equations.")
    intvalidation(numeqinput)


def equationsolver(numofequations):
    for index in range(numofequations):
        print("----------Equation", index + 1, "----------")
        print("ax + by + cz = d   (Coefficients can be 0 or negative)")
        x = None
        while x is None:
            x = coefficientvalidation(input("Coefficient for x: "))

        y = None
        while y is None:
            y = coefficientvalidation(input("Coefficient for y: "))

        z = None
        while z is None:
            z = coefficientvalidation(input("Coefficient for z: "))

        d = None
        while d is None:
            d = coefficientvalidation(input("Value of d: "))

        print("Equation", index + 1, ": ", x, "x +", y, "y +", z, "z =", d)
        xyzarray = [x, y, z]
        constantarray = [d]
        Adata.append(xyzarray)
        Bdata.append(constantarray)
    Aarray = np.array(Adata)
    Barray = np.array(Bdata).flatten()
    print(Aarray, Adata)
    print(Barray, Bdata)
    values = np.linalg.solve(Aarray, Barray)
    print("x = {:.2f}, y = {:.2f}, z = {:.2f}".format(values[0], values[1], values[2]))
    answer = None
    while answer == None:
        answer = input("Would you like to display the entire float?")
        if answer == 'yes':
            print("x = {}, y = {}, z = {}".format(values[0], values[1], values[2]))
        elif answer == 'no':
            pass
        else:
            answer = None
            print("Please provide a valid answer.")


menu()
