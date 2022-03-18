# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        # print(str(i) + "*" + str(j) + "=" + str(i*j))
        print("%d * %d = %02d" % (i, j, i*j))