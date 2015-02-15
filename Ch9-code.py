#Page 113
def f(i):
   """i��int�^�Ƃ��C����i >= 0�ł���Ƃ���"""
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
   """n�����R���Ƃ���
      n!��Ԃ�"""
   answer = 1
   while n > 1:
      answer *= n
      n -= 1
   return answer

#Page 115, Figure 9.1
def squareRootExhaustive(x, epsilon):
   """x��epsilon�𐳂�float�^�Ƃ��C����epsilon < 1�ł���Ƃ���
      y*y��x�̌덷��epsilon�ȓ��ł���悤��y��Ԃ�"""
   step = epsilon**2
   ans = 0.0
   while abs(ans**2 - x) >= epsilon and ans*ans <= x:
      ans += step
   if ans*ans > x:
      raise ValueError
   return ans

#Page 116, Figure 9.2
def squareRootBi(x, epsilon):
   """x��epsilon�𐳂�float�^�Ƃ��C����epsilon < 1�ł���Ƃ���
      y*y��x�̌덷��epsilon�ȓ��ł���悤��y��Ԃ�"""
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
   """x�𐳂�int�^�Ƃ���"""
   ans = 0
   #�萔���Ԃ�v���郋�[�v
   for i in range(1000):
      ans += 1
   print 'Number of additions so far', ans
   #x�̎��Ԃ�v���郋�[�v
   for i in range(x):
      ans += 1
   print 'Number of additions so far', ans
   #x**2�̎��Ԃ�v�������q���[�v
   for i in range(x):
      for j in range(x):
         ans += 1
         ans += 1
   print 'Number of additions so far', ans
   return ans

#Page 119
def intToStr(i):
   """i��񕉂�int�^�Ƃ���
      i�̒l��10�i���ŕ\���������Ԃ�"""
   digits = '0123456789'
   if i == 0:
      return '0'
   result = ''
   while i > 0:
      result = digits[i%10] + result
      i = i//10
   return result

def addDigits(n):
   """n��񕉂�int�^�Ƃ���
      n�̒l��10�i���ŕ\�����Ƃ��̊e���̐����̘a��Ԃ�"""
   stringRep = intToStr(n)
   val = 0
   for c in stringRep:
      val += int(c)
   return val

def addDigits(s):
   """s�𕶎���Ƃ��C���e������10�i���̐����ł���Ƃ���
      s�̊e�����̘a�𐮐��Ƃ��ĕԂ�"""
   val = 0
   for c in s:
      val += int(c)
   return val

#Page 120
def factorial(x):
   """x�𐳂�int�^�Ƃ���
      x!��Ԃ�"""
   if x == 1:
      return 1
   else:
      return x*factorial(x-1)

#Page 121, Figure 9.3
def isSubset(L1, L2):
   """L1��L2�����X�g�Ƃ���
      L1�̊e�v�f��L2�ɂ������True���C
      �����łȂ����False��Ԃ�"""
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
   """L1��L2�����X�g�Ƃ���
      L1��L2�̋��ʕ�������Ȃ郊�X�g��Ԃ�"""
   #���ʂ̗v�f����Ȃ郊�X�g���\�z����
   tmp = []
   for e1 in L1:
      for e2 in L2:
         if e1 == e2:
            tmp.append(e1)
   #�d���̂Ȃ����X�g���\�z����
   result = []
   for e in tmp:
      if e not in result:
         result.append(e)
   return result

#Page 122, Figure 9.5
def getBinaryRep(n, numDigits):
   """n��numDigits��񕉂�int�^�Ƃ���
      n�̒l���CnumDigits����2�i���ŕ\���������Ԃ�"""
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
   """L�����X�g�Ƃ���
      L�̗v�f�́C���ׂẲ\�ȑg��������Ȃ郊�X�g��Ԃ�
      �Ⴆ��L��[1, 2]�Ȃ�΁C
      [], [1], [2], [1,2] ��v�f�ɂ����X�g��Ԃ�"""
   powerset = []
   for i in range(0, 2**len(L)):
      binStr = getBinaryRep(i, len(L))
      subset = []
      for j in range(len(L)):
         if binStr[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset
