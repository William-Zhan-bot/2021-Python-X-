# 翻箱倒櫃
# 在櫃子裡面找東西
# 輸入兩個 1為一組字串 以空格分開的物體 為不同的東西放在櫃子中
# 2為要尋找的物體，找到的話回傳True 如果不在 回傳False
box = input()
box = box.split(" ")
item = input()
if item in box:
    box.remove(item)
    print(True)
    print(box)
else:
    print(False)