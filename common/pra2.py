# 装饰器
import functools

def hi(f):
    @functools.wraps(f)
    def wrap():
        print('1')
        f()
        print('2')
    return wrap

@hi
def say_hi():
    return 'hi'


say_hi()
print(say_hi)
