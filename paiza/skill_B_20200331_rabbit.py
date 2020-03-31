# coding: utf-8

# 標準入力から値を取得してinput_lineに入れる
N,M,K = map(int,input().split())
circle = ['']*N
index_list = []
for i in range(M):
    index = int(input())-1 # 位置取得 
    # circle[index] = 'rabbit_' + str(i+1) # うさぎ配置
    index_list.append(index)

for jump in range(K):
    for rabbit_ind in range(M):
        pre_index = index_list[rabbit_ind] # index -1 
        next_index = pre_index + 2
        if next_index > N-1:
            next_index = next_index - N
        # circle[next_index] = 'rabbit_' + str(rabbit_ind+1)
        # circle[pre_index] = ''
        index_list[rabbit_ind] = next_index

for i in index_list:
    print(str(i+1))