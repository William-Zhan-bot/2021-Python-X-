# 神的考驗
class Person: # 建立人的類別
    life = 80 # 屬性 壽命長度
    def __init__(self,name): # 初始化
        self.name = name

n = input()
num = int(input())
p = Person(n) # 建立Person物件
p.life = Person.life-num//100 # 處理人物物件的屬性
Person.life = num # 處理類別的屬性

print(p.name)
print(Person.life)
print(p.life)