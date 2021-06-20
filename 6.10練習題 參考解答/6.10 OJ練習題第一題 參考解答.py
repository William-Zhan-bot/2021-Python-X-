# 變身列表
# 輸入一組數字 以空格分開
# 輸出兩組列表
# 第一組為將字串轉換成列表
# 第二組為原列表但頭尾新增數值a a為第一組列表的長度

num = input() # 輸入字串
word = num.split(" ") # 去除空格 轉換成列表
print(word) # 印出原列表

long = len(word) # 取得列表長度作為新增值
word.append(long) # 新增在最後
word.insert(0,long) # 插入在開頭
print(word)