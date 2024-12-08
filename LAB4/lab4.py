


def problem1(lst , idx):
    if idx < 0 or idx > len(lst):
        return None

    else:
        return lst[idx] 
    



def problem2(lst, idx):
    if idx < 0 or idx > len(lst):
        return lst
    
    else: 
        del lst[idx]    
        return lst
    
    

def problem3(lst, bl):
    ascending = sorted(lst)
    descending = ascending[::-1]
    
    if bl == True:
        return ascending
    
    elif bl == False:
        return descending
        
    

def problem4(l, w):                  
    number1 = 0
    number2 = 0
    
    for i in range(len(l)):
        mult = l[i] * w[i] 
        number1 += mult
        number2 += w[i]      
        
    result = float(number1 / number2)
    return result
    
    
    
    
def problem5(l1, l2):
    common_list = []
    for i in l1:
        if i in l2:
            common_list.append(i)
        
    for i in common_list:
        if common_list.count(i) > 1:
            common_list.remove(i)
            
        
    return len(common_list)
       
      
      

def problem6(dtm):
    for i in dtm:
        if len(i) != len(dtm[0]):
            return None
    
    
    if len(dtm) == 1:
        return float(dtm[0][0])
    

    if len(dtm) == 2:
        return float(dtm[0][0] * dtm[1][1] - dtm[0][1] * dtm[1][0])
    

    if len(dtm) == 3:
        dtm.append(dtm[0])
        dtm.append(dtm[1])

        a = (dtm[0][0] * dtm[1][1] * dtm[2][2] ) + (dtm[1][0] * dtm[2][1] * dtm[3][2] ) + (dtm[2][0] * dtm[3][1] * dtm[4][2])
        b = ( dtm[0][2] * dtm[1][1] * dtm[2][0] ) + ( dtm[1][2] * dtm[2][1] * dtm[3][0]) + (dtm[2][2] * dtm[3][1] * dtm[4][0])
        return float(a - b)
    


def problem7(accounts, source, lira, kurus):
    
    if source < 0 or source >= len(accounts): 
        return accounts    
    
    
    
    money = lira + kurus/100
    money_from = float(accounts[source])
     
    
    if money <= money_from:
        
        money_from -= money
        a = round(money_from, 2) 
        a_str = str(a)
            
        if len(a_str.split(".")[1]) == 1 and a_str.split(".")[1] != "0" :
            a_str += "0"
                    
        accounts[source] = a_str
        return accounts
      
      
    else:
        return accounts    
    
      
def problem8(students):
    repeat = 0
    list_students = []

    for i in range(1,students+1):
        list_students.append(i)

    while len(list_students) > 1:
        for i in range(len(list_students)):
            repeat += 1
            if repeat % 9 == 0:
                list_students.remove(list_students[i])
        
        
    return list_students[0]
        
 
        
  
  
def problem9(lst):
    new_lst = []
    for i in lst:
        if lst.count(i) > 1:
            new_lst.append(i) 
            
    if len(new_lst) == 0:
        return None
            
    result = str(new_lst[0])       
    return result         
        
      
      


