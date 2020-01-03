import time


class TestTool:

    @staticmethod
    def acquire_excuted_time(func):
        """
        装饰器：获取代码的执行时间
        """
        def wrapper(*arg,**args):
            start_time = time.time()
            re = func(*arg,**args)
            finsh_time = time.time()
            print(func.__name__, ' excuted_time: ',finsh_time - start_time)
            return re
        return wrapper

    @staticmethod
    def using_log(func):
        print('%s is running...' % func.__name__)

    @staticmethod
    def use_4_process(func):
        """
        装饰器：使用4个进程执行同一个任务
        """
        def wrapper(*args,**kwargs):

        p = mp.Process(targer=func,)
