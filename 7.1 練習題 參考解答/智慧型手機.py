class phone:
    def __init__(self,name):
        self.name = name
    
    def contact(self):
        i = self.name + ' can call'
        return i

class computer:
    def __init__(self,name):
        self.name = name

    def web(self):
        i = self.name + ' can use web'
        return i

class iphone(phone,computer):
    pass

a = input()
i = iphone(a)
print(i.contact())
print(i.web())