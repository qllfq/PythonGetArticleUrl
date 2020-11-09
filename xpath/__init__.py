# class Parent:
#     parentAttr = 100
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('调用父类构造器')
#
#     def parentMethod(self):
#         print('调用父类方法')
#
#     def setAttr(self):
#         pass
#
#     def __str__(self):
#         return '我的名字是%s,我的年龄是%s' % (self.name, self.age)
#
#
# parent = Parent('lulu', 21)
# print(parent)
# # for letter in 'Python':
# #     if letter == 'h':
# #         pass
# #         print('这是pass块')
# #     print('当前字母：', letter)
# list1 = ['python', 'java', 21, 1999]
# list2 = [0] * 10
# list3 = []
# list3.append('apple')
# list3.append('orange')
#print(list1)
# list3 = list1 + list2
# print(list3)
# print(list2)
# print(list3)
# print('after deleting value at index 2')
# del list1[2]
# print(list1)

#
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('----init---')
#
#     def __new__(cls, *args, **kwargs):
#         print('---new---')
#         return object.__new__(cls)
#
#
# person = Person('lulu', 21)

