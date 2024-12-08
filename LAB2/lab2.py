


def problem1():
    fah = float(input("Enter Fahrenheit degree: "))
    celc = (fah - 32) * 5/9
    return float(celc)


def problem2():
    celc = float(input("Enter Celsius degree: "))
    fah = (celc *9/5) + 32
    return float(fah)


def problem3():
    n = int(input("Enter a number: "))
    hexa = 2*(n**2) - n
    return int(hexa)


def problem4():
    number = int(input("Enter a number: "))

    if number == 0:
        return 2
    
    elif number == 1:
        return 1

    elif number > 1:
        first = 1 
        second = 2 
        for i in range(2 , number+1):
            res = first + second
            first , second = res , first
        return first

def problem5():
    string = str(input("Enter a string: "))
    a = string[::-1]
    return a


def problem6():
    unwanted = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'         
    string = str(input("Enter a string: "))
    new = ""
    a = 0
    while a <= len(unwanted):
        for i in string:
            if i not in unwanted:
                new += i
        a += 1
        return new


def problem7():
    number = int(input("Enter input: "))  
    repre = ""

    if number == 0:
        return 0
    
    check = False
    if number < 0:
        check = True
        number = abs(number)
  
    
    while number  != 0:
        remain = (number) % 4
        repre += str(remain)
         
        number //= 4

    if check:
        return "-" + repre[::-1]
    else:
        return repre[::-1]


def problem8():
    user = str(input("Enter input: "))
    if user[0] == "}" or user[0] == ")" or user[0] == "]" :
                return False
    check = []
    for i in user:
        if i == "{" or i == "(" or i == "[":
            check.append(i)
        elif  (i ==  "}" and check[len(check) - 1] == "{" ) or ( i == ")" and check[len(check) - 1] == "(" )   or    ( i == "]" and check[len(check) - 1] == "[" ): 
            check.pop()


    if len(check) == 0:
        return True
    
    else:
        return False        



def problem9():
    user = str(input("Enter a string: "))
    reverse = user[::-1]
    i = 0
    if " "  in user:
        while reverse[i] != " ":
            i += 1
        
        return i    
    
    else:
        return len(user)






    





    


    



    
         
        
 


