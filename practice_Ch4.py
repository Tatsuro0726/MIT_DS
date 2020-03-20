# -*- coding: utf-8 -*-

# # practice:4-1 p41

# def isIn(str1, str2):
#         return str2 in str1

# input1 = input('Enter strings :')
# input2 = input('ENter search strings :')

# print(isIn(input1,input2))

# # Sample
# # Keyword argument
# # exp. 名前を表示する関数
# def printName(firstName, lastName, reverse=False): # reverse=False：デフォルトでFalseが設定される
#     if reverse:
#         print(lastName + ',' + firstName)
#     else:
#         print(firstName, lastName)

# printName('Olga', 'Puchmajerova', False)
# printName('Olga', 'Puchmajerova', reverse=False)
# #printName('Olga', lastName= 'Puchmajerova', False) # keyword引数の後に、keyword引数出ないものを書くとエラー
# printName(lastName='Puchmajerova',firstName='Olga',reverse=False)

# #4.1.3
# #scope
# # example
# def f(x):
#     y = 1
#     x = x + y
#     print('x =', x)
#     return x

# x = 3
# y = 2
# z = f(x)
# print('z =', z)
# print('x =', x)
# print('y =', y)

# # 4.2 仕様(Specification)
# # example:平方根の近似値を探索 bisection method
# def findRoot(x, power, epsilon):
#     """x と epsilon >0は整数もしくは浮動小数点, power>=1を整数と仮定
#        y**powerがxのepsilon以内になるような浮動小数点yを返す
#        もし、そのような浮動小数点数が存在しなければNoneを返す"""
#     if x < 0 and power % 2 == 0:  # 負の数は平方根を持たない
#         return None
#     low = min(-1.0, x)
#     high = max(1.0, x)
#     ans = (high + low) / 2
#     while abs(ans ** power - x) >= epsilon:
#         if (ans ** power < x):
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2
#     return ans

# # findRoot関数のテスト用
# def testFindRoot():
#     epsilon = 0.0001
#     for x in (0.25, -0.25, 2, 8, -8):
#         for power in range(1,4):
#             print('Testing x=', str(x), 'and power = ', power)
#             result = findRoot(x, power, epsilon)
#             if result == None:
#                 print('No root')
#             else:
#                 print(' ', result ** power, '~=', x)

# testFindRoot()

# # 階乗の実装（繰り返しと再帰）
# # 以下、繰り返しloop
# def factl(n):
#     """n > 0を整数と仮定
#        n!を返す"""
#     result = 1
#     while n > 1:
#         result = result * n
#         n -= 1
#     return result

# # 以下、再帰（recursive）
# def factR(n):
#     """n > 0を整数と仮定
#        n!を返す """
#     if n == 1:
#         return n
#     else:
#         return n * factR(n - 1)

# input_n = input('Enter an intger:')
# print(input_n,'の階乗は',str(factR(int(input_n))),'です')

# 4.3.1
# Fibonacci sequence
# def fib(n):
#     """ n > 0 を整数と仮定
#         n 番目のフィボナッチ数を返す"""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# def testFib(n):
#     for i in range(n + 1):
#         print('fib of', i, '=', fib(i))

# testFib(5)

# 出力結果：3回
# fib(5)
# = fib(4) + fib(3)
# = (fib(3) + fib(2)) + (fib(2) + fib(1))
# = ((fib(2) + fib(1)) + fib(2)) + (fib(2) + fib(1))

# # 4.3.2
# # 回文(palindrome)
# def isPalindrome(s):
#     """s を文字列と仮定
#        s が回文ならTrueを返し、それ以外ならFalseを返す
#        ただし、句読点、空白、大文字/小文字は無視する"""
    
#     def toChars(s): # 全ての文字を小文字に変換し、文字でないものを無視
#         s = s.lower()
#         letters = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 letters = letters + c
#         return letters
    
#     def isPal(s):
#         print(' isPal called with', s)
#         if len(s) <= 1:
#             print('About to return True from base case')
#             return True
#         else:
#             answer = s[0] == s[-1] and isPal(s[1:-1])
#             print('About to return', answer, 'for', s)
#             return answer
#             # return s[0] == s[-1] and isPal(s[1:-1]) #s[-1]は最終文字、s[1:-1]の-1は最後から1つ前の文字
    
#     return isPal(toChars(s))

# def testIsPalindrome():
#     print('Try dogGod')
#     print(isPalindrome('dogGod'))
#     print('Try doGood')
#     print(isPalindrome('doGood'))

# testIsPalindrome()

# # 広域変数について；あんまり使用されることはない
# def fib(x):
#     """x >= 0を整数と仮定
#        x番目のフィボナッチ数を返す"""
#     global numFibCalls  #Grobal Valiablesの宣言
#     numFibCalls += 1
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)

# def testFib(n):
#     for i in range(n + 1):
#         global numFibCalls
#         numFibCalls = 0
#         print('fib of', i, '=', fib(i))
#         print('fib called', numFibCalls, 'times.')

# testFib(6)

# 4.5 モジュール
# import
# import circle
# pi = 3
# print(pi)
# print(circle.pi)
# print(circle.area(3))
# print(circle.circumference(3))
# print(circle.sphereSurface(3))

# # インポートするモジュールで定義された名前にアクセスする場合
# from circle import *
# print(pi)

#4.6 ファイル
# sample : write
# nameHandle = open('kids', 'w')
# for i in range(2):
#     name = input('Enter name:')
#     nameHandle.write(name + '\n')
# nameHandle.close()

# sample : read
# nameHandle = open('kids', 'r')
# for line in nameHandle:
#     print(line) # この書き方だと、行末の\nで改行される
# nameHandle.close()

# sample:read - 2
# 改行なし
nameHandle = open('kids', 'w')
nameHandle.write('Michale\n')
nameHandle.write('Mark\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1]) # 改行なし：行末から-1を読み込んでいるから
nameHandle.close()

# 追加書き込み
nameHandle = open('kids', 'a')
nameHandle.write('David\n')
nameHandle.write('Andrea\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])  # \nを回避
nameHandle.close()