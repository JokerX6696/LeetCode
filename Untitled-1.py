class Cat:
    name = "cat"
    def __init__(self,new='moren',b='123'):  
        print('change')
        self.name = new

def p(a=1,b=2):
    ret = a + b
    print(ret)


mao = Cat(b=123)
print(mao.name)

p(b=5,a=2)