import random

class Game:
    def __init__(self):
        self.Players = list()
        self.CTPlayers = list()
        self.TPlayers = list()
        self.SpecPlayers = list()
    def JoinPlayer(self,player,team):
        self.Players.append(player)
        if team==0:
            self.SpecPlayers.append(player)
        elif team==1:
            self.CTPlayers.append(player)
        else:
            self.TPlayers.append(player)
    def NewGame(self):
        for player in self.Players:
            player.NewGameDefaults()
        self.StatScoreCT = 0
        self.StatScoreT = 0
        self.CurrentRound=1
        self.isGameEnded = False
    def NewRound(self):
        for player in self.Players:
            player.NewRoundDefaults()
        self.CurrentRound+=1
    def ProcessRound(self):
            if self.isGameEnded:
                return('Game is ended.')
            self.NewRound()
            random.seed()
            if random.choice([True,False]):
                msgresult='CT wins the round!'
                self.StatScoreCT+=1
            else:
                msgresult='T wins the round!'
                self.StatScoreT+=1
            self.isGameEnded = self.StatScoreCT==16 or self.StatScoreT==16 or (self.StatScoreT+self.StatScoreCT==30)
            return(msgresult)
    def GameStat(self):
        return('CT:{} T:{}'.format(self.StatScoreCT,self.StatScoreT))


class Player:
    def __init__(self,name):
        self.nickname=name
        self.NewGameDefaults()
        self.NewRoundDefaults()
    def __str__(self):
        return('{} HP{} A{}'.format(self.nickname,self.hp,self.ap))
    def NewGameDefaults(self):
        self.StatK,self.StatA,self.StatD=0,0,0
        self.hp,self.ap=100,0
    def NewRoundDefaults(self):
        self.x,self.y,self.z=200,200,50
        self.bullpacks,self.bullets=3,30
        self.hp=100
    def isDead(self):
        return(self.hp==0)
    def Spawn(self):
        self.__init__(self.nickname)
        self.NewRoundDefaults()
    def Kill(self):
        self.hp=0
        self.ap=0
        self.StatD+=1
    def Fight(self,enemy):
        if self.isDead() or enemy.isDead():
            return
        elif self.hp>enemy.hp:
            enemy.Kill()
            self.StatK+=1
        elif self.hp<enemy.hp:
            self.Kill()
            enemy.StatK+=1
        else:
            random.seed()
            if random.choice([True,False]):
                enemy.Kill()
                self.StatK+=1
            else:
                self.Kill()
                enemy.StatK+=1


game = Game()
zheka = Player('-=Zheka=-')
simple = Player('NaVi~S1mple')
game.JoinPlayer(zheka,1)
game.JoinPlayer(simple,2)
game.NewGame()
while True:
    roundresult = game.ProcessRound()
    print('Round {}: {}'.format(game.CurrentRound-1,roundresult))
    if game.isGameEnded:
        break
print(game.GameStat())
