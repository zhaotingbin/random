# import copy
# acc1=['Charlie',['credit',0.0]]
# acc5=copy.deepcopy(acc1)
# acc5[0]='Clinton'
# acc5[1][1]=-19.9
# print(id(acc1)),print(id(acc5)),print(id(acc1)),print(id(acc5))

#
# c1=complex(1,2)
# print(c1.conjugate())
# print(c1.real)

# class Person2:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def say_hi(self):
#         print('你好，我叫',self.name)
# p1=Person2('张三',24)
# p1.say_hi()
# print(p1.age)

class Person3:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person3.count += 1

    def __del__(self):
        Person3.count -= 1

    def say_hi(self):
        print('你好，我叫', self.name)

    def get_count(self):
        print('总计数为：', Person3.count)


print('总计数为：', Person3.count)
p31 = Person3('张三', 25)
p31.say_hi()
Person3.get_count()
# p32 = Person3('李四', 27)
# p32.say_hi()
# Person3.get_count()
# del p31
# Person3.get_count()
# del p32
# Person3.get_count()
