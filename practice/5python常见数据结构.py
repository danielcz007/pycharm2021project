# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 21:33
# @Author  : Daniel
'''
    列表
        定义：
            - python中可以通过组合一些值，得到多种复合数据类型
            - 列表是其中最常见的数据结构
            - 列表通过
    元组: () 元素不可修改
    字典：键值对 {}
    集合：用 set() 关键字创建 {}
'''
list_test = ['a', 'b', 'c', 'n', 'd', 1, 2, 3, 4, 5, 7, 8, 1, 'c', 'a', 0]
list_int = [1, 2, 5, 9, 7, 66, 0, 5, 0, 3, 9]
seq_test = (1, 4, 7, 3, 2, 77, 'a', 'df')
''' list 练习
#  序号	函数
#	len(list)
print(len(list_test))
# 表元素个数
#	max(list) 列表必须是数字
print(max(list_int), list_int)
# 回列表元素最大值
#	min(list)
print(min(list_int), list_int)
# 回列表元素最小值
#	list(seq)
# 元组转换为列表
print(list(seq_test), seq_test)
#	list.append(obj)
# 列表末尾添加新的对象
list_test.append("append")
print(list_test)
#	list.count(obj)
# 计某个元素在列表中出现的次数
print(list_test.count(1))
print(list_int.count(0))
#	list.extend(seq)
# 列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list_test.extend(seq_test)
print(list_test)
#	list.index(obj)
# 列表中找出某个值第一个匹配项的索引位置
print(list_test.index(1))
#	list.insert(index, obj)
# 对象插入列表
list_int.insert(10, "ten")
print(list_int)
list_int[10] = 10
print(list_int)
#	list.pop([index=-1])
# 除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list_int.pop())
print(list_int)
#	list.remove(obj)
# 除列表中某个值的第一个匹配项
list_test.remove(1)
print(list_test)
#	list.reverse()
#
# 反向列表中元素
print("===========")
list_int.reverse()
print(list_int)
#	list.sort( key=None, reverse=False)
# 原列表进行排序
list_int.sort()
print(list_int)
list_int.reverse()
print(list_int)

#	list.copy()
# 制列表
list_int_copy = list_int.copy()
print(list_int_copy)
#	list.clear()
# 空列表
list_int_copy.clear()
print(list_int_copy)
# for x in [1, 2, 3]:
#    print(x, end=" ")
'''
