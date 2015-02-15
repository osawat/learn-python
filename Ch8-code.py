#Page 92
print type(IntSet), type(IntSet.insert)	

#Page 93, Figure 8.1
class IntSet(object):
    """intSet�͐����̏W���ł���"""
    #�����Ɏ����Ɋւ�����������i���ۉ��̏��ł͂Ȃ��j�D
    #�W���́Cint�^�̗v�f����Ȃ郊�X�gself.vals�ɂ���ĕ\�킳���D
    #int�^�̗v�f�͂��ꂼ��C���X�gself.vals�ɂ��傤��1�x���������D

    def __init__(self):
        """�����̋�W���𐶐�����"""
        self.vals = []

    def insert(self, e):
        """e��int�^�Ƃ��Ce��self�ɑ}������"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """e��int�^�Ƃ���
           e��self�ɂ����True���C�Ȃ����False��Ԃ�"""
        return e in self.vals

    def remove(self, e):
        """e��int�^�Ƃ��Ce��self����폜����
           e��self�ɂȂ���Η�OValueError�𔭐�������"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        """self���܂ޗv�f�������X�g��Ԃ�
           �v�f�̏����Ɋւ��Ă͉����񑩂ł��Ȃ�"""
        return self.vals[:]

    def __str__(self):
        """self�̕�����\����Ԃ�"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' #-1�Ƃ����͍̂Ō�̃J���}����������

#Page 94
s = IntSet()

s = IntSet()
s.insert(3)
print s.member(3)

#Page 95
s = IntSet()
s.insert(3)
s.insert(4)
print s

#Page 97, Figure 8.2
import datetime

class Person(object):

    def __init__(self, name):
        """�u�l�ԁv�𐶐�����"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """self�̖��O�i�t���l�[���j��Ԃ�"""
        return self.name

    def getLastName(self):
        """self�̐���Ԃ�"""
        return self.lastName

    def setBirthday(self, birthdate):
        """birthdate��datetime.date�^�Ƃ���
           self�̐��N������birthdate�Ɛݒ肷��"""
        self.birthday = birthdate

    def getAge(self):
        """self�̌��݂̔N�����P�ʂŕԂ�"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """self�̖��O��other�̖��O�Ɣ�ׂĎ������őO�Ȃ��True���C
           �����łȂ����False��Ԃ�"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """self�̖��O�i�t���l�[���j��Ԃ�"""
        return self.name

#Page 97
me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print him.getLastName()
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print him.getName(), 'is', him.getAge(), 'days old'

#Page 98
pList = [me, him, her]
for p in pList:
    print p
pList.sort()
for p in pList:
    print p

#Page 99, Figure 8.3
class MITPerson(Person):

    nextIdNum = 0 #�l���ʔԍ�

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

#Page 100
p1 = MITPerson('Barbara Beaver')
print str(p1) + '\'s id number is ' + str(p1.getIdNum())

p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print 'p1 < p2 =', p1 < p2
print 'p3 < p2 =', p3 < p2
print 'p4 < p1 =', p4 < p1

print 'p1 < p4  =', p1 < p4

#Page 101, Figure 8.4
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

#Page 101
p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print p5, 'is a graduate student is', type(p5) == Grad
print p5, 'is an undergraduate student is', type(p5) == UG

def isStudent(self):
    return isinstance(self, Student)

#Page 102
print p5, 'is a student is', p5.isStudent()
print p6, 'is a student is', p6.isStudent()
print p3, 'is a student is', p3.isStudent()

def isStudent(self):
    return type(self) == Grad or type(self) == UG

class TransferStudent(Student):

    def init(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool

#Page 103, Figure 8.5
class Grades(object):
    """�w�����琬�у��X�g�ւ̎ʑ�"""
    def __init__(self):
        """��̐��уu�b�N�𐶐�����"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """student��Student�^�Ƃ���
           student�𐬐уu�b�N�֒ǉ�����"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """grade��float�^�Ƃ���
           grade��student�̐��у��X�g�֒ǉ�����"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """student�̐��у��X�g��Ԃ�"""
        try: #student�̐��у��X�g�̃R�s�[��Ԃ�
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """���уu�b�N�Ɏ��߂�ꂽ�w���̃��X�g��Ԃ�"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #�w���̃��X�g�̃R�s�[��Ԃ�

#Page 104
allStudents = course1.getStudents()
allStudents.extend(course2.getStudents())

#Page 105, Figure 8.6
def gradeReport(course):
    """course��Grades�^�Ƃ���"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n'\
                     + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                     + str(s) + ' has no grades'
    return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print gradeReport(sixHundred)

#Page 105
Rafael = MITPerson()

#Page 107, Figure 8.7
def getStudents(self):
    """���уu�b�N�Ɏ��߂�ꂽ�w���̃��X�g���C��x��1�v�f���Ԃ�"""
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s

#Page 107
book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print s

for s in course.getStudents():

#Page 109, Figure 8.8
def findPayment(loan, r, m):
    """loan��r��float�^�Ƃ��Cm��int�^�Ƃ���
       ������̋�����r�Ƃ��āC�ؓ��zloan�̏Z��[����
       m�����ŕԍς���ꍇ�́C�����̕ԍϊz��Ԃ�"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """�قȂ��ނ̏Z��[�����\�z���邽�߂̒��ۃN���X"""
    def __init__(self, loan, annRate, months):
        """�V���ɏZ��[���𐶐�����"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #description of mortgage
    def makePayment(self):
        """�ԍς��s��"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    def getTotalPaid(self):
        """����܂łɎx���������z��Ԃ�"""
        return sum(self.paid)
    def __str__(self):
        return self.legend

#Page 110, Figure 8.9
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + '%, '\
                      + str(pts) + ' points'

#Page 111, Figure 8.10
class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100)\
                      + '% for ' + str(self.teaserMonths)\
                      + ' months, then ' + str(r*100) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate,
                                       self.months - self.teaserMonths)
        Mortgage.makePayment(self)

#Page 111, Figure 8.11
def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print m
        print ' Total payments = $' + str(int(m.getTotalPaid()))

compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05, varRate1=0.045,
                 varRate2=0.095, varMonths=48)
