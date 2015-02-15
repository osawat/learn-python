import pylab, random
from rcParamsSettings import *

#����2�̊֐��͈ȑO�̏͂Ŋ��ɒ�`���Ă���C�����ŗp����D
def stdDev(X):
    """X�𐔂̃��X�g�Ɖ��肷��D
       X�̕W���΍���Ԃ�"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #���ςƂ̍��̕�����

def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

#Page 209, Figure 15.1
def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

#Page 209, Figure 15.2
def plotData(inputFile):
    masses, distances = getData(inputFile)
    masses = pylab.array(masses)
    distances = pylab.array(distances)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo',
               label = �e�ψʂ̊ϑ��l')
    pylab.title(�e�o�l�̕ψʂ̊ϑ��l')
    pylab.xlabel('|��| (�j���[�g��)�f)
    pylab.ylabel(�e���� (���[�g��)')


#Page 212, Figure 15.3
def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo',
               label = �e�ψʂ̊ϑ��l')
    pylab.title(�e�o�l�̕ψʂ̊ϑ��l')
    pylab.xlabel('|��| (�j���[�g��)')
    pylab.ylabel(�e���� (���[�g��)�f)
    #1���̓K���Ȑ��i�����j�����߂�
    a,b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a*pylab.array(forces) + b
    k = 1.0/a
    pylab.plot(forces, predictedDistances,
               label = �e�ψʂ̐��`�K���ɂ��\���l, k = '
               + str(round(k, 5)))
    pylab.legend(loc = 'best')
##    pylab.plot(forces, predictedDistances,
##               label = 'Displacements predicted by\nlinear fit, k = '
##               + str(round(k,5)))

#Page 212, additional code for fitData in Fig. 15.3
#3���̓K���Ȑ������߂�
a,b,c,d = pylab.polyfit(forces, distances, 3)
predictedDistances = a*(forces**3) + b*forces**2 + c*forces + d
pylab.plot(forces, predictedDistances, 'b:', label = �e3���̓K��')

#Page 213, �}15.3��fitData���C����������
distances = pylab.array(distances[:-6])
masses = pylab.array(masses[:-6])

#Page 215, Figure 15.4
def getTrajectoryData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    heights1, heights2, heights3, heights4 = [],[],[],[]
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, h1, h2, h3, h4 = line.split()
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return (distances, [heights1, heights2, heights3, heights4])

def processTrajectories(fileName):
    distances, heights = getTrajectoryData(fileName)
    numTrials = len(heights)
    distances = pylab.array(distances)
    #�e�����ɂ����镽�ύ��������z��𓾂�
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    meanHeights = totHeights/len(heights)
    pylab.title(�e���˕��̋O�� ('\
                + str(numTrials) + ' ��̎��s�̕��ϒl)�f)
    pylab.xlabel(�e���˂���̃C���`��')
    pylab.ylabel(�e���˂���̍����i�C���`�j')
    pylab.plot(distances, meanHeights, 'bo')
    a,b = pylab.polyfit(distances, meanHeights, 1)
    altitudes = a*distances + b
    pylab.plot(distances, altitudes, 'b', label = �e���`�K��')
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) +  b*distances + c
    pylab.plot(distances, altitudes, 'b:', label = �e2�̓K��')
    pylab.legend()

#Page 216, Figure 15.5
def rSquared(measured, predicted):
    """measured�͊ϑ��l��ێ�����1�����̔z��
       predicted�͗\���l��ێ�����1�����̔z��Ɖ��肷��
       ����ϐ���Ԃ�"""
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/float(len(measured))
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability

#Page 218, Figure 15.6
def getHorizontalSpeed(a, b, c, minX, maxX):
    """minX��maxX���C���`�P�ʂ̋����Ɖ��肷��D
       ���������̑��x��Ԃ��i�P�ʂ̓t�B�[�g/�b�j�D"""
    inchesPerFoot = 12.0
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*inchesPerFoot #�d�͉����x�i�C���`/�b/�b�j
    t = (2*yPeak/g)**0.5
    print �e���������̑��x =', int(xMid/(t*inchesPerFoot)), �e�t�B�[�g/�b�f

#Page 218, Figure 15.7
vals = []
for i in range(10):
    vals.append(2**i)
pylab.plot(vals,'bo', label = �e���ۂ̓_')
xVals = pylab.arange(10)
a,b,c,d,e = pylab.polyfit(xVals, vals, 4)
yVals = a*(xVals**4) + b*(xVals**3) + c*(xVals**2)+ d*xVals + e
pylab.plot(yVals, 'bx', label = �e�\���_', markersize = 20)
pylab.title('Fitting y = 2**x')
pylab.legend()

#Page 219, additional code for Figure 15.7
pred2to20 = a*(20**4) + b*(20**3) + c*(20**2)+ d*20 + e
print �e���f���̗\���ɂ��ƁC2**20�͂����悻', round(pred2to20)
print �e2**20�̎��ۂ̒l��', 2**20

xVals, yVals = [], []
for i in range(10):
    xVals.append(i)
    yVals.append(2**i)
pylab.plot(xVals, yVals)
pylab.semilogy()

#Page 220, Figure 15.8
import math

#�C�ӂ̎w���֐����`����
def f(x):
    return 3*(2**(1.2*x))

def createExpData(f, xVals):
    """f��������1���w���֐��Ɖ��肷��
       xVals���Cf�̓K���Ȉ��������z��Ƃ���
       xVals�̗v�f�Ɋ֐�f��K�p�������ʂ�ێ�����z���Ԃ��D"""
    yVals = []
    for i in range(len(xVals)):
        yVals.append(f(xVals[i]))
    return pylab.array(xVals), pylab.array(yVals)

def fitExpData(xVals, yVals):
    """xVals��yVals���C
       yVals[i] == f(xVals[i])�ƂȂ鐔��ێ�����z��Ɖ��肷��D
       log(f(x), base) == ax + b�𖞂���a,b��Ԃ�"""
    logVals = []
    for y in yVals:
        logVals.append(math.log(y, 2.0)) #�ꂪ2�̑ΐ��𓾂�
    a,b = pylab.polyfit(xVals, logVals, 1)
    return a, b, 2.0

xVals, yVals = createExpData(f, range(10))
pylab.plot(xVals, yVals, 'ro', label = �e���ۂ̒l')
a, b, base = fitExpData(xVals, yVals)
predictedYVals = []
for x in xVals:
    predictedYVals.append(base**(a*x + b))
pylab.plot(xVals, predictedYVals, label = �e�\���l')
pylab.title(�e�w���֐���K������')
pylab.legend()
#�I���W�i���̃f�[�^�ɂ͂Ȃ�x�̒l�𒲂ׂ�
print 'f(20) =', f(20)
print 'Predicted f(20) =', base**(a*20 + b)
