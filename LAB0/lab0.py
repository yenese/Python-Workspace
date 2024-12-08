my_name = "Yunus Emre Buyukyilmaz"
my_id = "220102002054"
my_email = "y.buyukyilmaz2022@gtu.edu.tr"




def problem1():
    name = "Hi all, This is Yunus Emre Buyukyilmaz!"
    return name


def problem2():
    a = input("Enter some input : ")
    b = "Input was " + a
    return b

def problem3():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    result = number1 + number2
    return result

def problem4():
    number1 = float(input("Enter first number : "))
    number2 = float(input("Enter second number : "))
    res = number1 - number2
    return  res

def problem5():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    if number2 == 0:
        return "the denominator cannot be 0"
    if number1 < number2:
        return "The first number cannot be completely divided by the second number"
    res = number1 % number2
    return res

def problem6():
    radius = float(input("Enter radius : "))
    height = float(input("Enter height : "))
    pi = 3.141592
    volume = pi * (radius**2) * height
    return volume

def problem7():
    side = float(input("Enter the lenght : "))
    per = 4 * side
    per = str(per)
    res = "The perimeter of the square is " + per + "."
    return  res







