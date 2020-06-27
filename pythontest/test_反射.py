class Person:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f'{self.name} is eating')

p=Person('JERRY')
print(hasattr(p,'name'))#判断实例有没有属性或方法
f=getattr(p, 'eat')#获取实例的属性或方法
f()
