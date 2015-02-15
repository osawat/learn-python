import random

#Page 252, Fig. 18.1
def fib(n):
    """nを0以上の整数とする
       n番目のフィボナッチ数を返す"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print fib(20)


#Page 254, Fig. 18.3
def fastFib(n, memo = {}):
    """nを0以上の整数とする． memoは再帰呼び出しによってのみ使われる
       n番目のフィボナッチ数を返す"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


print fastFib(250)


#Page 236, Fig. 17.2 again 
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'
        return result

#Page 257, Fig. 18.6
def maxVal(toConsider, avail):
    """toConsiderを品物のリスト, availを重さとする
       それらをパラメータとする0/1ナップサック問題の解である
       総重量と品物のリストからなるタプルを返す"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #右側の分岐のみを探索する
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #左側の分岐を探索する
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #右側の分岐を探索する
        withoutVal, withoutToTake = maxVal(toConsider[1:],
                                           avail)
        #よりよい分岐を選択
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print item
    print 'Total value of items taken =', val

smallTest()


#Page 258, Fig. 18.7
def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxWeight)))
    return items

def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print 'Items Taken'
    for item in taken:
        print item
    print 'Total value of items taken =', val

bigTest(10)


#Page 259, Fig. 18.8
def fastMaxVal(toConsider, avail, memo = {}):
    """toConsiderを品物のリスト, availを重さ，
       memoは再帰呼び出しによってのみ使われるとする
       それらをパラメータとする0/1ナップサック問題の解である
       総重量と品物のリストからなるタプルを返す"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result
item.append(Item(str(i),
                 random.randint(1, maxVal),
                 random.randint(1, maxWeight)))

item.append(Item(str(i),
                 random.randint(1, maxVal),
                 random.randint(1, maxWeight)*random.random()))
