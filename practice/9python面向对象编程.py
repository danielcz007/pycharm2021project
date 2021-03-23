# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 12:58
# @Author  : Danie      l
'''
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
        方法：类中定义的函数。
        类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
        数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
        方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
        局部变量：定义在方法中的变量，只作用于当前实例的类。
        实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
        继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
        实例化：创建一个类的实例，类的具体对象。
        对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
'''

class Person:
    #类变量，公共变量，类中的方法以及实例对象都可以使用
    name = "无名"
    age = 0
    gender = 'boy'
    weight = 0
    high = 0

    #构造方法，在类实例化的时候就被调用了
    def __init__(self,n,a,g,w):
        #self.变量名 的方式，来访问问题，叫做实例变量 如下:
        #需要注意的是，构造方法中的变量（实例变量）与类变量的区别
        self.name = n
        self.age = a
        self.gender = g
        self.weight = w
        print(n, a, g, w)

    #方法，在类的内部，使用 def 关键字来定义一个方法；类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
    def eat(self):
        print(f"{self.name} eating food")

    def talk(self):
        print(f"{self.name} like toking,so we don\'t like him ")

zhangsan = Person('张三',18,'男',140)
zhangsan.eat()
zhangsan.talk()