# 相反數列
# 輸入一個整數a
# 輸出1~a內由1-2+3-4.....a 的整數和
i = int(input())
n = 1
m = 0 
while n < i+1:
    temp = n % 2
    if temp == 0:
        m=m-n
    else:
        m=m+n
    n+=1
print(m)