# 兩倍列表
# 輸入一組數字 以空格分開
# 輸出兩組列表
# 第一組為將字串轉換成列表
# 第二組為原列表但頭尾新增數值a a為第一組列表的長度

num = input()
word = num.split(" ")
print(word)
long = len(word)
word.append(long)
word.insert(0,long) 
print(word)