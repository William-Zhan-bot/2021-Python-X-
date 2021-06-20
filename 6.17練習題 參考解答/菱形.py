# 印出一個菱形
# 兩個輸入
# 一個為要打印的圖形a
# 另一個為層數n
# 輸出一個由a打印出 共(2n-1)層的菱形

element = input()
height = int(input())
long = 1 + (height-1)*2
space_num = long//2
element_num = 1

# 上半部
for i in range(height):
    print(" "*space_num + element*element_num)
    space_num -= 1
    element_num += 2

# 初始化
space_num += 2
element_num -= 4

# 下半部
for q in range(height-1):
    print(" "*space_num + element*element_num)
    space_num += 1
    element_num -= 2