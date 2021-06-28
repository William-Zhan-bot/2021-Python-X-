num = int(input())
i = 2
while i < num:
    s = num % i
    if s == 0:
        break
    else:
        i += 1
if num == i:
    print("{0}是質數".format(num))
else:
    print("{0}不是質數".format(num))