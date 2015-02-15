import pylab, random, string, copy

#Page 267, Figure 19.2
def minkowskiDist(v1, v2, p):
    """v1とv2は長さの等しい数値配列であるとする
       v1とv2の，p次のミンコウスキ距離を返す"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1.0/p)

#Page 267, Figure 19.3
class Animal(object):
    def __init__(self, name, features):
        """nameは文字列; featuresは数値のリストとする"""
        self.name = name
        self.features = pylab.array(features)
        
    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.features
    
    def distance(self, other):
        """otherはAnimalオブジェクトとする
           自分自身とother間のユークリッド距離を返す"""
        return minkowskiDist(self.getFeatures(),
                             other.getFeatures(), 2)

#Page 268, Figure 19.4
def compareAnimals(animals, precision):
    """animalsはAnimalオブジェクトのリスト, precisionは非負の整数とする
       それぞれのAnimal間のユークリッド距離の表を作る"""
    #行と列のラベルを得る
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #Animal間の距離を得る
    #行について
    for a1 in animals:
        row = []
        #列について
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #表を作る
    table = pylab.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))
    table.scale(1, 2.5)
    pylab.axis('off') #x軸とy軸を表示しない
    pylab.savefig('distances')
    pylab.show()

#Page 269
rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa\nconstrictor', [0,1,0,1,0])
dartFrog = Animal('dart frog', [1,0,1,0,4])
animals = [rattlesnake, boa, dartFrog]
compareAnimals(animals, 3)

#Page 272, Figure 19.5
class Example(object):
    
    def __init__(self, name, features, label = None):
        #featuresは数の配列である
        self.name = name
        self.features = features
        self.label = label
        
    def dimensionality(self):
        return len(self.features)
    
    def getFeatures(self):
        return self.features[:]
    
    def getLabel(self):
        return self.label
    
    def getName(self):
        return self.name
    
    def distance(self, other):
        return minkowskiDist(self.features, other.getFeatures(), 2)
    
    def __str__(self):
        return self.name +':'+ str(self.features) + ':' \
               +str(self.label)

#Page 273, Figure 19.6
class Cluster(object):
    
    def __init__(self, examples, exampleType):
        """examplesはexampleType型のリストとする"""
        self.examples = examples
        self.exampleType = exampleType
        self.centroid = self.computeCentroid()
        
    def update(self, examples):
        """クラスターのexamplesを新しい標本examplesで置き換える
           クラスターの重心が何回変更されたかを返す"""
        oldCentroid = self.centroid
        self.examples = examples
        if len(examples) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
        
    def members(self):
        for e in self.examples:
            yield e
        
    def size(self):
        return len(self.examples)
    
    def getCentroid(self):
        return self.centroid
    
    def computeCentroid(self):
        dim = self.examples[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for e in self.examples:
            totVals += e.getFeatures()
        centroid = self.exampleType('centroid',
                              totVals/float(len(self.examples)))
        return centroid
    
    def variance(self):
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist**0.5
    
    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
                 + str(self.centroid.getFeatures()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]

#Page 275, Figure 19.7
def kmeans(examples, exampleType, k, verbose):
    """examplesはexmapleType型の標本リストであり，
       kは正の整数，verboseはブール型とする
       k個のクラスターからなるリストを返す．もしverboseの値が
       Trueならば，k-平均法の各繰り返しの途中結果を出力する      
    """
    #k個の初期中心をランダムに選ぶ
    initialCentroids = random.sample(examples, k)
    
    #それぞれの中心ただ一つからなるクラスターを作成する
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e], exampleType))
        
    #中心が変化しなくなるまで繰り返す
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #k個の空のリストからなるリストを作成する
        newClusters = []
        for i in range(k):
            newClusters.append([])

        #それぞれのサンプルを最も近い中心へと関連づける
        for e in examples:
            #eに最も近い中心を見つける
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #eを適切なクラスターの標本リストへ加える
            newClusters[index].append(e)
            
        #それぞれのクラスターを更新する; 中心が変化したかどうかをチェック
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print 'Iteration #' + str(numIterations)
            for c in clusters:
                print c
            print '' #空行を追加する
    return clusters

#Page 276, Figure 19.8
def dissimilarity(clusters):
    totDist = 0.0
    for c in clusters:
        totDist += c.variance()
    return totDist
    
def trykmeans(examples, exampleType, numClusters, numTrials,
              verbose = False):
    """kmeans関数をnumTrials回呼び出しそして，
       最も類似性が小さいクラスタリングを返す"""
    best = kmeans(examples, exampleType, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    for trial in range(1, numTrials):
        clusters = kmeans(examples, exampleType, numClusters, verbose)
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
    return best

#Page 277, Figure 19.9
def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(Example(namePrefix+str(s), [x, y]))
    return samples

def plotSamples(samples, marker):
    xVals, yVals = [], []
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(), xy = (x, y),
                       xytext = (x+0.13, y-0.07),
                       fontsize = 'x-large')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals, yVals, marker)

def contrivedTest(numTrials, k, verbose):
    random.seed(0)
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 10
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, '1.')
    plotSamples(d1Samples, 'b^')
    d2Samples = genDistribution(xMean+3, xSD, yMean+1, ySD, n, '2.')
    plotSamples(d2Samples, 'ro')
    clusters = trykmeans(d1Samples + d2Samples, Example, k,
                         numTrials, verbose)
    print 'Final result'
    for c in clusters:
        print '', c
    pylab.show()
    
contrivedTest(1, 2, True)


#Page 279, Figure 19.11
def contrivedTest2(numTrials, k, verbose):
    random.seed(0)
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 8
    d1Samples = genDistribution(xMean,xSD, yMean, ySD, n, '1.')
    plotSamples(d1Samples, 'b^')
    d2Samples = genDistribution(xMean+3,xSD,yMean, ySD, n, '2.')
    plotSamples(d2Samples, 'ro')
    d3Samples = genDistribution(xMean, xSD, yMean+3, ySD, n, '3.')
    plotSamples(d3Samples, 'gd')
    clusters = trykmeans(d1Samples + d2Samples + d3Samples,
                         Example, k, numTrials, verbose)
    print 'Final result'
    for c in clusters:
        print '', c
    pylab.show()

contrivedTest2(40,  2, False)

#Page 282, Figure 19.12
def readMammalData(fName):
    dataFile = open(fName, 'r')
    numFeatures = 0
    #ファイルの先頭の処理
    for line in dataFile: #特徴の数を調べる
        if line[0:6] == '#Label': #特徴の終了を示す
            break
        if line[0:5] != '#Name':
            numFeatures += 1
    featureVals = []
    
    #featureVals, speciesNames と labelList の生成
    featureVals, speciesNames, labelList = [], [], []
    for i in range(numFeatures):
        featureVals.append([])
        
    #コメント後の行ごとの処理
    for line in dataFile:
        dataLine = string.split(line[:-1], ',') #改行の除去; その後分割
        speciesNames.append(dataLine[0])
        classLabel = float(dataLine[-1])
        labelList.append(classLabel)
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i+1]))
            
    #特徴ベクトルを含むリストを作るためにfeatureValsを使う
    #それぞれのほ乳類について
    featureVectorList = []
    for mammal in range(len(speciesNames)):
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][mammal])
        featureVectorList.append(featureVector)
    return featureVectorList, labelList, speciesNames

#Page 283, Figure 19.13
def buildMammalExamples(featureList, labelList, speciesNames):
    examples = []
    for i in range(len(speciesNames)):
        features = pylab.array(featureList[i])
        example = Example(speciesNames[i], features, labelList[i])
        examples.append(example)
    return examples

def testTeeth(numClusters, numTrials):
    features, labels, species = readMammalData('dentalFormulas.txt')
    examples = buildMammalExamples(features, labels, species)
    bestClustering =\
                   trykmeans(examples, Example, numClusters, numTrials)
    for c in bestClustering:
        names = ''
        for p in c.members():
            names += p.getName() + ', '
        print '\n', names[:-2] #後端のコンマとスペースを削除
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.getLabel() == 0:
                herbivores += 1
            elif p.getLabel() == 1:
                carnivores += 1
            else:
                omnivores += 1
        print herbivores, 'herbivores,', carnivores, 'carnivores,',\
              omnivores, 'omnivores'

testTeeth(3, 20) 

#Page 284, Figure 19.14
def scaleFeatures(vals):
    """valsは数列とする"""
    result = pylab.array(vals)
    mean = sum(result)/float(len(result))
    result = result - mean
    sd = stdDev(result)
    result = result/sd
    return result

#Page 285, Figure 19.15, augmented by code elided in book
def readMammalData(fName, scale):
    """scaleはブール型とする.
       もしTrueならば特徴ベクトルをスケーリングする"""
    dataFile = open(fName, 'r')
    numFeatures = 0
    #ファイルの先頭の処理
    for line in dataFile: #特徴の数を調べる
        if line[0:6] == '#Label': #特徴の終了を示す
            break
        if line[0:5] != '#Name':
            numFeatures += 1
    featureVals = []
    
    #featureVals, speciesNames と labelList の生成
    featureVals, speciesNames, labelList = [], [], []
    for i in range(numFeatures):
        featureVals.append([])
        
    #Continue processing lines in file, starting after comments
    for line in dataFile:
        dataLine = string.split(line[:-1], ',') #改行の除去; その後分割
        speciesNames.append(dataLine[0])
        classLabel = float(dataLine[-1])
        labelList.append(classLabel)
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i+1]))

    #特徴ベクトルを含むリストを作るためにfeatureValsを使う
    #それぞれのほ乳類について必要なら特徴ベクトルをスケーリング
    if scale:
        for i in range(numFeatures):
            featureVals[i] = scaleFeatures(featureVals[i])
    featureVectorList = []
    for mammal in range(len(speciesNames)):
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][mammal])
        featureVectorList.append(featureVector)
    return featureVectorList, labelList, speciesNames

def testTeeth(numClusters, numTrials, scale):
    features, classes, species =\
              readMammalData('dentalFormulas.txt', scale)
    examples = buildMammalExamples(features, classes, species)
    #この後のコードは前のバージョンの部分と同じ
    bestClustering =\
                   trykmeans(examples, Example, numClusters, numTrials)
    for c in bestClustering:
        names = ''
        for p in c.members():
            names += p.getName() + ', '
        print '\n', names[:-2]
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.getLabel() == 0:
                herbivores += 1
            elif p.getLabel() == 1:
                carnivores += 1
            else:
                omnivores += 1
        print herbivores, 'herbivores,', carnivores, 'carnivores,',\
              omnivores, 'omnivores'

print 'Cluster  without scaling' ,testTeeth(3, 20, False)
print '\nCluster  with scaling' ,testTeeth(3, 20, True)

