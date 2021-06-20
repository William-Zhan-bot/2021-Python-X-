# 猜數字

# 設計一個猜數字遊戲 可以讓電腦進行猜測 共有五次機會
# 第一個輸入為預設的答案 一定是1~100的整數 如果不為0到100的話 會輸出:please input between 0~100
# 並會需要重新輸入

# 第一個以後的輸入皆為猜測的數值
# 根據不同的猜測給出不同的結果
# 假設(life)為剩下的次數
# 如果數值太小 則輸出: Guess smaller,last (life) chances 
# 如果數值太大 則輸出: Guess bigger,last (life) chances
# 如果數值不在 1~100 之間 輸出: guesse number not in right area,last (life) chances
# 如果猜對了 則輸出: correct!


life = 5
while True:
    answer = int(input())
    if answer <0 or answer>100:
        print('please input between 0~100')
    else:
        break

while life > 0:
    s = int(input())
    if s>100 or s <0:
        life-=1
        print("guesse number not in right area,last %s chances" % life)
    elif s > answer:
        life -= 1
        print("guess smaller,last %s chances" % life)
    elif s < answer:
        life -= 1
        print("guess bigger,last %s chances" % life)
    else:
        print('correct!')
        break