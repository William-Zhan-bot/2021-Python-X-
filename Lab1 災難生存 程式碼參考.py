# 避難模擬器
map = input()
map = map.split(" ")
# init 地圖名稱 地圖大小 避難點座標x y
# korea 30 5 5
map[1] = int(map[1]) # 大小
map[2] = int(map[2]) # 避難點x座標
map[3] = int(map[3]) # 避難點y座標 

danger = input()
danger = danger.split(" ")
# danger x y 傷害半徑
# 25 25 12
danger[0] = int(danger[0]) # x
danger[1] = int(danger[1]) # y
danger[2] = int(danger[2]) # danger

people = input()
people = people.split(" ")
# 人名 x y 衝刺距離
# Ming 4 4 2
people[1] = int(people[1]) # x
people[2] = int(people[2]) # y
people[3] = int(people[3]) # 衝刺

# 檢查地圖是否成立
if map[1] <= 0:
    print('error')
else: # 檢查人是否超出邊界
    # 檢查是否為災害範圍內
    if ((people[1]-danger[0])**2+(people[2]-danger[1])**2)**0.5 <= danger[2]:
        if ((people[1]-map[2])**2+(people[2]-map[3])**2)**0.5 <= people[3]:
            #print("safe for security") ##
            print(people[0],"safe in",map[0])
        else:
            #print("dead for no security") ## 
            print(people[0],"bye bye")
    else:
        #print("safe for not in danger area") ##
        print(people[0],"safe in",map[0])