# 回文
# 輸入以空格為分開的一組字串
# 輸出為一組字串 為一開始三個字母合起來之後再以相反順序排序一次，前半段為大寫後半段為小寫
# ex. 
# 輸入a b c
# 輸出ABCcba

word = input() # 輸入字串
word = word.split(" ") # 轉換成列表
w1 = "".join(word) # 以新變數w1重新合併成字串
w1 = w1.upper() # 變成大寫

word.reverse() # 將原列表轉換 
w2 = "".join(word) # 以新變數w2重新合併成字串
w2 = w2.lower() # 轉換為小寫
words = w1 + w2 # 字串合併
print(words)