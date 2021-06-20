# 因數
# 輸入一整數 
# 輸出為列表 裡面元素為整數形式的所有因數

# 新增sort()說明
num = int(input())
limit = int(num**0.5)
answer1 = []
for k in range(1,limit+1):
    if num % k == 0:
        answer1.append(k)
        if k == num//k:
            continue
        else:
            answer1.append(num//k)
answer1.sort()
print(answer1)