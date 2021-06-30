# 處理輸入
map = input()
map = map.split(" ") # 地圖名稱 地圖邊長 避難點x,y座標

danger = input(" ")
danger = danger.split(" ") # 災害中心點x,y 傷害半徑

people = input()
people = people.split(" ") # 人名 x,y座標 衝刺半徑

# 處理數據
map[1] = int(map[1]) # 邊長
map[2] = int(map[2]) # x
map[3] = int(map[3]) # y

danger[0] = int(danger[0]) # x
danger[1] = int(danger[1]) # y
danger[2] = int(danger[2]) # 半徑

people[1] = int(people[1]) # x
people[2] = int(people[2]) # y
people[3] = int(people[3]) # 半徑

# 建立條件與運算

if map[1] <= 0:
    print('error')
else:
    # 檢查是否在災害範圍外
    if ((people[1] - danger[0])**2 + (danger[1] - people[2])**2)**0.5 > danger[2]:
        print(people[0],"safe in",map[0])
    else:
 # 比較是否避難所在人的衝刺範圍內
        if ((people[1]- map[2])**2 + (people[2]- map[3])**2)**0.5 < people[3]**0.5:
            print (people[0],"safe in",map[0])
        else:
            print (people[0],"bye bye")