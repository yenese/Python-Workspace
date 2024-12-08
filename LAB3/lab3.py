
def problem1(card):
    for i in card:
        if i == "K":
            return True
    
    return False


def problem2(a, b, c, d):
    list = [a, b, c, d]                         
    ite = 0
    while ite <= 3:
        for i in range(len(list)-1 ):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1] , list[i]    
            
        ite += 1
    
    return float(list[0])   
            
        
        
def problem3(number, b):
    remainder = number % 1 
    divide = number // 1
    rnd1 = divide
    rnd2 =  divide + 1
    
    if remainder == 0:
        return int(number)    
    elif abs(b - rnd1) < abs(b - rnd2): 
        return int(rnd1)
    elif abs(b - rnd2) < abs(b - rnd1):
        return int(rnd2)
    elif abs(b - rnd2) == abs(b - rnd1):
        return int(rnd2)        
                   
        
        
    
    
def problem4(radius, height, pi = 3.1415):
    volume = (radius**2)*height*pi
    return volume



def problem5(radius, height, pi = 3.1415):              
    
    if type(radius) == int or  type(radius) == float:
        if type(height) == int or type(height) == float:
            if type(pi) == int or type(pi) == float:
                volume = (radius**2)*height*pi
                return volume
            
    return -1        
                
                
    
    
def problem6(a):                       
    list1 = []
    list2 = []
    for i in a:  
        if i not in list1:
            list1.append(i)
        else:
            list2.append(i)   
        
    while len(list1) != 1:
        for i in list1:
            if i in list2:
                list1.remove(i)
            
    return list1[0]
                      
            
            
def problem7(a):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(a)- 1):
            if alphabet.index(a[i]) > alphabet.index(a[i+1]):
                return False
            
    return True         
            
            
            
def problem8(a):
    list1 = []
    list2 = []
    for i in a:
        if i not in list1:
            list1.append(i)
        else:
            list2.append(i)    
            
    if len(list2) == 0:
        return True
    
    else:
        return False
                
        

      
        


      
     
    