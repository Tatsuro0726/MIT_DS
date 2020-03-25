# -*- coding: utf-8 -*-
# # Sample
# class IntSet(object):
#     """IntSetは整数の集合（Set）である"""
#     #ここに実装に関する情報を記述（抽象化の情報ではない）
#     #集合は,int型の要素からなるリストself.valsによって表される
#     #int型の要素はそれぞれ、リストself.valsにちょうど一度だけ現れる

#     # コンストラクタ
#     def __init__(self):
#         """整数の空集合を生成する"""
#         self.vals = []
    
#     def insert(self, e):
#         """eをint型とし、eをselfに挿入する"""
#         if not e in self.vals:
#             self.vals.append(e)
    
#     def member(self, e):
#         """eをint型とする
#            eがselfにあればTrueを、なければFalseを返す"""
#         return e in self.vals
    
#     def remove(self, e):
#         """eをint型とし、eをselfから削除する
#            eがselfになければ例外ValueErrorを発生させる"""
#         try:
#             self.vals.remove(e)
#         except:
#             return ValueError(str(e) + 'not found')
    
#     def getMembers(self):
#         """seflが含む要素を持つリストを返す
#            要素の順序に関しては何も約束できない"""
#         return self.vals[:]  # cloneを返す
    
#     def __str__(self):
#         """selfの文字列表現を返す"""
#         self.vals.sort()
#         result = ''
#         for e in self.vals:
#             result = result + str(e) + ','  # 例：A,B,C
#         return '{' + result[:-1] + '}'  # -1としたのは最後のカンマをのぞくため
# # Methodは,method attribute(メソッド属性)と呼ばれることもある

# # Instance生成
# s = IntSet()
# s.insert(3)
# s.insert(4)
# print(s)

# 8.1.2 学生と教員の情報管理のためのクラスの利用
import datetime
class Person(object):

    def __init__(self, name):
        """「人間」を生成する"""
        self.name = name
        try: # 「○○ ○○」で名前が入力される想定
            lastBlank = name.rindex(' ') # 文字列の最後から''までの長さ
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        """selfの名前(フルネーム）を返す"""
        return self.name

    def getLastName(self):
        """selfの姓を返す"""
        return self.lastName
    
    def setBirthday(self, birthdate):
        """birthdateをdatetime.date型とする
           selfの生年月日をbirthdateとする"""
        self.birthday = birthdate
    
    def getAge(self):
        """selfの現在の年齢を日単位で返す"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    # __lt__は<の比較演算子を実装
    # Object同氏の比較が可能になる。
    def __lt__(self, other):
        """selfの名前がotherの名前と比較して
           アルファベット順で前ならばTrueを、
           そうでなければFalseを返す。
           比較は、姓について行われるが
           姓が同じであれば名前（フルネーム）が比較される"""
        if self.lastName == other.lastName:
            return self.name < other.name # フルネーム比較
        return self.lastName < other.lastName
    
    def __str__(self):
        """selfの名前（フルネーム）を返す"""
        return self.name

# テストコード
# 一般的にインスタンス生成時は、該当クラスメソッド__init__の仕様をよく見ること!!!!!
# me = Person('Michael Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# # print(him.getLastName())
# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958, 8, 16))
# # print(him.getName(), 'is', him.getAge(), 'days old')

# # 比較演算子のテスト
# # オブジェクトの比較演算が必要なときは__lt(含めない)/le(以下)__,__eq/ne__,__gt(含めない)/ge(以上)__
# pList = [me, him, her]
# for p in pList:
#     print(p)
# pList.sort()  # 比較演算子<が使用できるので__lt__を用いてソートされる
# for p in pList:
#     print(p)

# 8.2 継承(inheritance)
# # Sample
# class MITPerson(Person): # Personクラスを継承

#     nextIdNum = 0  # 個人識別番号
    
#     def __init__(self, name):
#         Person.__init__(self, name)
#         self.idNum = MITPerson.nextIdNum
#         MITPerson.nextIdNum += 1

#     def getIdNum(self):
#         return self.idNum
    
#     def __lt__(self, other):
#         return self.idNum < other.idNum

#     def isStudent(self):
#         return isinstance(self, Student)


# テストコード
# p1 = MITPerson('Barbara Beaver') # MITPersonのインスタンス生成
# print(str(p1) + '\'s id number is' + str(p1.getIdNum()))  # \'はエスケープ文字

# p1 = MITPerson('Mark Guttag')
# p2 = MITPerson('Billy Bob Beaver')
# p3 = MITPerson('Billy Bob Beaver')
# p4 = Person('Billy Bob Beaver')

# print('p1 < p2 =', p1 < p2)
# print('p3 < p2 =', p3 < p2)
# print('p4 < p1 =', p4 < p1)

# error
# print('p1 < p4 =', p1 < p4) # p4はPersonクラスであり、idNum属性を持たないので比較できない

# 8.2.1 多重継承
# # Sample
# class Student(MITPerson):  # MITPersonを継承: Personクラス > MITPerson
#     pass  # スーパークラスから継承する属性以外は何も持たない宣言

# class UG(Student):  # Studentクラスを継承
#     def __init__(self, name, classYear): # __init__をオーバライド
#         MITPerson.__init__(self, name)
#         self.year = classYear
#     def getClass(self):
#         return self.year

# class Grad(Student):
#     pass  # Studentクラスからそのまま継承

# テストコード
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
# print(p5, 'is a graduate Student is', type(p5) == Grad)
# print(p5, 'is an undergraduate Student is', type(p5) == UG)

# Studentのテストコード
# print(p5, 'is a student is', p5.isStudent()) # studentクラスのインスタンスであるためTrue
# print(p6, 'is a student is', p6.isStudent()) # studentクラスのインスタンスであるためTrue
# print(p3, 'is a student is', p3.isStudent())  # MITPersonクラスのインスタンスであるためFalse

# 編入生クラス
# class TransferStudent(Student):

#     def init(self, name, fromSchool):
#         MITPerson.__init__(self, name)
#         self.fromSchool = fromSchool
    
#     def getOldSchool(self):
#         return self.fromSchool

# 8.3 カプセル化と情報隠蔽
# class Grades(object):
#     def __init__(self):
#         """空の成績ブックを生成する"""
#         self.students = []
#         self.grades = {}
#         self.isSorted = True
    
#     def addStudent(self, student):
#         """studentをStudent型とする
#            studentを成績ブックへ追加する"""
#         if student in self.students: # 事前に登録されている場合
#             raise ValueError('Duplicate student')
#         self.students.append(student)
#         self.grades[student.getIdNum()] = []
#         self.isSorted = False

#     def addGrade(self, student, grade):
#         """gradeをfloat型とする
#            gradeをstudentの成績リストへ追加する"""
#         try:
#             self.grades[student.getIdNum()].append(grade)
#         except:
#             raise ValueError('Student not in mapping')
    
#     def getGrades(self, student):
#         """studentの成績リストを返す"""
#         try:  # studentの成績リストのコピーを返す
#             return self.grades[student.getIdNum()][:]
#         except:
#             raise ValueError('Student not in mapping')

#     def getStudent(self):
#         """成績ブックに収められた学生の、ソートされたリストを返す"""
#         if not self.isSorted:  # Falseの場合
#             self.students.sort()
#             self.isSorted = True
#         return self.students[:]  # 学生のリストのコピーを返す

# # sixHundredという名前の講義に登録している学生の成績レポートを作成する関数
# def gradeReport(course):
#     """courseをGrade型とする"""
#     report = ''
#     for s in course.getStudent():
#         tot = 0.0
#         numGrade = 0
#         for g in course.getGrades(s):
#             tot += g
#             numGrade += 1
#         try:
#             average = tot / numGrade
#             report = report + '\n'\
#                         + str(s) + '\'s mean grade is ' + str(average)
#         except ZeroDivisionError:
#             report = report + '\n'\
#                         + str(s) + 'has no grades'
#     return report

# ug1 = UG('Jane Doe', 2014)
# ug2 = UG('John Doe', 2015)
# ug3 = UG('David Henry', 2003)
# g1 = Grad('Billy Buckner')
# g2 = Grad('Bucky F. Dent')
# sixHundred = Grades()  # generate an instance
# sixHundred.addStudent(ug1)
# sixHundred.addStudent(ug2)
# sixHundred.addStudent(g1)
# sixHundred.addStudent(g2)
# for s in sixHundred.getStudent():
#     sixHundred.addGrade(s, 75)
# sixHundred.addGrade(g1, 25)
# sixHundred.addGrade(g2, 100)
# sixHundred.addStudent(ug3)
# print(gradeReport(sixHundred))

# # テスト
# slist = sixHundred.getStudent()
# for s in slist:
#     print(s.getName())

# encapsulation（カプセル化）：
# データ属性とそれを操作するメソッドをまとめて扱うことを意味する
# Rafael = MITPerson('Rafael Reif)
# 以降、'.'ドットを使用してRafaelの年齢や個人番号などといった属性にアクセスできる。

# 情報隠蔽(java, c++のprivate的なもの)
# Sample 
class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsovisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'  # privateと同じ
    
    def printVisible(self):
        print(self.visible)

    def printInvisible(self):
        print(self.__invisible)
    
    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)

# 変数の隠蔽確認コード
test = infoHiding()
print(test.visible) # OK
print(test.__alsovisible__)  #OK
#print(test.__invisble)  #NG:外からアクセスできない

# メソッドの隠蔽確認コード
test.printInvisible() #OK
test.__printInvisible__() # OK
# test.__printInvisible() # NG:外からは使用できない

# subclassのとき
class subClass(infoHiding):
    def __init__(self):
        print('from subclass', self.__invisble)  # NG:infoHidingで隠蔽した__invisibleが使えない

# testSub = subClass()    # Error:サブクラスがスーパークラスで隠蔽された属性を使用するときAttribute Errorが発生
# ⇒上記がPythonにおける情報隠蔽を少しばかり厄介にしている⇒なのであまり__の命名規則は利用しない人が多い
# __を使用しないことにより、クラス定義外でインスタンス変数を生成したり、クラス変数に直接アクセスできてしまう
# 上記に注意しながらプログラムを各必要がある