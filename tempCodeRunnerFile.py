class Cat:
    name = "cat"
    def __init__(self,new='moren'):  
        print('change')
        self.name = new

def p(a=1,b=2):
    ret = a + b
    print(ret)


mao = Cat()
print(mao.name)

p(b=5)