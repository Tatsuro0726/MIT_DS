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

# practice:p27
num = int(input('Enter an positive integer:'))
root = num
pwr = 1
flag = False
while pwr < 6:
    while root > 0:
        if root ** pwr == num:
            flag = True
            break

        root = root - 1
    pwr = pwr + 1

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
