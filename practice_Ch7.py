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
def sumDigits(s):
    """sを文字列とする.
       sの中の数字の合計を返す.
       例えば,sが'a2b3c'ならば5を返す"""
    number = 0
    for c in s:
        try:
            number += int(c)
        except ValueError:
            pass
    return number

input = input('Enter string:')
print(sumDigits(input))