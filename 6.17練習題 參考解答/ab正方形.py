# ab正方形
# 輸出由字串ab構成的正方形
# 輸入為正方形邊長 代表每行每列元素的數量

# 輸出為一個正方形 由ab交叉構成
# 第一行的奇數項目為a 偶數項為b
# 第二行則偶數項為a 奇數項為b
# 其他行以此類推

border = int(input())
lst = []
for i in range(border + 1):
    if i %2 == 0:
        lst.append('a')
    else:
        lst.append('b')
for k in range(1,border+1):
    if k%2 != 0:
        i = "".join(lst[0:border])
        print(i)
    else:
        i = "".join(lst[1:border+1])
        print(i)
    