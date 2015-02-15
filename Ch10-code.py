#Page 126
def search(L, e):
   """Lをリストとする
      eがLにあればTrueを，そうでなければFalseを返す"""

def search(L, e):
   for i in range(len(L)):
      if L[i] == e:
         return True
   return False

#Page 128
def search(L, e):
   """Lを，要素が昇順で並んだリストとする
      eがLにあればTrueを，そうでなければFalseを返す"""
   for i in range(len(L)):
      if L[i] == e:
         return True
      if L[i] > e:
         return False
   return False

#Page 129, Figure 10.2
def search(L, e):
   """Lを，要素が昇順で並んだリストとする
      eがLにあればTrueを，そうでなければFalseを返す"""

   def bSearch(L, e, low, high):
      #high - lowを減少させる
      if high == low:
         return L[low] == e
      mid = (low + high)//2
      if L[mid] == e:
         return True
      elif L[mid] > e:
         if low == mid: #探索対象は残っていない
            return False
         else:
            return bSearch(L, e, low, mid - 1)
      else:
         return bSearch(L, e, mid + 1, high)

   if len(L) == 0:
      return False
   else:
      return bSearch(L, e, 0, len(L) - 1)

#Page 132, Figure 10.3
def selSort(L):
   """Lを，>を用いて比較できる要素からなるリストとする
      Lを昇順にソートする"""
   suffixStart = 0
   while suffixStart != len(L):
      #サフィックスの各要素を見る
      for i in range(suffixStart, len(L)):
         if L[i] < L[suffixStart]:
            #要素の位置を入れ替える
            L[suffixStart], L[i] = L[i], L[suffixStart]
      suffixStart += 1

#Page 134, Figure 10.4
def merge(left, right, compare):
   """leftとrightをソート済みのリストとし，
      compareを要素間の順序を定義する関数とする
      (left + right)と同じ要素からなり，
      compareに従いソートされた新たなリストを返す"""

   result = []
   i,j = 0, 0
   while i < len(left) and j < len(right):
      if compare(left[i], right[j]):
         result.append(left[i])
         i += 1
      else:
         result.append(right[j])
         j += 1
   while (i < len(left)):
      result.append(left[i])
      i += 1
   while (j < len(right)):
      result.append(right[j])
      j += 1
   return result

import operator

def mergeSort(L, compare = operator.lt):
   """Lをリストとし，
      compareをLの要素間の順序を定義する関数とする
      Lと同じ要素からなり，ソートされた新たなリストを返す"""
   if len(L) < 2:
      return L[:]
   else:
      middle = len(L)//2
      left = mergeSort(L[:middle], compare)
      right = mergeSort(L[middle:], compare)
      return merge(left, right, compare)

#Page 135, Figure 10.5
def lastNameFirstName(name1, name2):
   import string
   name1 = string.split(name1, ' ')
   name2 = string.split(name2, ' ')
   if name1[1] != name2[1]:
      return name1[1] < name2[1]
   else: #姓が同じであれば，名によりソート
      return name1[0] < name2[0]

def firstNameLastName(name1, name2):
   import string
   name1 = string.split(name1, ' ')
   name2 = string.split(name2, ' ')
   if name1[0] != name2[0]:
      return name1[0] < name2[0]
   else: #名が同じであれば，姓によりソート
      return name1[1] < name2[1]

L = ['Chris Terman', 'Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, lastNameFirstName)
print 'Sorted by last name =', newL
newL = mergeSort(L, firstNameLastName)
print 'Sorted by first name =', newL

#Page 136
L = [3,5,2]
D = {'a':12, 'c':5, 'b':'dog'}
print sorted(L)
print L
L.sort()
print L
print sorted(D)
D.sort()

L = [[1,2,3], (3,2,1,0), 'abc']
print sorted(L, key = len, reverse = True)

#Page 139, Figure 10.6
class intDict(object):
   """整数をキーとする辞書"""

   def __init__(self, numBuckets):
      """空の辞書を生成する"""
      self.buckets = []
      self.numBuckets = numBuckets
      for i in range(numBuckets):
         self.buckets.append([])

   def addEntry(self, dictKey, dictVal):
      """dictKeyをint型とし，エントリを追加する"""
      hashBucket = self.buckets[dictKey%self.numBuckets]
      for i in range(len(hashBucket)):
         if hashBucket[i][0] == dictKey:
            hashBucket[i] = (dictKey, dictVal)
            return
      hashBucket.append((dictKey, dictVal))

   def getValue(self, dictKey):
      """dictKeyをint型とする
         キーdictKeyに関連付けられたエントリを返す"""
      hashBucket = self.buckets[dictKey%self.numBuckets]
      for e in hashBucket:
         if e[0] == dictKey:
            return e[1]
      return None

   def __str__(self):
      result = '{'
      for b in self.buckets:
         for e in b:
            result = result + str(e[0]) + ':' + str(e[1]) + ','
      return result[:-1] + '}' #result[:-1]により最後のカンマを省く
 
#Page 139
import random #標準ライブラリモジュール

D = intDict(29)
for i in range(20):
   #0から10**5までの整数をランダムに選ぶ
   key = random.randint(0, 10**5)
   D.addEntry(key, i)
print 'The value of the intDict is:'
print D
print '\n', 'The buckets are:'
for hashBucket in D.buckets: #抽象化の壁を侵す
   print '  ', hashBucket
