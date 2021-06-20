# 費波納西數列
# 建立一個可計算數列值的程式

# 輸入為一字串
# 輸出為一整數

fib = [0,1]
num = int(input())-1
if num == 1:
    print(fib[0])
elif num == 2:
    print(fib[1])
else:
    init = 0
    answer = 0
    for k in range(num):
        answer = fib[init] + fib[init+1]
        fib.append(answer)
        init += 1
    print(fib[num])