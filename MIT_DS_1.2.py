nameHandle = open('kid','a')
nameHandle.write('David\n')
nameHandle.write('Andrew\n')
nameHandle.close()
nameHandle = open('kid','r')
for line in nameHandle:
    print(line[:-1])

nameHandle.close()
