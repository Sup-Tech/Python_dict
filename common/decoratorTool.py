import functools

# 类装饰器
class loging(object):
  def __init__(self,level="warn"):
    self.level = level

  def __call__(self,func):
    @functools.wraps(func)
    def _deco(*args, **kwargs):
      if self.level == "warn":
        self.notify(func)
      return func(*args, **kwargs)
    return _deco

  def notify(self,func):
    # logit只打日志，不做别的
    print("%s is running" % func.__name__)


@loging(level="warn")#执行__call__方法
def bar(a,b):
  print('i am bar:%s'%(a+b))


bar(1,3)
