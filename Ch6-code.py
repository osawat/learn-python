#Page 73
def copy(L1, L2):
    """L1とL2をリストとする
       L2をL1のコピーに更新する"""	
    while len(L2) > 0: #L2から全ての要素を削除する
        L2.pop() #L2の最後の要素を削除
    for e in L1: #空リストに初期化したL2にL1の要素を追加
        L2.append(e)

def isPrime(x):
    """xを非負のint型とする
       xが素数ならばTrueを, そうでなければFalseを返す"""
    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

#Page 74
def abs(x):
    """xをint型とする
       x>=0ならばxを, そうでなければ-xを返す""" 
    if x < -1:
        return -x
    else:
        return x

#Page 79, Figure 6.1
def isPal(x):
    """xをリストとする
       そのリストが回文ならばTrueを，そうでなければFalseを返す"""
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """nを正のint型とする
       ユーザからn個の入力を受ける
       もし入力文字列が回文であれば'Yes'を，
       そうでなければ'No'を出力する"""
    for i in range(n):
        result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print 'Yes'
    else:
        print 'No'

#Page 80
def silly(n):
    """nを正のint型とする
       ユーザからn個の入力を受ける
       もし入力文字列が回文であれば'Yes'を，
       そうでなければ'No'を出力する"""
    result = []
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
    print result
    if isPal(result):
        print 'Yes'
    else:
        print 'No'

#Page 81
def isPal(x):
    """xをリストとする
       そのリストが回文ならばTrueを，そうでなければFalseを返す"""

    temp = x[:]
    temp.reverse()
    if temp == x:
        return True
    else:
        return False
