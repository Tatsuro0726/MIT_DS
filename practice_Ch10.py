# -*- coding: utf-8 -*-
# code10.2
# def search(L, e):
#     """Lを、要素が昇順で並んだリストとする
#        eがLにあればTrueを、そうでなければFalseを返す"""
#     # 二分探索(binary search)
#     def bSearch(L, e, low, high):
#         #high - lowを減少させる（探索領域を縮める）
#         if high == low:
#             return L[low] == e
#         mid = (low + high) // 2  #商を返す
#         if L[mid] == e:
#             return True
#         elif L[mid] > e:
#             if low == mid:
#                 return False
#             else:
#                 return bSearch(L, e, low, mid - 1)
#         else:
#             return bSearch(L, e, mid + 1, high)
    
#     if len(L) == 0:
#         return False
#     else:
#         return bSearch(L, e, 0, len(L) - 1)

# # list作成
# L = [3, 5, 45, 23, 11, 674, 342, 1, 0, 8, 7, 6, 9, 14, 33, 66]
# sort_L = L.sort()

# print(search(L,77))

#10.2 ソーティングアルゴリズム
# selection sort
# 2次の計算時間 while ⇒ O(len(L)), for ⇒ (len(L))
# https://medium-company.com/%E9%81%B8%E6%8A%9E%E3%82%BD%E3%83%BC%E3%83%88/
# def selSort(L):
#     """Lを, >を用いて比較できる要素からなるリストとする
#        Lを昇順にソートする"""
#     suffixStart = 0
#     while suffixStart != len(L):
#         # Suffixの各要素を見る
#         for i in range(suffixStart, len(L)):
#             if L[i] < L[suffixStart]:
#                 #要素の位置を入れ替える
#                 L[suffixStart], L[i] = L[i], L[suffixStart]
#         suffixStart += 1

# # Generate list
# L = [3, 5, 45, 23, 11, 674, 342, 1, 0, 8, 7, 6, 9, 14, 33, 66]

# # Sorted list
# selSort(L)
# print(L)

#10.2.1 マージソート
def merge(left, right, compare):
    """leftとrightをソート済みのリストとし、
       compareを要素間の順序を定義する関数とする
       (left+right)と同じ要素からなり、
       compareに従いソートされた新たなリストを返す"""
    
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare=lambda x, y: x < y):  # 関数を引数としている
    """Lをリストとし
       compareをLの要素間の順序を定義する関数とする
       Lと同じ要素からなり、ソートされた新たなリストを返す"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

# L = [2, 1, 4, 5, 3]
# print(mergeSort(L), mergeSort(L, lambda x, y: x > y)) # x > yは昇順

#10.2.3 Pythonにおけるソーティング
def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:  #姓が同じ場合、名前でソート
        return arg1[0] < arg2[0]

def firstNamelastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else:  #名が同じ場合、姓でソート
        return arg1[1] < arg2[1]

# テストコード
L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, lastNameFirstName)
print('Sorted by last name =', newL)
newL = mergeSort(L, firstNamelastName)
print('Sorted by first name =', newL)

# pythonのソート
# L = [3, 5, 2]
# D = {'a': 12, 'c': 5, 'b':'dog'}
# print(sorted(L))
# print(L)
# L.sort() # リストを変更してしまう
# print(L)
# print(sorted(D))
# D.sort() #dict型はソートできない

L = [[1, 2, 3], (3, 2, 1, 0), 'abc',[1,2,3,4,5,6,7]]
print(sorted(L, key=len, reverse=True))  # key=len:リストの長さが長い順にソート