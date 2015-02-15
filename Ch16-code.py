import pylab, random
from rcParamsSettings import *

#Page 224, Figure 16.1
def plotHousing(impression):
    """impression�́C�fflat�f�C�fvolatile�f�C�ffair�f
       �̂����ꂩ�̒l���Ƃ镶����Ɖ��肷��D
       ���Ԍo�߂ɔ����Z��i�̖_�O���t�𐶐�����"""
    f = open('midWestHousingPrices.txt', 'r')
    #�t�@�C���̊e�s�́C�A�����J���O���������̎l�������Ƃ̉��i��\���Ă���D
    labels, prices = ([], [])
    for line in f:
        year, quarter, price = line.split()
        label = year[2:4] + '\n Q' + quarter[1]
        labels.append(label)
        prices.append(float(price)/1000)
    quarters = pylab.arange(len(labels)) #�_�O���t��x���W
    width = 0.8 #�_�O���t�̕�
    if impression == 'flat':
        pylab.semilogy()
    pylab.bar(quarters, prices, width)
    pylab.xticks(quarters+width/2.0, labels)
    pylab.title(�e�A�����J���O���������ł̏Z��i')
    pylab.xlabel(�e�l�����f)
    pylab.ylabel(�e���ω��i ($1,000\'s)')
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
    print �e�Z���ɏ��Ȃ��Ƃ�48�l�����܂��m�� =', jProb

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
    print �e�����ꂩ�̌��ɏ��Ȃ��Ƃ�48�l�����܂��m�� =', aProb
