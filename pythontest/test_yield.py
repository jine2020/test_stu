
#yield +函数==生成器

def provider():
     for i in range(5):
         yield i #return i

p=provider()
print(next(p))
print(next(p))
print(next(p))




