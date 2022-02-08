from random import randint


class game():
    def __init__(self): 
        a = int(input('Hazır Save ye geçmek istiyormusun ?\n1-Evet\n2-Hayır'))
        if a == 1:
            self.userStats = self.getStats()
            print(f'Hoşgeldin {self.userStats[0]}\nMoney:{self.userStats[1]}\nWin:{self.userStats[2]}\nLose:{self.userStats[3]}')
        if a == 2:
            #userStats 0 = username 1 = money 2 = winpoint 3 = losepoint
            username = input('UserName:')
            self.userStats = [username,500,0,0]
        self.Start()
    #------------Start Game's----------#
    def Start(self):
         while True: # Kullanıcıya Oyun seçtirmek
            a = int(input('Hangi Oyunu oynamak istersin ?\n\t1-'))
            if a == 1:
                self.guessNumber()


    #------------Save Profile----Get Profile-----------#

    def saveStats(self): # txt üerine kullanıcı bilgilerini yazmak
        with open('game/moneyStats.txt','w',encoding='utf-8') as f:
            f.write(f'{self.userStats[0]}:{self.userStats[1]}:{self.userStats[2]}:{self.userStats[3]}')

    def getStats(self): # txt uzerinden kullanıcı bilgilerini çekmek
       
        with open('game/moneyStats.txt','r',encoding='utf-8') as f:
           return f.readline().split(':')

    #--------------Win-Lose-Progress-----------#
    def getWin(self,bet):
        self.userStats[1] = self.userStats[1] + (bet * 2)
        print(f'kazandın\n\tKazancın:{bet * 2}\n\tToplam Paran{self.userStats[1]}')
        self.saveStats()
    def getLose(self,bet):
        print(f'{bet} kadar para kaybettin')
    #---------------------Bet--------------------#
    def getBet(self):
        while True:
            bet = int(input('Bahis:'))
            if int(self.userStats[1]) >= bet:
                return bet
            else:
                print(f'Yeterli paranız bulunmamaktadır. ({self.userStats[1]})')
                
    #--------------------Games---------------------#
    def guessNumber(self): #Sayı Tahmin oyunu bet ile beraber
        bet = self.getBet()
        self.userStats[1] = int(self.userStats[1])
        self.userStats[1] = self.userStats[1] - bet
        number = randint(0,10)
        print(number)
        for x in range(0,5):
            guess = int(input('tahmin:'))
            if number == guess:
                self.getWin(bet)
                break
            else:
                print('Bilemedin Tekrar Dene')
                self.saveStats()
        
        print('-- Oyun bitti --')
            


