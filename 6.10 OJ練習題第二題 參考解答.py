# 回文
# 輸入以空格為分開的一組字串
# 輸出為一組字串 為一開始三個字母合起來之後再以相反順序排序一次，前半段為大寫後半段為小寫
# ex. 
# 輸入a b c
# 輸出ABCcba

word = input()
word = word.split(" ")
w1 = "".join(word)
w1 = w1.upper()


word.reverse()
w2 = "".join(word)
w2 = w2.lower()
words = w1 + w2
print(words)