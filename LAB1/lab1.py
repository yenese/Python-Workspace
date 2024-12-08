my_name = "Yunus Emre Buyukyilmaz"
my_id = "220102002054"
my_email = "y.buyukyilmaz2022@gtu.edu.tr"


def problem1():
    first = my_name[0]
    return first

def problem2():    
    index = int(input("Enter a number: "))      
    if index > len(my_name):
        new_ind = index % len(my_name)
        return my_name[new_ind]

    elif index < 0 :
        new1_ind = index + len(my_name)
        return my_name[new1_ind]
    
    else:
        return my_name[index]
    

def problem3():
    first = int(input("Enter first number: "))
    sec = int(input("Enter second number: "))
    


    if first < 0 or first > len(my_name):

        while first >= len(my_name):
            first += len(my_name)
            break
    new_f = first % len(my_name)        
   
    if sec < 0 or sec > len(my_name):

        while sec >= len(my_name):
            sec += len(my_name)
            new_s = first 
            break

    new_s = sec % len(my_name) 


    index1 = min(new_s,new_f)
    index2 = max(new_s,new_f)

    return my_name[index1:index2 + 1]



def problem4():     
    vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    string = str(input("Enter input: "))
    i = 0

    for a in string:                                                             
        for j in vowels:
            if a  == j:
                i += 1
    if i == 0:
        return 0
    else:          
        return i       
    

def problem5():
    sum = 0

    for i in my_id:
        i = int(i)
        sum = sum + i
    return sum


def problem6():   
    number = int(input("Enter input: "))

    a = 1
    for i in range(1,number+1):
        a *= i
    return a


def problem7():
    number = int(input("Enter a number: "))

    if number % 3 == 0 and number % 7 == 0:
        return True
    else:
        return False


def problem8():
    number = int(input("Enter a number: "))

    if number % 3 == 0 and number % 7 != 0:
        return 1
    elif number % 7 == 0 and number % 3 != 0:
        return 2
    elif number % 3 == 0 and number % 7 == 0:
        return 3
    

def problem9():
    number = int(input("Enter a number: "))
    if number == 1:
        return False
    
    elif number <= 0:
        return False
    
    elif number == 2:
        return True
    
    elif number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        
        else:
            return True


def problem10():
    number = float(input("Enter a number: "))
    starting_guess = 1
    iteration = 14
    while iteration != 0:
        starting_guess = 1/2*(starting_guess+number/starting_guess) 
        iteration -= 1

    return (starting_guess)







                                

    








