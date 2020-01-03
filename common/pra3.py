"""
    练习:在不改变fun01与fun02函数定义和调用的情况下,
         为期增加新功能(打印函数执行时间)
                       记录开始与结束时间
"""
import time

# 使用装饰器，拦截对旧功能的调用
# 将新功能与旧功能包装在一起
def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # func -- 旧功能
        re = func(*args, **kwargs)
        stop_time = time.time()
        # 新功能 -- 打印执行时间
        print(stop_time - start_time)
        return re

    return wrapper


@print_execute_time  # print_execute_time(fun01)
def fun01():
    time.sleep(2)  # 睡眠2秒，用于模拟计算2秒钟
    return 'xxx'

@print_execute_time
def fun02(a):
    time.sleep(3)  # 睡眠3秒


fun01()
print(fun01())
fun02(10)
