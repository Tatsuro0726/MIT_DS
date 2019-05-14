
# nameHandle作成
nameHandle = open('kid','w');

# 名前入力＆書き込み
for i in range(2):
    name = input('Enter name:')
    nameHandle.write(name + '\n')

nameHandle.close()

# 名前の読み込み

nameHandle = open('kid', 'r')

for line in nameHandle:
    print(line)

nameHandle.close()
