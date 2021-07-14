lst = input()
i = int(input())
lst = lst.split(" ")
len_lst = len(lst)

try:
    print(lst[i])
except IndexError:
    print(lst[0])
print("clear")