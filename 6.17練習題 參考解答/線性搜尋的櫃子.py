# 線性搜尋櫃子
# 輸入為一組物品 字串 空格分開 建立一個由頭到尾的搜尋系統
# 輸出為 "物品 in 物品的位置(櫃子中第幾個)"
# 如果物品不在則輸出False

s = input()
s = s.split(" ")
stuff = input()
print(s)
switch = 0

for k in range(len(s)):
    if s[k] == stuff:
        print(s[k],"in",k+1)
        switch = 1
        break
if switch == 0:
    print(False)