# -*- coding: utf-8 -*-

# # 整数の二乗を地道に求める
# input_num = int(input('Number:'))  # 入力はstr型で受け取る
# ans = 0
# itersLesft = abs(input_num)
# while (itersLesft != 0):
#     ans = ans + abs(input_num)
#     itersLesft = itersLesft - 1

# print(str(input_num) + '*' + str(input_num) + '=' + str(ans))


# #practice:p23

# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# while (numXs != 0):
#     toPrint = toPrint + 'X'
#     numXs = numXs - 1

# print(toPrint)

# # sample
# # 11と12ともに割りきれる正の整数を見つける
# x = 1
# while True:
#     if x % 11 == 0 and x % 12 == 0:
#         break
#     x = x + 1

# print(x, 'is divisible by 11 and 12')

# # practice:p24
# num = 10  # 入力回数
# flag = False # 奇数入力の判定
# while (num != 0):
#     input_num = int(input('正の整数を入力してください：'))  # 入力される値
    
#     if (input_num % 2 == 1):
#         if (flag == False):
#             max = input_num
#             flag = True
#         else:
#             if (max < input_num):
#                 max = input_num
#     num = num - 1

# if (flag == False):
#     print('奇数が入力されませんでした。')
# else:
#     print('最大の奇数は'+str(max)+'です。')

# 参考の回答
max = 0
i = 0
while i < 10:
    num = int(input('input number:'))
    if num % 2 != 0 and max < num:
        max = num
    i = i + 1

if max != 0:
    print(max)
else:
    print('no positive odd number')
