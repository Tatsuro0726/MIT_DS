# -*- coding: utf-8 -*-
# 例外とアサーション

# 以下は,numFailuersが0の場合エラーが発生
# successFailureRatio = numSuccesses / numFailuers
# print('The success/failure ration is', successFailureRatio)
# print('Now here')

# try:
#     successFailureRatio = numSuccesses / numFailuers
#     print('The success/failure ration is', successFailureRatio)
# except ZeroDivisionError:
#     print('No failures, so the success/failure ration is undefined.')
# print('Now here')

# Practice:7-1
# def sumDigits(s):
#     """sを文字列とする.
#        sの中の数字の合計を返す.
#        例えば,sが'a2b3c'ならば5を返す"""
#     number = 0
#     for c in s:
#         try:
#             number += int(c)
#         except ValueError:
#             pass
#     return number

# input = input('Enter string:')
# print(sumDigits(input))

# sample
# while True:
#     val = input('Enter an intger:')
#     try:
#         val = int(val)
#         print('The square of the number you entered is', val ** 2)
#         break  # whileループから抜ける
#     except ValueError:
#         print(val, 'is not an integer')

# integerかかくにん
# def readInt():
#     while True:
#         val = input('Enter an integer:')
#         try:
#             return (int(val))
#         except ValueError:
#             print(val,'is not an integer')

# def readVal(valType, requestMsg, errorMsg):
#     while True:
#         val = input(requestMsg + '')
#         try:
#             return (valType(val))  # 値を返す前に文字型をvalType型に変換する
#         except ValueError:
#             print(val, errorMsg)

# readVal(int, 'Enter an integer:', 'is not an integer')

# 2種類以上の例外を引き起こす可能性がある場合
# 以下のようにtupleでくくる
# except (ValueError, TypeError) :

# どんな例外でも拾うときは
# except:

# 7.2 フロー制御機構としての例外
# Practice

# def findAnEven(L):
#     """Lをint型の要素を持つリストとする
#        Lに最初に現れる偶数を返す
#        Lが偶数を含まなければValueErrorを引き起こす"""
#     for e in L:
#             if e % 2 == 0:
#                 return (e)
#     raise ValueError

# L = [1, 1, 3, 5, 7]

# print(findAnEven(L))

# # 参考の回答
# def findAnEven(l):
#     """lをint型の要素を持つリストとする
#        lに最初に現れる偶数を返す
#        lが偶数を含まなければValueErrorを引き起こす"""
#     for x in l:
#         if x % 2 == 0:
#             return x
#     raise ValueError


# print(findAnEven([1,2,3]))
# try:
#     findAnEven([1,3,5])
# except ValueError:
#     print('ValueError')

# sample 7.1
# def getRatios(vect1, vect2):
#     """vect1とvect2を同じ長さのリストとする
#     　　vect1[i]/vect2[i]を意味する値からなるリストを返す"""
#     ratios = []
#     for index in range(len(vect1)):
#         try:
#             ratios.append(vect1[index] / vect2[index])
#         except ZeroDivisionError:                       # 最初の例外
#             ratios.append(float('nan'))  # nan = Not a number
#         except:
#             raise ValueError('getRatios called with bad arguments')
#     return ratios

# # sampleのテストスクリプト
# try:
#     print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0,0.0, 3.0]))
#     print(getRatios([], []))
#     print(getRatios([1.0, 2.0], [3.0]))
# except ValueError as msg: # 上のtryでgetRatiosから返ってきた値gが ValueError('')であれば、このexceptが評価される
#     print(msg)

# # 7.2 上記と同じ仕様であるが、try-exceptを用いずに実装
# # 上のコードに比べ長く、読みづらい
# def getRatios(vect1, vect2):
#     """vect1とvect2を同じ長さのリストとする
#    　　vect1[i]/vect2[i]を意味する値からなるリストを返す"""
#     ratios = []
#     if len(vect1) != len(vect2):
#        raise ValueError('getRatios called with bad arguments')
#     for index in range(len(vect1)):
#         vect1Elem = vect1[index]
#         vect2Elem = vect2[index]
#         if (type(vect1Elem) not in (int, float))\
#             or (type(vect2Elem) not in (int, float)):
#             raise ValueError('getRatios called with bad arguments')
#         if vect2Elem == 0.0:
#             ratios.append(float('NaN'))  # Nan = Not a number
#         else:
#             ratios.append(vect1Elem / vect2Elem)
#     return ratios

# def getGrades(fname):
#     try:
#         gradesFile = open(fname, 'r')  # 読み込み用にファイルを開く
#     except IOError:
#         raise ValueError('getGrades could not open' + fname)
#     grades = []
#     for line in gradesFile:
#         try:
#             grades.append(float(line))
#         except:
#             raise ValueError('Unable to convert line to float')
#     return grades


# # テストスクリプト
# try:
#     grades = getGrades('quiz1grades.txt')
#     grades.sort()
#     median = grades[len(grades) // 2]
#     print('median grade is', median)
# except ValueError as errorMsg:
#     print('Whoops.', errorMsg)

# assertのテストスクリプト
# try:
#     kitai = 100
#     input = 1
#     assert kitai == input, '期待する値[{0}],入力値[{1}],テスト{2}'.format(kitai, input,100)
# except AssertionError as error:
#     print('AssertionError:', error)

# memo
# '{NUM}.format('',NUM,・・・)　formatのindexが{}に代入される
print('{0},{1},{2},{3},{4}'.format(0,1,2,3,4))