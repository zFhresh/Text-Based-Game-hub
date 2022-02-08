from random import randint


class game():
    def __init__(self): 
        a = int(input('Do you want to load the save game?\n1-Yes\n2-No'))
        if a == 1:
            self.userStats = self.getStats()
            print(f'Welcome: {self.userStats[0]}\nMoney:{self.userStats[1]}\nWin:{self.userStats[2]}\nLose:{self.userStats[3]}')
        if a == 2:
            #userStats 0 = username 1 = money 2 = winpoint 3 = losepoint
            username = input('UserName:')
            self.userStats = [username,500,0,0]
        self.Start()
    #------------Start Game's----------#
    def Start(self):
         while True: # Kullanıcıya Oyun seçtirmek
            a = int(input('what do you want to play\n\t1-Guess the number'))
            if a == 1:
                self.guessNumber()


    #------------Save Profile----Get Profile-----------#

    def saveStats(self): # Load the user info from .txt 
        with open('game/moneyStats.txt','w',encoding='utf-8') as f:
            f.write(f'{self.userStats[0]}:{self.userStats[1]}:{self.userStats[2]}:{self.userStats[3]}')

    def getStats(self): # Get the user info from .txt
       
        with open('game/moneyStats.txt','r',encoding='utf-8') as f:
           return f.readline().split(':')

    #--------------Win-Lose-Progress-----------#
    def getWin(self,bet):
        self.userStats[1] = self.userStats[1] + (bet * 2)
        print(f'You Win\n\Win:{bet * 2}\n\tTotal Coin:{self.userStats[1]}')
        self.saveStats()
    def getLose(self,bet):
        print(f'you lost 200 {bet}')
    #---------------------Bet--------------------#
    def getBet(self):
        while True:
            bet = int(input('Bet:'))
            if int(self.userStats[1]) >= bet:
                return bet
            else:
                print(f'you dont have enough money ({self.userStats[1]})')
                
    #--------------------Games---------------------#
    def guessNumber(self): #Guess the number
        bet = self.getBet()
        self.userStats[1] = int(self.userStats[1])
        self.userStats[1] = self.userStats[1] - bet
        number = randint(0,10)
        print(number)
        for x in range(0,5):
            guess = int(input('Guess:'))
            if number == guess:
                self.getWin(bet)
                break
            else:
                print('Try again')
                self.saveStats()
        
        print('-- Game Over --')
            


