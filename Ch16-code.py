import pylab, random
from rcParamsSettings import *

#Page 224, Figure 16.1
def plotHousing(impression):
    """impressionは，’flat’，’volatile’，’fair’
       のいずれかの値をとる文字列と仮定する．
       時間経過に伴う住宅価格の棒グラフを生成する"""
    f = open('midWestHousingPrices.txt', 'r')
    #ファイルの各行は，アメリカ合衆国中西部の四半期ごとの価格を表している．
    labels, prices = ([], [])
    for line in f:
        year, quarter, price = line.split()
        label = year[2:4] + '\n Q' + quarter[1]
        labels.append(label)
        prices.append(float(price)/1000)
    quarters = pylab.arange(len(labels)) #棒グラフのx座標
    width = 0.8 #棒グラフの幅
    if impression == 'flat':
        pylab.semilogy()
    pylab.bar(quarters, prices, width)
    pylab.xticks(quarters+width/2.0, labels)
    pylab.title(‘アメリカ合衆国中西部での住宅価格')
    pylab.xlabel(‘四半期’)
    pylab.ylabel(‘平均価格 ($1,000\'s)')
    if impression == 'flat':
        pylab.ylim(10, 10**3)
    elif impression == 'volatile':
        pylab.ylim(180, 220)
    elif impression == 'fair':
        pylab.ylim(150, 250)
    else:
        raise ValueError

plotHousing('flat')
pylab.figure()
plotHousing('volatile')
pylab.figure()
plotHousing('fair')

#Page 231, Figure 16.2
def juneProb(numTrials):
    june48 = 0
    for trial in range(numTrials):
      june = 0
      for i in range(446):
          if random.randint(1,12) == 6:
              june += 1
      if june >= 48:
          june48 += 1
    jProb = june48/float(numTrials)
    print ‘六月に少なくとも48人が生まれる確率 =', jProb

#Page 231, Figure 16.3
def anyProb(numTrials):
    anyMonth48 = 0
    for trial in range(numTrials):
      months = [0]*12
      for i in range(446):
          months[random.randint(0,11)] += 1
      if max(months) >= 48:
          anyMonth48 += 1
    aProb = anyMonth48/float(numTrials)
    print ‘いずれかの月に少なくとも48人が生まれる確率 =', aProb
