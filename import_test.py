
def the_pygame():#音乐播放器？
    import pygame
    # 进行pygame的初始化设置
    pygame.mixer.init()




#cecececeshi

#关于字符串
class String_test():
    def __init__(self):
        self.define_string()


    def define_string(self): #字符串的定义
        self.str1 = "Hello, World!"
        self.str2 = 'Python is fun.'
        self.str3 = """This is a multi-line string.It can span multiple lines."""


    def command(self):  #指令运用
        #拼接
        print(self.str1 + self.str2)
        #通过拼接进行字符串的修改

        self.str1 = ','.join([self.str1[2:], self.str2[:7]])  #拼接字符串
        print(self.str1)


class List_test():
    def __init__(self):
        self.define_list()


    def define_list(self): #列表的定义
        self.list1 = [1, 2, 3, 4, 5]
        self.list2 = ['apple', 'banana', 'cherry']
        self.list3 = [1, 'apple', 3.14, True]
        self.list = [x for x in range(10)]


    def command(self):  #指令运用
        #访问列表元素
        print(self.list1[0])  #访问第一个元素
        print(self.list2[-1])  #访问最后一个元素

        #修改列表元素
        self.list1[0] = 10
        print(self.list1)
        #增加
        self.list1.append(20)
        print(self.list1)
        #筛选
        self.list = [x for x in self.list if x % 2 == 0]












# b = 0

# a = [1,1,2,3,1,4,5,1,6,2,2,4,5]
# for i in a:
#     a = [x for x in a if x != i or a.index(x) != b]
#     b += 1
# print(a)
