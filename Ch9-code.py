#Page 113
def f(i):
   """iをint型とし，かつi >= 0であるとする"""
   answer = 1
   while i >= 1:
      answer *= i
      i -= 1
   return answer

#Page 114
def linearSearch(L, x):
   for e in L:
      if e == x:
         return True
   return False

#Page 115
def fact(n):
   """nを自然数とする
      n!を返す"""
   answer = 1
   while n > 1:
      answer *= n
      n -= 1
   return answer

#Page 115, Figure 9.1
def squareRootExhaustive(x, epsilon):
   """xとepsilonを正のfloat型とし，かつepsilon < 1であるとする
      y*yとxの誤差がepsilon以内であるようなyを返す"""
   step = epsilon**2
   ans = 0.0
   while abs(ans**2 - x) >= epsilon and ans*ans <= x:
      ans += step
   if ans*ans > x:
      raise ValueError
   return ans

#Page 116, Figure 9.2
def squareRootBi(x, epsilon):
   """xとepsilonを正のfloat型とし，かつepsilon < 1であるとする
      y*yとxの誤差がepsilon以内であるようなyを返す"""
   low = 0.0
   high = max(1.0, x)
   ans = (high + low)/2.0
   while abs(ans**2 - x) >= epsilon:
      if ans**2 < x:
         low = ans
      else:
         high = ans
      ans = (high + low)/2.0
   return ans

#Page 116
def f(x):
   """xを正のint型とする"""
   ans = 0
   #定数時間を要するループ
   for i in range(1000):
      ans += 1
   print 'Number of additions so far', ans
   #xの時間を要するループ
   for i in range(x):
      ans += 1
   print 'Number of additions so far', ans
   #x**2の時間を要する入れ子ループ
   for i in range(x):
      for j in range(x):
         ans += 1
         ans += 1
   print 'Number of additions so far', ans
   return ans

#Page 119
def intToStr(i):
   """iを非負のint型とする
      iの値を10進数で表す文字列を返す"""
   digits = '0123456789'
   if i == 0:
      return '0'
   result = ''
   while i > 0:
      result = digits[i%10] + result
      i = i//10
   return result

def addDigits(n):
   """nを非負のint型とする
      nの値を10進数で表したときの各桁の数字の和を返す"""
   stringRep = intToStr(n)
   val = 0
   for c in stringRep:
      val += int(c)
   return val

def addDigits(s):
   """sを文字列とし，かつ各文字が10進数の数字であるとする
      sの各数字の和を整数として返す"""
   val = 0
   for c in s:
      val += int(c)
   return val

#Page 120
def factorial(x):
   """xを正のint型とする
      x!を返す"""
   if x == 1:
      return 1
   else:
      return x*factorial(x-1)

#Page 121, Figure 9.3
def isSubset(L1, L2):
   """L1とL2をリストとする
      L1の各要素がL2にもあればTrueを，
      そうでなければFalseを返す"""
   for e1 in L1:
      matched = False
      for e2 in L2:
         if e1 == e2:
            matched = True
            break
      if not matched:
         return False
   return True

#Page 121, Figure 9.4
def intersect(L1, L2):
   """L1とL2をリストとする
      L1とL2の共通部分からなるリストを返す"""
   #共通の要素からなるリストを構築する
   tmp = []
   for e1 in L1:
      for e2 in L2:
         if e1 == e2:
            tmp.append(e1)
   #重複のないリストを構築する
   result = []
   for e in tmp:
      if e not in result:
         result.append(e)
   return result

#Page 122, Figure 9.5
def getBinaryRep(n, numDigits):
   """nとnumDigitsを非負のint型とする
      nの値を，numDigits桁の2進数で表す文字列を返す"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > numDigits:
      raise ValueError('not enough digits')
   for i in range(numDigits - len(result)):
      result = '0' + result
   return result

def genPowerset(L):
   """Lをリストとする
      Lの要素の，すべての可能な組合せからなるリストを返す
      例えばLが[1, 2]ならば，
      [], [1], [2], [1,2] を要素にもつリストを返す"""
   powerset = []
   for i in range(0, 2**len(L)):
      binStr = getBinaryRep(i, len(L))
      subset = []
      for j in range(len(L)):
         if binStr[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset
