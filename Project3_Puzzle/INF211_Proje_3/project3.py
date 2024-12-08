




def mix_words(arr):      #solve_board'ta words listesini karıştırmak için tasarlandı.
    x = "hello"
    i = 0
    while (i<len(words)+100): 
        t1 = int(str(hash(x))) % len(arr)
        x += "a"
        t2 = int(str(hash(x))) % len(arr)
        temp = arr[t1]
        arr[t1] = arr[t2]
        arr[t2] = temp
        i += 1
        x += "a" 

    return arr 

def del_board():   #print_board_w_c de kullanmak için tasarlandı.
    del board[0]
    for i in range(len(board)):
        del board[i][0]
        
    for i in board:
        for j in range(len(i)):
            if i[j] == " ":
                i[j] = "1"
 
            elif i[j] == "+":
                i[j] = "0"
        
        



def read_file(filename="test_puzzle.txt"):
    dosya = open(filename,"r")
    splt = dosya.readlines() 
    list = [i.strip() for i in splt]
    board = []
    words = []  
    for i in list:
         
        if i.isalpha():
            words.append(i)  
        
        elif i.isdigit():
            board.append(i) 
    
       
            
    return words , board

    

def check_consistency(board):
    a = len(board[0])
    check =  True
    for i in board:
        if len(i) != a:
            check = False
            
    return check 
    


def create_board(boarD): 
    global board
    board_lol = []
    for i in range(len(board)):
        a = board[i].split()

        for j in a:
            board_lol.append(list(j))
            
    board = board_lol 
    

            
   
    
def identifier(words):
    stat = []
    for i in range(len(words)):
        stat.append(False)
        
    return stat    


def print_board(board):
    for i in board:
        for j in range(len(i)):
            if i[j] == "1":
                i[j] = " "
 
            elif i[j] == "0":
                i[j] = "+"
                          
    str_board = [''.join(i) for i in board]
    
    for i in str_board:
        print(i)
    

def print_board_w_c(board):
    row = [" "]
    for i in range(len(board[0])):
        row.append(f"C{i+1}")
        
    board.insert(0,row)
    
    for i in range(1, len(board)):
        board[i].insert(0, f"R{i}")    
    for i in board:
        for j in range(len(i)):
            if i[j] == "1":
                i[j] = " "
 
            elif i[j] == "0":
                i[j] = "+"   
    str_board = [' '.join(i) for i in board]
    
    board = str_board
    
    
     

    for i in board:
        print(i)
        
    
    del_board() 
        
    


def print_wordlist(words,wstatus):
    word_list = ["Word List         Status"]
    
    for i in range(len(wstatus)):
        if wstatus[i] == False:
            wstatus[i] = "NOT USED"
        elif wstatus[i] == True:
            wstatus[i] = "USED"    
    
    
    for i in range(1,len(words)+1):
        word_list.insert(i , f"W{i}" + "  " + words[i-1] + "           " + f"{wstatus[i-1]}" ) 
        
   
    for i in word_list:
        print(i)
             

    
        
def decompose_command(str1):
    str1_low = str1.lower() 
    check = -1
    check_list = []
    word_number = "" 
    coordinates_list = []
    row = ""
    columns = ""
    direction = ""
    list_necessary = ["w" , "r" , "c" , "d"]

    for i in range(len(str1_low)):
        if str1_low[i] == "w" and str1_low[i+1].isdigit():
            check_list.append(0)
        elif str1_low[i] == "r" and str1_low[i+1].isdigit():
            check_list.append(0)
        elif str1_low[i] == "c" and str1_low[i+1].isdigit():
            check_list.append(0)
        elif str1_low[i] == "d" and str1_low[i+1].isalpha():
            check_list.append(0)

    if len(check_list) == 4:
        check = 0
      
    count = 0  
    for i in str1_low:
        if i.isalpha():
            count += 1
    if count > 5 :
        check = -1   
            
      
    if check == 0:
        for i in range(len(str1_low)-1):
            if str1_low[i] == "w":
                i += 1  
                while i < len(str1_low) and str1_low[i].isdigit():
                    word_number += str1_low[i]
                    i += 1
                    
        word_number = int(word_number)      
        
        for i in range(len(str1_low)-1):
            if str1_low[i] == "r":
                i += 1  
                while i < len(str1_low) and str1_low[i].isdigit():
                    row += str1_low[i]
                    i += 1        
       
        for i in range(len(str1_low)-1):
            if str1_low[i] == "c":
                i += 1  
                while i < len(str1_low) and str1_low[i].isdigit():
                    columns += str1_low[i]
                    i += 1
       
        columns = int(columns)
        row = int(row)
        coordinates_list.append(columns)
        coordinates_list.insert(0, row) 
        
        
        for i in range(len(str1_low)-1):
            if str1_low[i] == "d":
                if str1_low[i+1] == "v":
                    direction = "V"      
                
                else:
                    direction = "H"   
                            
        return check , word_number , coordinates_list , direction
 
                
    else:
        return -1 , None , None , None  
    
    

def check_entries(coordinates,wordno,board,words): 
    check1 = True
    check2 = True
    for i in coordinates:
        if i > len(board) or i < 0:
            check1 = False

    if wordno > len(words) or wordno < 0:
        check2 = False
        
        
    return check1 , check2
            
    
def check_location(board,words,coordinates,wordno,direction='H'):
    
    if check_entries(coordinates,wordno,board,words) == (True,True):
        
        check = 0
    
        if board[coordinates[0]-1][coordinates[1]-1] == "0":
            check = 1
            return False ,1

        
        
        if direction == "V": #before
            if coordinates[0] != 1:
                if board[coordinates[0]-2][coordinates[1]-1] == "1"or board[coordinates[0]-2][coordinates[1]-1].isalpha():
                    check = 1 
                    return False ,2 
                
        
        if direction == "H":  #before
            if coordinates[1] != 1:
                if board[coordinates[0]-1][coordinates[1]-2] == "1" or board[coordinates[0]-1][coordinates[1]-2].isalpha():
                    check = 1
                    return False , 3
                
                
            
        if direction == "H": #doesn't fit  
            i = 1
            x = 2
            a = 0
            
            while i<len(words[wordno - 1])+1: 
                if coordinates[1] == 1:
                    a = -1
                    x = 1 
                if 0 <= coordinates[0]-1 < len(board) and 0 <= coordinates[1]-x+i+a < len(board[0]):
                    if board[coordinates[0]-1][coordinates[1]-x+i+a] == "0":
                        check = 1
                        return False,5
                    
                    
                i += 1
                
        
        
        if direction == "V": #doesn't fit    
            i = 1
            x = 2
            a = 0
            
                    
            while i<len(words[wordno - 1])+1: 
                if coordinates[0] == 1:
                    a = -1
                    x = 1
                
                if 0 <= coordinates[0] - x + i + a < len(board) and 0 <= coordinates[1] - 1 < len(board[0]):
                    if board[coordinates[0] - x + i + a][coordinates[1] - 1] == "0":
                        check = 1
                        return False, 8
                i += 1
            
            
            
        if direction == "H": #exceed     
            space = 0
            i = 1
            x = 2
            a = 0
            y = coordinates[1]
            
            while y<len(board[0])+1:
                if coordinates[1] == 1:
                    a = -1
                    x = 1
                if board[coordinates[0]-1][coordinates[1]-x+i+a] == "1" or board[coordinates[0]-1][coordinates[1]-x+i+a].isalpha():
                    space += 1
                i += 1
                y += 1
                
                        
                            
            if len(words[wordno-1]) > space:
                check = 1
                return False,4 
                    
            
            
        if direction == "V": #exceed   
            space = 0
            i = 1
            x = 2
            a = 0
            y = coordinates[0]
                    
            while y<len(board)+1:
                if coordinates[0] == 1:
                    a = -1 
                    x = 1
                if board[coordinates[0]-x+i+a][coordinates[1]-1] == "1" or board[coordinates[0]-x+i+a][coordinates[1]-1].isalpha():
                    space += 1
                i += 1
                y += 1
                
                
                
            if len(words[wordno-1]) > space:
                check = 1
                return False,7 
            
                
        
        if direction == "H": #next   
            lenght = len(words[wordno-1])
            space = 0
            i = 1
            x = 2
            a = 0
            y = coordinates[1]
            
            while y<len(board[0])+1:
                if coordinates[1] == 1:
                    x = 1
                    a = -1                
                if board[coordinates[0]-1][coordinates[1]-x+i+a] == "1" or board[coordinates[0]-1][coordinates[1]-x+i+a].isalpha():
                    space += 1
                i += 1
                y += 1
            
            if space != len(words[wordno-1]):  
                if board[coordinates[0]-1][lenght] == "1" or board[coordinates[0]-1][lenght].isalpha() :
                    check = 1
                    return False ,6
                
                
        if direction == "V": #next 
            lenght = len(words[wordno-1])
            space = 0
            i = 1
            x = 2
            a = 0
            y = coordinates[0]
                    
            while y<len(board)+1:
                if coordinates[0] == 1:
                    a = -1
                    x = 1
                if board[coordinates[0]-x+i+a][coordinates[1]-1] == "1" or board[coordinates[0]-x+i+a][coordinates[1]-1].isalpha():
                    space += 1
                i += 1
                y += 1
                
            if space !=  len(words[wordno-1]):
                if board[lenght][coordinates[1]-1] == "1" or board[lenght][coordinates[1]-1].isalpha() :
                        check = 1
                        return False , 9
            
        if check == 0:
                return True,0 
              
         

def check_word_fits(board,words,coordinates,wordno,direction='H'):
    
    if direction == "V":              
        common = 0
        space = 0
        i = 1
        x = 2
        a = 0
                
        while i<len(words[wordno - 1])+1:     
            if coordinates[0] == 1:
                a = -1
                x = 1
            if board[coordinates[0]-x+i+a][coordinates[1]-1] == "1" or board[coordinates[0]-x+i+a][coordinates[1]-1] == words[wordno-1][i-1]:
                space += 1
            
            
            i += 1
            
            
        if len(words[wordno-1]) == space:
            return True,0
        
        else:
            return False,1
        
    if direction == "H":    
        common = 0
        space = 0
        i = 1
        x = 2
        a = 0
        while i<len(words[wordno - 1])+1:
            if coordinates[1] == 1:
                a = -1
                x = 1 
            if board[coordinates[0]-1][coordinates[1]-x+i+a] == "1" or board[coordinates[0]-1][coordinates[1]-x+i+a] == words[wordno-1][i-1]:
                space += 1
                
            i += 1
        
            
        
                           
        if len(words[wordno-1]) == space:
            return True,0 
        
        else:
            return False,2
    
    
def clear_board(board,wstatus):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].isalpha():
                board[i][j] = "1"
            
    for i in range(len(wstatus)):
        if wstatus[i] is not False:
            wstatus[i] = False







def word_it(board,words,wstatus,coordinates,wordno,direction):
    
    check = 0
    
    if check_entries(coordinates,wordno,board,words) == (True,True):
        check = 1
        if check_location(board,words,coordinates,wordno,direction) == (True,0):
            check = 2
            if check_word_fits(board,words,coordinates,wordno,direction) == (True,0):
                check = 3
                if wstatus[wordno-1] == False:
                     check = 4 
                    
                     if direction == "H":       
                         i = 1
                         x = 2
                         a = 0
                             
                         while i<len(words[wordno - 1])+1:
                             if coordinates[1] == 1:
                                 a = -1
                                 x = 1
                             board[coordinates[0]-1][coordinates[1]-x+i+a] = words[wordno-1][i-1] 
                             i += 1  
                        
                     if direction == "V":    
                        i = 1
                        x = 2
                        a = 0
                                
                        while i<len(words[wordno - 1])+1:
                            if coordinates[0] == 1:
                                a = -1
                                x = 1
                            board[coordinates[0]-x+i+a][coordinates[1]-1] = words[wordno-1][i-1]  
                            i += 1   
                            
                     
                     wstatus[wordno - 1] = True
                    
                     return True
                     
    if check != 4:
        return False      
          
                  
                  
def copy_board(board):
    copy_board = board
    
    return copy_board
    
    

def track_move(mvn,trackboard,coordinates,wordno,direction,board,wstatus):
    mvn = 0
    trackboard.append(coordinates)
    trackboard.append(wordno)
    trackboard.append(direction)
    trackboard.append(board)
    trackboard.append(wstatus)
    mvn += 1
    
    return mvn


def check_solved(board): 
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "1":
                return False
            
            
    else:
        return True 
    


def solve_board(board,words):
    cmd = ""
    wstatus=identifier(words)  
    
    while check_solved(board) == False:
        for i in range(1,len(words)+1):             
            for j in range(1,len(board)+1):
                for k in range(1,len(board[0])+1):
                            
                    cmd = f"w{i}" + f"r{j}" + f"c{k}" + "dh"
                    iflag, wordno, coordinates, direction = decompose_command(cmd)
                    word_it(board, words, wstatus, coordinates, wordno, direction)
                        

                    if word_it(board, words, wstatus, coordinates, wordno, direction) is True:
                        continue

                    else:
                        cmd = f"w{i}" + f"r{j}" + f"c{k}" + "dv"
                        iflag, wordno, coordinates, direction = decompose_command(cmd)
                        word_it(board, words, wstatus, coordinates, wordno, direction)
    
        
        
        if check_solved(board) == False:
            mix_words(words) 
            clear_board(board,wstatus)   
        
        
          
             
       
    
                        
            
                    
def word_puzzle():
    pass    
                    
                    
    
                
                













  
                
                
                
                
                

    
    
    






