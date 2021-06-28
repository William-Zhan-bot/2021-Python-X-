# 母音個數
# 輸入為一字串 有大小寫
# 輸出母音的個數
s = input()
word = []
m = ['a','e','i','o','u']
s = s.lower()
count = 0
for i in s:
    if i in m:
        count += 1
print(count)