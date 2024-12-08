


def problem1(row , column):
    if row == 1 and column == 1:
        return 1
    if row > 1 and column == 1:
        return 3
    if row == column:
        return 2
    
    
    return problem1(row-1 , column-1) + problem1(row-1, column)







def problem2(user1 , user2):
    min_str = user2
    max_str = user1
    lenght = 0
    if len(user1) <= len(user2):
        min_str = user1
        max_str = user2

    for i in range(len(min_str)):
        if min_str[i] == max_str[i]:
            lenght += 1 
                
    return lenght      
            
       
       
       
       

def problem3(accounts, source, destination, lira, kurus, fee = False):
    
    if fee == False:
        return accounts
    
    if source == destination:
        return accounts
    
    elif source > len(accounts) or destination > len(accounts) or source < 0 or destination < 0:
        return accounts
    
    
    money = (lira + kurus/100) 
    transfer_from = float(accounts[source])
    transfer_to = float(accounts[destination])
    

    
    if money <= transfer_from:
         if money < 10:
            fee = True
            transfer_from = transfer_from - (money + 0.1)
            a = int(transfer_from * 100) / 100
            
            transfer_to += money
            b = int(transfer_to * 100) / 100
            
            a_str = str(a)
            b_str = str(b)
            if len(a_str.split(".")[1]) == 1 and a_str.split(".")[1] != "0" :
                a_str += "0"
            if len(b_str.split(".")[1]) == 1 and b_str.split(".")[1] != "0":
                b_str += "0"    
            
                
            
            accounts[source] = a_str 
            accounts[destination] = b_str 
            
            
            
         else:
            fee = True
            percent1 = int((money/100) * 100) / 100
            
            transfer_from = transfer_from - (money + percent1)
            a = int(transfer_from * 100) / 100
            
            transfer_to += money 
            b = int(transfer_to * 100) / 100  
            
            a_str = str(a)
            b_str = str(b)
            if len(a_str.split(".")[1]) == 1 and a_str.split(".")[1] != "0" :
                a_str += "0"
            if len(b_str.split(".")[1]) == 1 and b_str.split(".")[1] != "0":
                b_str += "0"
                
            accounts[source] = a_str 
            accounts[destination] = b_str     
             
    return accounts
    
    
    
    

      





