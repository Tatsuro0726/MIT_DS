nameHandle = open('kid','w')
nameHandle.write('Michael\n')
nameHandle.write('Mark\n')
nameHandle.close()
nameHandle = open('kid','r')

for line in nameHandle:
    print(line[:-1])

nameHandle.close()
