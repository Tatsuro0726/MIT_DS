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

# 4.2 仕様(Specification)
# example:平方根の近似値を探索 bisection method
def findRoot(x, power, epsilon):
    """x と epsilon >0は整数もしくは浮動小数点, power>=1を整数と仮定
       y**powerがxのepsilon以内になるような浮動小数点yを返す
       もし、そのような浮動小数点数が存在しなければNoneを返す"""
    if x < 0 and power % 2 == 0:  # 負の数は平方根を持たない
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2
    while abs(ans ** power - x) >= epsilon:
        if (ans ** power < x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

# findRoot関数のテスト用
def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, 8, -8):
        for power in range(1,4):
            print('Testing x=', str(x), 'and power = ', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print('No root')
            else:
                print(' ', result ** power, '~=', x)

testFindRoot()
