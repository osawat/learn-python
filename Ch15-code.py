# coding: utf-8
import pylab, random
from rcParamsSettings import *

#次の2つの関数は以前の章で既に定義しており，ここで用いる．
def stdDev(X):
    """Xを数のリストと仮定する．
       Xの標準偏差を返す"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #平均との差の平方根

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
               label = '変位の観測値')
    pylab.title('バネの変位の観測値')
    pylab.xlabel('|力| (ニュートン)')
    pylab.ylabel('距離 (メートル)')


#Page 212, Figure 15.3
def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo',
               label = '変位の観測値')
    pylab.title('バネの変位の観測値')
    pylab.xlabel('|力| (ニュートン)')
    pylab.ylabel('距離 (メートル)’)
    #1次の適合曲線（直線）を求める
    a,b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a*pylab.array(forces) + b
    k = 1.0/a
    pylab.plot(forces, predictedDistances,
               label = '変位の線形適合による予測値, k = '
               + str(round(k, 5)))
    pylab.legend(loc = 'best')
##    pylab.plot(forces, predictedDistances,
##               label = 'Displacements predicted by\nlinear fit, k = '
##               + str(round(k,5)))

#Page 212, additional code for fitData in Fig. 15.3
#3次の適合曲線を求める
a,b,c,d = pylab.polyfit(forces, distances, 3)
predictedDistances = a*(forces**3) + b*forces**2 + c*forces + d
pylab.plot(forces, predictedDistances, 'b:', label = '3次の適合')

#Page 213, 図15.3のfitDataを修正したもの
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
    #各距離における平均高さをもつ配列を得る
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    meanHeights = totHeights/len(heights)
    pylab.title('発射物の軌跡 ('                + str(numTrials) + ' 回の試行の平均値)’)
    pylab.xlabel('発射からのインチ数')
    pylab.ylabel('発射からの高さ（インチ）')
    pylab.plot(distances, meanHeights, 'bo')
    a,b = pylab.polyfit(distances, meanHeights, 1)
    altitudes = a*distances + b
    pylab.plot(distances, altitudes, 'b', label = '線形適合')
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) +  b*distances + c
    pylab.plot(distances, altitudes, 'b:', label = '2の適合')
    pylab.legend()

#Page 216, Figure 15.5
def rSquared(measured, predicted):
    """measuredは観測値を保持する1次元の配列
       predictedは予測値を保持する1次元の配列と仮定する
       決定変数を返す"""
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/float(len(measured))
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability

#Page 218, Figure 15.6
def getHorizontalSpeed(a, b, c, minX, maxX):
    """minXとmaxXをインチ単位の距離と仮定する．
       水平方向の速度を返す（単位はフィート/秒）．"""
    inchesPerFoot = 12.0
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*inchesPerFoot #重力加速度（インチ/秒/秒）
    t = (2*yPeak/g)**0.5
    print '水平方向の速度 =', int(xMid/(t*inchesPerFoot)), 'フィート/秒’

#Page 218, Figure 15.7
vals = []
for i in range(10):
    vals.append(2**i)
pylab.plot(vals,'bo', label = '実際の点')
xVals = pylab.arange(10)
a,b,c,d,e = pylab.polyfit(xVals, vals, 4)
yVals = a*(xVals**4) + b*(xVals**3) + c*(xVals**2)+ d*xVals + e
pylab.plot(yVals, 'bx', label = '予測点', markersize = 20)
pylab.title('Fitting y = 2**x')
pylab.legend()

#Page 219, additional code for Figure 15.7
pred2to20 = a*(20**4) + b*(20**3) + c*(20**2)+ d*20 + e
print 'モデルの予測によると，2**20はおおよそ', round(pred2to20)
print '2**20の実際の値は', 2**20

xVals, yVals = [], []
for i in range(10):
    xVals.append(i)
    yVals.append(2**i)
pylab.plot(xVals, yVals)
pylab.semilogy()

#Page 220, Figure 15.8
import math

#任意の指数関数を定義する
def f(x):
    return 3*(2**(1.2*x))

def createExpData(f, xVals):
    """fを引数を1つもつ指数関数と仮定する
       xValsを，fの適当な引数をもつ配列とする
       xValsの要素に関数fを適用した結果を保持する配列を返す．"""
    yVals = []
    for i in range(len(xVals)):
        yVals.append(f(xVals[i]))
    return pylab.array(xVals), pylab.array(yVals)

def fitExpData(xVals, yVals):
    """xValsとyValsを，
       yVals[i] == f(xVals[i])となる数を保持する配列と仮定する．
       log(f(x), base) == ax + bを満たすa,bを返す"""
    logVals = []
    for y in yVals:
        logVals.append(math.log(y, 2.0)) #底が2の対数を得る
    a,b = pylab.polyfit(xVals, logVals, 1)
    return a, b, 2.0

xVals, yVals = createExpData(f, range(10))
pylab.plot(xVals, yVals, 'ro', label = '実際の値')
a, b, base = fitExpData(xVals, yVals)
predictedYVals = []
for x in xVals:
    predictedYVals.append(base**(a*x + b))
pylab.plot(xVals, predictedYVals, label = '予測値')
pylab.title('指数関数を適合する')
pylab.legend()
#オリジナルのデータにはないxの値を調べる
print 'f(20) =', f(20)
print 'Predicted f(20) =', base**(a*20 + b)
