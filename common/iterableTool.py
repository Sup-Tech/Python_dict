
class IterableTool:
    """
    只是函数 不做类也行，
    做类是为了 配合面对对象思想
    """
    #  静态方法--不会自动传递参数， 不加静态方法，会
    @staticmethod
    def find_with_condition(iterable, func_condition):
        """
            通用的查找可迭代对象（iterable）中满足func中condition的所有元素
        :param: iterable：需要被搜索的可迭代对象
        :param: func_condition --> bool：需要满足的条件 返回bool值
        :return: 生成器类型，满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find(iterable):
        for item in iterable:
            yield item

    @staticmethod
    def select(iterable, func_handle):
        """
            通用的筛选可迭代对象中的元素
        :param iterable: 需要被筛选的可迭代对象
        :param func_handle: 筛选的处理逻辑
        :return: 生成器类型，
        """
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def sum(iterable, func_handle):
        result = 0
        for item in iterable:
            result += func_handle(item)
        return result

    @staticmethod
    def delete_all_condition(iterable, func_condition):
        """
            删除iterable满足条件的对象
        :param iterable: 可迭代对象
        :param func_condition:条件函数
        :return: count 计数器
        """
        count = 0
        for i in range(len(iterable)-1,-1,-1):
            if func_condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def max_one(iterable, func_condition):
        """
            根据条件(func_condition)找出iterable中的最大值对象
        :param iterable:可迭代对象
        :param func_condition:条件函数
        :return:单个数据
        """
        for i in range(len(iterable)-1):
            for r in range(1,len(iterable)):
                if func_condition(iterable[i],iterable[r]):
                    iterable[i], iterable[r] = iterable[r], iterable[i]
        return iterable[-1]

    @staticmethod
    def list_order(iterable, func_condition):
        """
            根据条件(func_condition)对iterable进行升/降序排列
        :param iterable:可迭代对象
        :param func_condition:条件函数
        :return: None
        """
        for i in range(len(iterable)-1):
            for r in range(i+1, len(iterable)):
                if func_condition(iterable[i],iterable[r]):
                    iterable[i],iterable[r] = iterable[r],iterable[i]
# list_order使用例子
# print(sort(a))
# asd = ['2019-04-20','2020-05-30','1990-01-02','1990-11-20','2020-4-30']
# def func_condition(iterable1,iterable2):
#     return time.mktime(time.strptime(iterable1, '%Y-%m-%d')) < time.mktime(time.strptime(iterable2, '%Y-%m-%d'))
#
# IterableTool.list_order(asd, func_condition)
# print(asd)
