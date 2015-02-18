# coding: utf-8
import pylab, random
#from rcParamsSettings import *

#次の2つの関数は以前定義したものであり，
#この章で使う．
def stdDev(X):
    """Xを数のリストと仮定する．
       Xの標準偏差を返す"""    
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #平均との平方根

def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

#194ページ，図14.1
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    """numTrialsは1以上の整数（int）と仮定する
       勝利する確率の評価値を表示する"""
    numWins = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print '勝利する確率 =', numWins/numTrials

#196ページ, 図14.2
class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = (0,0)
        self.dpWins, self.dpLosses, self.dpPushes = (0,0,0)

    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break

    def passResults(self):
        return (self.passWins, self.passLosses)

    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)

#197ページ, 図14.3
def crapsSim(handsPerGame, numGames):
    """handsPerGameとnumGamesは1以上の整数（int）と仮定する
       handsPerGameの手から成るゲームをnumGames回プレイし，
       その結果を表示する"""
    games = []

    #ゲームをnumGames回プレイする
    for t in xrange(numGames):
        c = CrapsGame()
        for i in xrange(handsPerGame):
            c.playHand()
        games.append(c)
        
    #各ゲームの統計値を求める
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))
        
    #統計値の概要を求めて表示する
    meanROI = str(round((100.0*sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100.0*stdDev(pROIPerGame), 4)) + '%'
    print 'バス:', 'ROIの平均値 =', meanROI, 'Std. Dev. =', sigma
    meanROI = str(round((100.0*sum(dpROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100.0*stdDev(dpROIPerGame), 4)) + '%'
    print 'ドントバス:','ROIの平均値 =', meanROI, '標準偏差 =', sigma

#200ページ,　図14.4
def playHand(self):
    #playHandの，より高速な，もう1つの実装
    pointsDict = {4:1/3.0, 5:2/5.0, 6:5/11.0, 8:5/11.0,
                  9:2/5.0, 10:1/3.0}
    throw = rollDie() + rollDie()
    if throw == 7 or throw == 11:
        self.passWins += 1
        self.dpLosses += 1
    elif throw == 2 or throw == 3 or throw == 12:
        self.passLosses += 1
        if throw == 12:
            self.dpPushes += 1
        else:
            self.dpWins += 1
    else:
        if random.random() <= pointsDict[throw]: #7の前にポイントが出る
            self.passWins += 1
            self.dpLosses += 1
        else:                                    #ポイントの前に7が出る
            self.passLosses += 1
            self.dpWins += 1

#Page 203, Figure 14.5
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in xrange(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    #一つの象限内の針のみ数えるため，4倍する
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print '評価値 = ' + str(round(curEst, 5)) +          ', 標準偏差 = ' + str(round(sDev, 5))          + ', 針の数 = ' + str(numNeedles)
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2.0:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst
