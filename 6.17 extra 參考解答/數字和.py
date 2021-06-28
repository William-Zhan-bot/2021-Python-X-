# 數字和
# 輸入為一字串 任意數字構成
# 輸出他們的總和


a = input()
num = []
for i in a:
    num.append(int(i)) # 以整數形式逐個儲存列表
total = 0

# 列表中的整數逐個相加
for k in num:
    total += k
print(total)