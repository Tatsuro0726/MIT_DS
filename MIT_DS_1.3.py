# 高階プログラミング

# 関数を引数とする関数
def applyToEach(L, func):
    """L：リスト，func：関数を引数とする """
    for i in range(len(L)):
        #Lの要素をfunc()に置換する
        L[i] = func(L[i])

L = [1,-2,3.33]
print('L=',L)
print('Apply abs to each element of',L)
applyToEach(L,abs)
print('L=',L)
print('Apply int to each element of', L)
