# -*- coding: utf-8 -*-

# Chapter5
# タプル(tuple)

# t1 = ()
# t2 = (1, 'two', 3)
# print(t1)
# print(t2)

# # tupleで1を宣言するには、、、
# t3 = (1,)  # ,カンマが必須

# # tupleの反復
# print(3 * t2)

# index, slice
# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])

# tupleの要素の反復
# def intersect(t1, t2):
#     """t1, t2はタプルであると仮定
#        t1とt2両方に入っている要素を含むtupleを返す"""
#     result = ()  #返り値用変数
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result

# t1 = (1, 2, 3, 'abc', 5)
# t2 = (2, 7, 5, 'abc')

# print(intersect(t1,t2))

# 多重代入文：x,y = (3,4)
# # 最小公約数と最大公約数
# def findExtremeDivisors(n1, n2):
#     """n1とn2を正のint型とする.
#        n1とn2の最小公約数 > 1と最大公約数からなるtupleを返す。
#        公約数がない場合, (None, None) を返す. """
#     minVal, maxVal = None, None  # 返り値用変数
#     for i in range(2, min(n1, n2) + 1): #(n1,n2の小さい方まで繰り返す)
#         if n1 % i == 0 and n2 % i == 0:  # どちらでも割り切れた場合
#             if minVal == None:  # 最初の公約数をminValに格納
#                 minVal = i
#             maxVal = i
#     return (minVal, maxVal)

# input_n1 = int(input('Enter an integer:'))
# input_n2 = int(input('Enter an integer:'))

# min, max = findExtremeDivisors(input_n1,input_n2)

# print(str(min), str(max))

# 5.3 リストと可変性
# L = ['I did it all', '4', 'love']
# for i in range(len(L)):
#     print(L[i])

# sample
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

# UnivsはTechとIvysのリストを参照している
# Univs1は、新たに[['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]というリストを作成している
# 従ってUnivs と Univs1は見た目は同じだが、コンピューター上の中身は違うものである。
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

# print('Univs = ', Univs)
# print('Univs1 = ', Univs1)
# print(Univs == Univs1)

# 上記リストのオブジェクトidが等しいかをCheck
# print(id(Univs) == id(Univs1))
# print('Id of Univs =', id(Univs))
# print('Id of Univs1 = ', id(Univs1))

# 実行結果：Univs とUnivs1は異なる
# False
# Id of Univs = 1439693290696
# Id of Univs1 =  1439695041288

Techs.append('RPI')

# print('Univs =', Univs)
# print('Univs1 =', Univs1)

# 出力結果
# Univs = [['MIT', 'Caltech', 'RPI'], ['Harvard', 'Yale', 'Brown']] ⇒ UnivsはTechsを経由してリストにアクセス
# Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]　⇒ Univs1は、Univs1オブジェクトが割り当てられているリストオブジェクトの最初の要素を経て参照されている。

# for e in Univs:
#     print('Univs contains', e)
#     print(' which contains')
#     for u in e:
#         print('     ', u)

# # リストの連結
# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# L3 = L1 + L2
# print('L3 = ', L3)
# L1.extend(L2)  # L1リストの末尾に、リストL2の要素を追加
# print('L1 = ', L1)
# L1.append(L2)  # L1リストの末尾に、リストL2を追加
# print('L1 =', L1)

# # 出力結果：
# L3 =  [1, 2, 3, 4, 5, 6]
# L1 =  [1, 2, 3, 4, 5, 6]
# L1 = [1, 2, 3, 4, 5, 6, [4, 5, 6]]

# 5.3.1 クローンの作成
# def removeDups(L1, L2):
#     """L1とL2をリストとする。
#        L1からL2の中にも存在する要素を取り除く"""
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)

# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups(L1, L2)
# print('L1 =',L1)

# Clone: slice
# L1_copy = L1[:] # スライスはCloneとなる
# L1_copy2 = L1 # 参照
# print(id(L1),id(L1_copy),id(L1_copy2))
# 2592714781896 2592714782024 2592714781896

# #5.3.2 リスト内包
# L = [x ** 2 for x in range(1, 7)]
# print(L)

# mixed = [1, 2, 'a', 3, 4.0]
# print([x**2 for x in mixed if type(x) == int])

# 5.4
# 高階プログラミング(high-order programming)
# 関数を引数として使用

# def applyToEach(L, f):
#     """Lをリスト、fを関数とする。
#        Lのそれぞれの要素eをf(e)に置換してLを更新する。"""
#     for i in range(len(L)):
#         L[i] = f(L[i])

# L = [1, -2.3, 3.333]
# print('L =', L)
# print('Apply abs to each element of',L)
# applyToEach(L, abs)
# print('L =', L)
# print('Apply abs to each element of',L)
# applyToEach(L, int)
# print('L =', L)

# 高階関数map
# 一般的なfor文で利用：map(function,functionに代入すること)
# for i in map(abs, [-1, 2, -3, -5]):
#     print(i)

# lamdba式: lambda parameter_list: expression(式)
# sample
# L = []
# for i in map(lambda x, y: x ** y, [1, 2, 3, 4], [3, 2, 1, 0]):
#     L.append(i)
# print(L)

# 5.5：文字列,タプル,範囲とリスト
