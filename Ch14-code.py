import pylab, random
from rcParamsSettings import *

#����2�̊֐��͈ȑO��`�������̂ł���C
#���̏͂Ŏg���D
def stdDev(X):
�@�@�@"""X�𐔂̃��X�g�Ɖ��肷��D
       X�̕W���΍���Ԃ�"""    
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #���ςƂ̕�����

def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

#194�y�[�W�C�}14.1
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    """numTrials��1�ȏ�̐����iint�j�Ɖ��肷��
       ��������m���̕]���l��\������"""
    numWins = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print '��������m�� =', numWins/numTrials

#196�y�[�W, �}14.2
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

#197�y�[�W, �}14.3
def crapsSim(handsPerGame, numGames):
    """handsPerGame��numGames��1�ȏ�̐����iint�j�Ɖ��肷��
       handsPerGame�̎肩�琬��Q�[����numGames��v���C���C
       ���̌��ʂ�\������"""
    games = []

    #�Q�[����numGames��v���C����
    for t in xrange(numGames):
        c = CrapsGame()
        for i in xrange(handsPerGame):
            c.playHand()
        games.append(c)
        
    #�e�Q�[���̓��v�l�����߂�
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))
        
    #���v�l�̊T�v�����߂ĕ\������
    meanROI = str(round((100.0*sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100.0*stdDev(pROIPerGame), 4)) + '%'
    print �e�o�X:�f, �eROI�̕��ϒl =', meanROI, 'Std. Dev. =', sigma
    meanROI = str(round((100.0*sum(dpROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100.0*stdDev(dpROIPerGame), 4)) + '%'
    print �e�h���g�o�X:','ROI�̕��ϒl =', meanROI, �e�W���΍� =', sigma

#200�y�[�W,�@�}14.4
def playHand(self):
    #playHand�́C��荂���ȁC����1�̎���
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
        if random.random() <= pointsDict[throw]: #7�̑O�Ƀ|�C���g���o��
            self.passWins += 1
            self.dpLosses += 1
        else:                                    #�|�C���g�̑O��7���o��
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
    #��̏ی����̐j�̂ݐ����邽�߁C4�{����
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print �e�]���l = ' + str(round(curEst, 5)) +\
          ', �W���΍� = ' + str(round(sDev, 5))\
          + ', �j�̐� = ' + str(numNeedles)
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2.0:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst
