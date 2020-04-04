# 時間t と 移動距離dist は, 偶数と奇数が一致する

t, x, y = 0, 0, 0
msg = 'YES'
for i in range(int(input())):
    next_t, next_x, next_y = map(int, input().split())
    dist = abs(next_x - x) + abs(next_y - y)  #移動距離
    step = next_t - t  #移動時間
    if step < dist:  #移動時間より移動距離が大きい場合は、No
        msg = 'NO'
        break
    if step % 2 != dist % 2:
        msg = 'NO'
        break
    else:
        t, x, y = next_t, next_x, next_y

print(msg)