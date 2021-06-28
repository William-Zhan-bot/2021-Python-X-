# 01區間
# 輸入01字串
# 輸出 有多少個1的區段

i = input()
box = [] # 處理輸入

count = 0 # 計算初始化
for q in range(len(i)-1): # 逐個開始檢驗是否由1開始 只要有1 即開始計算區段
    if i[q] == '1':
        if i[q+1] == '1': # 同為1 掠過
            continue
        else: # 不為1 代表區段結束 新增一個區段
            count += 1
# 處理特殊情況 若最後項目為1 會少計算一個區段 因此必須補上
if i[-1] == '1': 
    count += 1
    print(count)
else:
    print(count)