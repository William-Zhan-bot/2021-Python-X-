# 遞迴 費式數列
def fib(n): # 建立費波納西數列的函式
    if n == 1: # 特殊情況 要求第一個數
        return 0
    elif n == 2: # 特殊情況 要求第二個數
        return 1
    else: # 一般情況 輸出前兩個的和
        return fib(n-1) + fib(n-2)
# 處理輸入
n = int(input())
print(fib(n))