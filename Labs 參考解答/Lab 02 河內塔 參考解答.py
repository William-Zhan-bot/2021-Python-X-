def Hanoi(n , a, b, c): # n 代表a上面有幾個環
    if n==1:
        print ("移動鐵環", a, "-->", c) # 只有一層的情況 把所有問題的最小化到這部
    else:
        Hanoi(n-1, a, c, b) # 把上面的n-1層移到中間的柱子b
        Hanoi(1, a, b, c) # 只有最下面一層的情況 a直接到c 
        Hanoi(n-1, b, a, c) # 把中間的n-1層b 移到c
a = int(input())
Hanoi(a, 'A', 'B', 'C')