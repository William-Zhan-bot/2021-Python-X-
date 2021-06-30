class birds:
    type = "bird"
    def __init__(self,name,move,feather):
        self.name = name
        self.move = move
        self.feather = feather

    def get_move(self):
        return self.move
    def get_feather(self):
        return self.feather
        
a = input()  
b = input()  
c = input()  
k = birds(a,b,c)
print(k.get_move())
print(k.get_feather())
print(birds.type)