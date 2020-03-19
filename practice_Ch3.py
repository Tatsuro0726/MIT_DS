# -*- coding: utf-8 -*-

# #完全立方の立方根を求める⇒3乗してそのxになるものを探している
# x = int(input('Enter an integer:'))
# ans = 0
# while ans ** 3 < abs(x):
#     ans = ans + 1
# if ans ** 3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of',x,'is',ans)

# # practice:p27
# num = int(input('Enter an positive integer:'))
# pwr = 1
# flag = False
# while pwr < 6:
#     root = 1
#     while root**pwr < num:  # rootのpwr乗がnumになるまで or 超えるまで rootを加算していく
#         root = root + 1
#     if root ** pwr == num:
#         print(root, pwr)
#     pwr = pwr + 1

# print(root,pwr)

# # 参考の回答
# n = int(input())
# i = 5
# while i > 0:
#     root = 1
#     while root ** i < n:
#         root = root + 1
#     if root ** i == n:
#         print(root, i)
#     i = i - 1

# x = 4
# for j in range(x): # このforは4回繰り返される
#     for i in range(x): # j=1のときはx=4が評価されるが、それ以降はx=2が評価されてしまい010101となる
#         print(i)
#         x=2

# # sample
# #完全立方に対する立方根
# x = int(input('Enter an integer:'))
# for ans in range(0, abs(x) + 1):
#     if ans ** 3 >= abs(x):
#         break
# if ans ** 3 != abs(x):
#     print(x, 'is not perfect cube')
# else:
#     if x < 0: # 負の値が入力された場合の処理
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# # sample
# total = 0
# for c in '12345678':
#     total = total + int(c)
# print(total)

# # practice
# total = 0
# s = '1.23,2.4,3.123'
# for i in range(0, len(s)):
#     if i == 0 and s[i] != ',':
#         start = i
    
#     if s[i] == ',':
#         end = i
#         total = total + float(s[start:end])
#         start = i + 1  # start位置の更新
        
# total = total + float(s[start:len(s)])

# print(total)

# # Sample
# # 総当たりを用いた平方根の近似
# x = 0.25
# epsilon = 0.01
# step = epsilon ** 2
# numGuesses = 0
# ans = 0.0
# #while abs(ans ** 2 - x) >= epsilon and ans <= x: #abs(ans ** 2 - x)は誤差 - 誤差がeps以上かつ総当たりの数が25以下
# #⇒この条件だと、xより大きい値が平方根の場合(0<x<1)を考慮できていない。
# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#     ans += step
#     numGuesses += 1  # 回数カウント？
# print('numGuesses =', numGuesses)
# if abs(ans ** 2 - x) >= epsilon: #指定の誤差を超えた場合
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of',x)

# #practice
# # 平方根の近似解のための2分法(bisection search)
# #x = float(input('Enter an integer:'))
# x = -25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low) / 2.0
# while abs(ans ** 2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans ** 2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0 # 探索領域を半分に減らす
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)

# #practice
# # 正負の立方根を求める
# x = -0.008
# n = 3
# epsilon = 0.01
# numGuesses = 0
# if x < 0:
#     low = min(x,-1)
# high = max(1.0, x)
# ans = (high + low) / 2.0
# while abs(ans ** n - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans ** n < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0 # 探索領域を半分に減らす
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)

# Chapter 3.4
# sample
# x = 0.0
# for i in range(10):
#     x = x + 0.1
# if x == 1.0:
#     print(x, '=1.0')
# else:
#     print(x, 'is not 1.0')
# 0.9999999999999999 is not 1.0 :0.1は二進数では表現できないため誤差が生じてしまっている。⇒ EWBのSpreadsheetも同様？？

# Newton's method
# 平方根を求めるためのNewton-Raphson method
# x**2-24=0で誤差がepsilon以下になるxを求める
epslion = 0.01
k = 24.0
guess = k / 2.0
cnt_newton = 0
while abs((guess ** 2) - k) >= epslion:
    cnt_newton += 1
    guess = guess - (((guess ** 2) - k) / (2 * guess))
print('Square root of', k, 'is about', guess)
print('Count_ne =', cnt_newton)

# 2分法
epslion = 0.01
k = 24.0
high = max(1, k)
low = 0
ans = (high + low) / 2
cnt_bisection = 0
while abs(ans ** 2 - 24) >= epslion:
    if ans ** 2 < k:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    cnt_bisection += 1
print('Count_bi =',cnt_bisection)
