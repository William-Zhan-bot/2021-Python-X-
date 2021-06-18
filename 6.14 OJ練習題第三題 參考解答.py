# 三角形

# 三個輸入 為邊長 必定由小到大

# 一個輸出
# 如果可以組直角三角形 輸出數字1 
# 只能組一般三角形 輸出數字0 
# 都不能則輸出False
a = int(input())
b = int(input())
c = int(input())

if a**2 + b**2 == c**2:
    print(1)
else:
    if ((a+b)>c) and ((b+c)>a) and ((a+c)>b):
        print(0)
    else:
        print(False)