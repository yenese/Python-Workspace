


def problem1():
    x = 0
    y = 0
    direction = str(input("Enter the exit route: "))
    for i in direction:
        if i == "w":
            x += 1
        elif i == "e":
            x -= 1
        elif i == "n":
            y += 1
        elif i == "s":
            y -= 1

    last = (abs(x) **2) + (abs(y)**2)
    
    if last == 0:
        return 0
    
    else:
        

        starting_guess = 1
        iteration = 14
        while iteration != 0:
            starting_guess = 1/2*(starting_guess+last/starting_guess)
            iteration -= 1

        return float(starting_guess)

