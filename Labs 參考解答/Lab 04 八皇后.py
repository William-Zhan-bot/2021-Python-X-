# 輸入一個整數
# 4 皇后
n = int(input())

table = [] # 已經選擇的index

def  check(x,table): # 座標 
    for index,pos in enumerate(reversed(table)):
        # 左上 右上
        if (x - index -1 == pos) or(x + index +1 == pos):
            return False
    return True
# 逐個搜尋棋盤擺法的功能 不會檢查擺過的地方
def search(table):
    if len(table) == n: # 代表每一行 都有一個皇后 而且彼此不衝突
        print(table)
    for i in range(n): # 每次搜尋的棋盤格i 
        if i not in table: # 同層不會有兩個
            #檢查是否衝突
            if check(i,table): # 彼此不衝突
                table.append(i)
                search(table) # 
                table.pop() # 如果搜尋沒有結果的話 會取消值
# 解的話是列表 直接丟出

search(table)