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
def selSort(L):
    """Lを, >を用いて比較できる要素からなるリストとする
       Lを昇順にソートする"""
    suffixStart = 0
    while suffixStart != len(L):
        # Suffixの各要素を見る
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #要素の位置を入れ替える
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1

# Generate list
L = [3, 5, 45, 23, 11, 674, 342, 1, 0, 8, 7, 6, 9, 14, 33, 66]

# Sorted list
selSort(L)
print(L)