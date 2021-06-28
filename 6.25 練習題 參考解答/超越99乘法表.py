# 超越99乘法表
limit = int(input()) # 輸入為底線
for i in range(1,limit+1): # 第一層迴圈 注意範圍
    for l in range(1,10): # 第二層迴圈 範圍固定
        print(i,"x",l,"=",i*l)