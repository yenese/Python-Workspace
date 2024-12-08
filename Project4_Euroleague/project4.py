import random




class Person():

    def  __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def  get_name(self):
        return self.name + " " +self.lastname

    
    def  __str__(self):
        return self.name + " " +self.lastname
    
    def  __lt__(self,player1):
        if self.lastname == player1.lastname:
            return self.name < player1.name 
    
        else:
            return self.lastname < player1.lastname
         



class Player(Person):

    i = 0

    def __init__(self,name, lastname):

        Player.i += 1

        self.name = name
        self.lastname = lastname
        self.shooting_power = random.randint(4,8)
        self.player_id = Player.i
        self.points = 0
        self.points_detailed = []
        self.team = None
        

        
   
    def reset(self):
        self.points = 0
        self.points_detailed = []

    def  get_id(self):
        return self.player_id
    

    def  get_power(self):
        return self.shooting_power
    
    def set_team(self, t):
        self.team = t

    def  get_team(self):
        return self.team
        
    def  add_to_points(self, x):
        self.points += x


    def get_points_detailed(self):
        return self.points_detailed

    def  get_points(self):
        total_points = 0
        for i in self.points_detailed:
            total_points += i
        return total_points
    
    def __lt__(self,x):
        if self.get_points() == x.get_points():
            if self.lastname == x.lastname:
                return self.name < x.name
            
            else:
                return self.lastname < x.lastname
            
        else:
            return self.get_points() < x.get_points()



    
   

    


class Manager(Person):

    i = 0

    def  __init__(self,name, lastname):

        Manager.i += 1

        self.name = name
        self.lastname = lastname
        self.influence = 0
        self.manager_id = Manager.i
        self.influence_detailed = []
        self.team = None

    def  reset(self):
        self.influence = 0  
        self.influence_detailed = []

    def  get_id(self):
        return self.manager_id
    

    def  set_team(self,t):
        self.team = t

    def  get_team(self):
        return self.team

    def  get_influence_detailed(self):
        return self.influence_detailed

    def get_influence(self):
        total_influence = 0
        for i in self.influence_detailed:
            total_influence += i
        return total_influence
    
    def __lt__(self,x):
        if self.get_influence() == x.get_influence():
            if self.lastname == x.lastname:
                return self.name < x.name
            
            else:
                return self.lastname < x.lastname
            
        else:
            return self.get_influence() < x.get_influence()

    


class Team():

    i = 0

    def  __init__(self,teamname, manager,players):
        Team.i += 1
        self.teamname = teamname
        self.manager = manager
        self.players = players
        self.team_id = Team.i
        self.team_fixture = []
        
     
        self.wins = 0
        self.losses = 0
        self.scored = 0
        self.conceded = 0

        self.team_score = 0




    def  reset(self):
        self.influence = 0
        for i in self.players:
            i.reset()

        self.team_fixture = 0
        self.wins = 0
        self.losses = 0
        self.scored = 0
        self.conceded = 0

        self.team_score = 0
            
    def  get_id(self):
        return self.team_id


    def get_name(self):
        return self.teamname
    
    def  get_roster(self):
            return self.players 
        

    def  get_manager(self):
            return self.manager
        
    def  add_to_fixture(self,m):
        self.team_fixture.append(m)

    def  get_fixture(self):
        return self.team_fixture
    
    def  add_result(self,s):
        self.scored += s[0]
        self.conceded += s[1]

        if s[0] > s[1]:
            self.wins += 1

        else:
            self.losses += 1

    def get_scored(self):
        return self.scored

    def get_conceded(self):
        return self.conceded

    def  get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def __str__(self):
        return self.teamname   
    
    def __lt__(self,x):
        a = self.scored - self.conceded
        b = x.scored - x.conceded
        if self.wins == x.wins:
            return a < b 

        else:
            return self.wins < x.wins 
        

    
        
        


class Match():
    def __init__(self,home_team, away_team,week_no):
        self.home_team = home_team
        self.away_team = away_team
        self.week_no = week_no
        self.played = False
        self.winner = None


    def  is_played(self):
        return self.played

    def  play(self):
         
         self.home_manager_point =  random.randint(-10, 10)
         self.away_manager_point = random.randint(-10, 10) 

         self.home_points = self.home_manager_point
         self.away_points = self.away_manager_point

         
         for player in self.home_team.players:
             pl_po_pe = 0
             for period in range(4):
                 pl_po_pe += player.shooting_power + random.randint(-10, 10)
                 
                 
             self.home_points += pl_po_pe
             player.points_detailed.append(pl_po_pe)
                 

         for player in self.away_team.players:
             pl_po_pe = 0
             for period in range(4):
                 pl_po_pe += player.shooting_power + random.randint(-10, 10)
                 
             self.away_points += pl_po_pe
             player.points_detailed.append(pl_po_pe)

         
         self.home_team.manager.influence_detailed.append(self.home_manager_point)
         self.away_team.manager.influence_detailed.append(self.away_manager_point)

         while self.home_points == self.away_points:
            for player in self.home_team.players:
                pl_po_pe = 0
                pl_po_pe += player.shooting_power + random.randint(-10, 10)

            self.home_points += pl_po_pe
            player.points_detailed[0] += pl_po_pe

            for player in self.away_team.players:
                 pl_po_pe = 0
                 pl_po_pe += player.shooting_power + random.randint(-10, 10)

            self.away_points += pl_po_pe
            player.points_detailed[0] += pl_po_pe


         if self.away_points > self.home_points:
             self.winner = self.away_team
             self.away_team.wins += 1
             self.home_team.losses += 1

         if self.home_points > self.away_points:
            self.winner = self.away_team
            self.home_team.wins += 1
            self.away_team.losses += 1 

         self.home_team.scored += self.home_points
         self.home_team.conceded += self.away_points

         self.away_team.scored += self.away_points
         self.away_team.conceded += self.home_points
          





         self.played = True   


          
                 
  

    def get_match_score(self):
        return (self.home_points , self.away_points)
    
    def get_teams(self):
        return self.home_team, self.away_team
    
    def get_home_team(self):
            return self.home_team
        
    def get_away_team(self):
            return self.away_team
         
    def  get_winner(self):
        if self.played == True:
                return self.winner
            
        else:
            return self.played


    def __str__(self):
        if self.played == True:
            return f"{self.home_team.get_name()} ({self.home_points}) vs. ({self.away_points}) {self.away_team.get_name()}"       

        
        else:
            return f"{self.home_team.get_name()} vs. {self.away_team.get_name()}"

   
   


class Season():
    def  __init__(self,teams, managers, players):

        self.teams = [] 
        self.managers = []
        self.players = []

        self.teams_list = [] 
        self.managers_list = []
        self.players_list = []


        self.season_played = False

        

        


        

        dosya1 = open(teams,"r")
        splt = dosya1.readlines() 
        self.teams_list = ([i.strip() for i in splt])


        dosya2 = open(managers,"r")
        splt = dosya2.readlines() 
        self.managers_list = ([i.strip() for i in splt])


        dosya3 = open(players,"r")
        splt = dosya3.readlines() 
        self.players_list = ([i.strip() for i in splt])


        self.separated_players = []
        for player in self.players_list:
                names = player.split(' ')
                self.separated_players.append({'first_name': names[0], 'last_name': names[-1]})

        self.separated_managers = []
        for manager in self.managers_list:
                names = manager.split(' ')
                self.separated_managers.append({'first_name': names[0], 'last_name': names[-1]})

       

        for name in self.teams_list:
            first_5 = []
            
            
            i = 0
            while i < 5:
                first_5.append(Player(self.separated_players[0]["first_name"],self.separated_players[0]["last_name"]))

                self.players.append(Player(self.separated_players[0]["first_name"],self.separated_players[0]["last_name"]))
                self.separated_players.pop(0)
                i += 1

            self.managers.append(Manager(self.separated_managers[0]["first_name"],self.separated_managers[0]["last_name"]))
            team = Team(name,Manager(self.separated_managers[0]["first_name"],self.separated_managers[0]["last_name"]),first_5)

            self.separated_managers.pop(0)

            self.teams.append(team)


        self.build_fixture()

        




    def reset(self):
        for i in self.teams:
            i.reset()
        for j in self.managers:
            j.reset()
        for k in self.players:
            k.reset()

        self.season_played = False 
        


    def  build_fixture(self):

        teams_count = len(self.teams)
        week = teams_count - 1

        if teams_count % 2 == 1:
            week = teams_count

        devre = int((week + 1) / 2)

        liste = list(range(1, week + 2))

        self.matches = []
        for r in range(week):
            week_matches = []
            for m in range(devre):
                home_team = self.teams[liste[m] - 1]
                away_team = self.teams[liste[-1 - m] - 1]
                match = Match(home_team, away_team, r)
                home_team.add_to_fixture(away_team)
                away_team.add_to_fixture(home_team)
                week_matches.append(match)
                
            liste.remove(week - r + 1)
            liste.insert(1, week - r + 1)

            self.matches.append(week_matches)

        
        self.reversed_fixture = []
        for i in self.matches:
            reversed_week_matches = [Match(match.away_team, match.home_team, match.week_no) for match in i]
            self.reversed_fixture.append(reversed_week_matches)

        self.full_fixture = self.matches + self.reversed_fixture

        


        for i in self.teams:
            for j in range(week):
                i.add_to_fixture(i.get_fixture()[j])


        for team in self.teams:
            for player in team.get_roster():
                player.set_team(team)

        for team in self.teams:
                team.manager.set_team(team) 


        
        

        
    def get_week_fixture(self,week_no):

        if week_no > len(self.full_fixture) or week_no < 1:
            return None
        else:
            return self.full_fixture[week_no-1]
        


    def get_week_no(self):
        pass 


    def play_week(self):
        for i in self.full_fixture:
            for j in i:
                j.play()

        self.season_played = True
        

    def get_players(self):
        return self.players
    

    def get_managers(self):
        return self.managers
    
    def get_teams(self):
        return self.teams
        
    def get_season_length(self):
        return len(self.full_fixture)


    def get_best_player(self):
        Best_player = self.teams[0].get_roster()[0] 
        for i in self.teams:
            for j in i.get_roster():
                if j.get_points() > Best_player.get_points():
                    Best_player = j


        return Best_player


    def get_best_manager(self):
        Best_manager = self.teams[0].get_manager()
       
        for i in self.teams:
            if i.get_manager().get_influence() > Best_manager.get_influence():
                Best_manager = i.get_manager()


        return Best_manager
    

    def get_most_scoring_team(self):
        most_scoring_team = self.teams[0]
        liste = []
        for i in self.teams:
            if i.scored > most_scoring_team.scored:
                most_scoring_team = i

        return most_scoring_team
        
    
    def get_champion(self):
        if self.season_played == False:
            return None
        
        else:
            champion_team = self.teams[0]
            liste = []
            for i in self.teams:
                if i.wins > champion_team.wins:
                    champion_team = i

            
            return champion_team
        


            



            
        

                




