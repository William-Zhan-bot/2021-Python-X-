# 連霸王
# 輸入為一字串 以空格分開
# 輸出最多的遞增次數

# 處理輸入
a = input()
num = a.split(" ")
int_num = []
for i in num:
    int_num.append(int(i))
# 建立列表中與前一個相減的數列 
int_num_a = int_num[:len(int_num)-1]
int_num_b = int_num[1:]
# print(int_num_a)
# print(int_num_b)
minus = []
for q in range(len(int_num_a)):
    equal = int_num_b[q] - int_num_a[q]
    minus.append(equal)

# 以POP取出差數列中的第一個同時刪除 準備開始檢驗
temp = minus.pop(0)
# 檢查第一個 (因為相減會把第一個的差忽略 這邊補上)
if int_num[0] + temp == int_num[1]:
    count = 1
else:
    count = 0
# 之後開始比較差是否相等 相等則count中記錄
ans = []
for i in minus:
    if i == temp:
        count += 1
    else:
        temp = i
    ans.append(count)
print(max(ans)) # 列表中最大的值，即為最多次的遞增次數