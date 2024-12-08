my_name = "Yunus Emre Buyukyilmaz"
my_id = "220102002054"
my_email = "y.buyukyilmaz2022@gtu.edu.tr"




def problem0():
    class p0():
        
        def __init__(self,x):
            self.x = x
            
        def set_value(self,x):
            self.x = x
            
        def get_value(self):
            return self.x
        
        
    return p0



def problem1():
    class p1():

        def __init__(self,x):
            self.x = x
            
        def get_value(self):
            if type(self.x) != int:
                return 0
            
            else:
                return self.x
            
        def set_value(self,x):
            self.x = x
    
    return p1      
            

def problem2():
    class p2():
        
        def __init__(self,x,y):
            self.x = x
            self.y = y
            
        def get_area(self):
            area = self.x * self.y
            return area
        
        def get_perimeter(self):
            perimeter = (self.x + self.y) * 2
            return perimeter
    
    return p2  


def problem3():
    class Grades():      

        def __init__(self):
            self.grades = []
            
        
        def add_grade(self,x):
            self.grades.append(x)
            
        def remove_grade(self,x):
            if x in self.grades:
                self.grades.remove(x) 
                
        def get_min(self):
            if len(self.grades) == 0:
                return 0.0
            else:
                return float(min(self.grades))
        
        def get_max(self):
            if len(self.grades) == 0:
                return 0.0
            else:
                return float(max(self.grades))
        
        def get_mean(self):
            if len(self.grades) == 0:
                return 0.0
            else:
                average = 0
                for i in self.grades:
                    average += i
                    
                return float(average / len(self.grades))
                
                
        def get_median(self):
            if len(self.grades) == 0:
                return 0.0
            
            else:
                if len(self.grades) % 2 == 0:
                    a = (len(self.grades)/2)-1
                    b = (len(self.grades)/2)
                    result1 = self.grades[int(a)] + self.grades[int(b)]  
                    return float(result1 / 2)   
                
                else:
                   a = ((len(self.grades)+1)/2) - 1
                   result2 = self.grades[int(a)] 
                   return float(result2) 

    return Grades    
                
            
        
def problem4():
    class Movie():
        
        def __init__(self,movie_name,director,year,rating = 0.0,length = 0):
            self.movie_name = str(movie_name)
            self.director = str(director)
            self.year = int(year)
            self.rating = float(rating) 
            self.lenght = float(length)
            
            
        def get_movie_name(self):
            return self.movie_name
        
        def get_director(self):
            return self.director
        
        def get_year(self):
            return self.year
        
        
        def get_rating(self):
            return self.rating
        
        def get_length(self):
            return self.lenght
        
        def set_rating(self,x):            
            self.rating = x
            
        def set_length(self,x):
            self.lenght = x
            
    return Movie   
    

def problem5():   
    A = problem4()
    
    class MovieCatalog(A):
        def __init__(self,filename):
            self.filename = filename
            self.movies_list = []
            self.temp_list = []
            self.temp1_list = []
            
            dosya = open(self.filename,"r")
            splt = dosya.readlines() 
            self.temp_list = [i.strip() for i in splt]
            
            for i in self.temp_list:
                self.temp1_list.append(i.split(","))
                
                
            for i in range(len(self.temp_list)):
                movie = A( 
                        movie_name = self.temp1_list[i][0],
                        director = self.temp1_list[i][1],        
                        year = self.temp1_list[i][2],
                        rating = self.temp1_list[i][3],
                        length = self.temp1_list[i][4]
                                                       )
                self.movies_list.append(movie)         

                
                
        def add_movie(self,movie_name, director, year, rating=0.0, length=0):
            movies_name_list = []
            
            for i in self.movies_list:
                
                movies_name_list.append(i.get_movie_name()) 
                
            if movie_name not in movies_name_list:
                new_movie = A(movie_name, director, year, rating, length)
                self.movies_list.append(new_movie)
                
                
        def remove_movie(self,movie_name):
            
            for i in self.movies_list:
                if i.get_movie_name() == movie_name:
                    self.movies_list.remove(i)
                    
                    
        def get_oldest(self):
            year = []
            
            for i in self.movies_list:
                year.append(i.get_year())
            
            oldest = min(year)   
            
            for i in self.movies_list:
                if i.get_year() == oldest:
                    return i.get_movie_name()
                
            
                
        def get_lowest_ranking(self):
            rank = []    
            
            for i in self.movies_list:
                rank.append(i.get_rating())
            
            lowest = min(rank)   
            
            for i in self.movies_list:
                if i.get_rating() == lowest:
                    return i.get_movie_name() 

            
        def get_highest_ranking(self):
            rank = []    
            
            for i in self.movies_list:
                rank.append(i.get_rating())
            
            highest = max(rank)   
            
            for i in self.movies_list:
                if i.get_rating() == highest: 
                    return i.get_movie_name() 
            
            
        def get_by_director(self,director):
            
            director_list = []
            
            for i in self.movies_list:
                if i.get_director() == director:
                    director_list.append(i.get_movie_name())
                    
            return director_list
        
        

    return MovieCatalog           
        
        

  

