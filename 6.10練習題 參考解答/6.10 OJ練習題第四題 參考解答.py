# 列表操作
# 輸入 一組文字(偶數個) 以空格分開
# 輸出 
# 1.轉換成的列表 在列表頭尾端插入"python"字串後的列表 
# 2.一列表，只包含原列表單數索引的列表元素
# 3.輸出原列表前面半段反轉後的列表
# 4.輸出原列表後面半段反轉後的列表

# 列表操作
s = input() # 輸入一組文字(偶數個) 以空格分開
list_ = s.split(" ") # 輸出 轉換成的列表
list_.append("python") # 在列表頭尾端插入"python"字串後的列表 
list_.insert(0,"python") # 在列表初始插入"python"字串後的列表
print(list_)

# 一列表，只包含單數索引的列表元素
odd = list_[1:len(list_):2]
print(odd)

# 輸出前半段 後半段分開反轉後的列表 以len()去適應不同列表的長度
sep1 = list_[0:len(list_)//2] # 前半段
sep2 = list_[len(list_)//2:len(list_)] # 後半段
# 分別反轉
sep1.reverse()
sep2.reverse()
# 輸出
print(sep1)
print(sep2)
