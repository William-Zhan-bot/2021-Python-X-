num = input()
target = int(input())
num = num.split(" ")
lst = []
for k in num:
    lst.append(int(k))

# 中間的索引
mid_index = (0+len(lst)-1)//2
print(lst)
while True:
    # 找中間點
    if target == lst[mid_index]:
        print(lst[mid_index])
        break
    # target在中間的右邊
    elif target > lst[mid_index]:
        lst = lst[mid_index:]
        print(lst)
        mid_index = (0+len(lst)-1)//2
        if len(lst) == 2:
            print(lst[-1])
            break
    # target在中間的左邊
    else:
        lst = lst[:mid_index+1]
        print(lst)
        mid_index = (0+len(lst)-1)//2
        if len(lst) == 2:
            print(lst[0])
            break

