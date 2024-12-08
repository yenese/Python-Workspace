




def problem1(lst , integer ):
    number_list = []
    result = []
    
    for i in lst:
        if i not in number_list:
            number_list.append(i)
            
    for i in number_list:
        if lst.count(i) == integer:
            result.append(i)
            
    return result 


def problem2(x):
    listOfdict = list(x.values())
    
    
    
    if len(listOfdict) % 2 == 0:
        a = (len(listOfdict)/2)-1
        b = (len(listOfdict)/2)
        result1 = listOfdict[int(a)] + listOfdict[int(b)]  
        return result1 / 2     
        

            
    if len(listOfdict) % 2 != 0:
        a = ((len(listOfdict)+1)/2) - 1
        result2 = listOfdict[int(a)] 
        return result2 
        



    
def ffunc(n):  
    strg = ""
    for i in range(n+1):
        strg += str(i)
        
    amount = strg.count("1")
    return amount



def problem3(fnc , n):
    strg = ""
    for i in range(n+1):
        strg += str(i)
        
    result = strg.count("1")
    
    a = ffunc(n)

    if result == a : 
        return True
    
    else: 
        return False

    
        
  

def problem4(strg):
    strg_lower = strg.lower()
    
    
    word_list = list(strg_lower)
    result = []
    i = 0
    
    while i < len(strg_lower):
        for j in range(len(strg_lower)):
            if strg_lower[j:] not in result:
                result.append(strg_lower[j:])
                
        
        word_list.insert(0,word_list[len(word_list)-1])
        word_list.pop()
        
        strg_lower = "".join(word_list)
        
        i += 1
    
        
    result_sort = sorted(result)
    
    return result_sort
        
        
    

  
  
def problem5(strg):
    strg_lower = strg.lower()
    words = []
    amount = []
    result = ""
    
    for i in strg_lower:
        if i not in words:
            words.append(i)
            
    for i in words:
        amount.append(str(strg_lower.count(i))) 
        
    
    for i in range(len(amount)):
        if amount[i] == "1":
            amount[i] = ""
            
    
    i = 0    
    while i < len(words):
        result += words[i]
        result += amount[i]
        i += 1
        
    percentage = ((len(strg_lower) - len(result)) * 100) / len(strg_lower) 
    
    return result , int(percentage)
    
    
    
    

        
        
        
        
        
    
    
      
    
      
    
            
    
        
    
