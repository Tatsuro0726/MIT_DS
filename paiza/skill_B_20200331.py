# coding: utf-8
# 標準入力から値を取得してinput_lineに入れる
input_line = input()
N,K = map(int, input_line.split())
A = int(N/K)

import numpy as np

M = np.zeros((N,N)).astype(np.int)
ans = np.zeros((A,A)).astype(np.int)
for i in range(N):
    M[i,:] = list(map(int,input().split()))

for i in range(A):
    start = i*K
    finish = (i+1)*K
    for j in range(A):
        start_j = j*K
        finish_j = (j+1)*K
        ans[i,j] = int(sum(sum(M[start:finish,start_j:finish_j]))/(K**2))

for i in range(A):
    string_line = ''
    for j in range(A):
        string_line += str(ans[i,j]) + ' '
    print(string_line.rstrip(' '))

#