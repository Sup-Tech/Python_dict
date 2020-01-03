from mathTool import is_prime
from testTools import TestTool
import multiprocessing as mp

@TestTool.acquire_excuted_time
def sum_prime(begin,end):
    re = 0
    for i in range(begin,end):
        if is_prime(i):
            re += i
    print(re)

# 使用多进程 进行100000以内质数的和运算
@TestTool.acquire_excuted_time
def use_4_process(num):
    jobs = []
    for i in range(1, num, num//4):
        begin = i
        end = i + num//4
        p = mp.Process(target=sum_prime,args=(begin,end))
        jobs.append(p)
        p.start()

    [i.join() for i in jobs]
# print(sum_prime(10000001))
# num = 1000001
# for i in range(1,num, num//4):
#     begin = i
#     end = i + num//4
#     p = mp.Process(target=sum_prime, args=(begin,end))
#     p.start()
#     p.join()

use_4_process(10000001)
