# coding: utf-8

# print("\n========== Python Strings Base begin ==========")
# str_h = "hello"
# str_w = "world"
# print(str_h, str_w)
# print("str_h length:", len(str_h))
# str_hw = str_h + " " + str_w
# print(str_hw)
# str_hw2 = "%s %s %d" % (str_h, str_w, 2019)
# print(str_hw2)
# print("========== Python Strings Base end ==========\n")

# print("\n========== Python Strings Common Operation begin ==========")
# s = "flouis"
# ss = s.capitalize()     # 首字母大写
# print("%s: %s" % ("s.capitalize()", ss))
# print("%s: %s" % ("s.upper()", s.upper()))
# print("ss.lower():", ss.lower())
# print("hello".replace("l", "(ell)"))    # he(ell)(ell)o
# print(len("     world ".strip()))   # Java中trim()方法
# print("========== Python Strings Common Operation end ==========\n")

print("集合是长度可变的数组")

# print("\n========== Python Containers(list) begin ==========")
# print("容器一：列表，是可容纳不同类型元素的有序集合")
# num_list = list(range(5))
# print(num_list)
# num_list.append("foo")
# num_list.append("bar")
# print(type(num_list[0]), type(num_list[-1]))
# print(num_list)
# pop_ele = num_list.pop()
# print(pop_ele, num_list)
# print("列表切片--list slicing")
# print("num_list[2:4]:", num_list[2:4])
# print("num_list[:2]:", num_list[:2])
# print("num_list[2:]:", num_list[2:])
# num_list[2:4] = [7, 8]
# print("num_list:", num_list)
# print("列表循环--list loop")
# for ele in num_list:
#     print(ele, end=" ")
# print()
# for i in range(len(num_list)):
#     print(num_list[i], end=" ")
# print()
# print("========== Python Containers(list) end ==========\n")

# print("\n========== Python Containers(dict) begin ==========")
# print("容器二：字典，存储{键: 值}对的无序集合，等同于Java中的Map或JavaScript中的对象")
# d = {"name": "Flouis", "age": 25, "gender": "M"}
# print(d)
# print("name" in d)      # True  判断字典中是否含有某个键的键值对
# print(d["name"])        # Flouis  索引一
# print(d.get("name"))    # Flouis  索引二
# print("建议使用索引二，因为索引一当字典中没有该键值对时，会报错，索引二相当于是先进行in判断，再取值，不存在时默认返回None")
# print(d.get("xxx"))
# # print(d["xxx"])     # KeyError: 'xxx'
#
# d["height"] = 180   # set an entry in a dict
# print(d)
# del d["age"]        # remove an element from a dict
# print(d)
#
# print("\n字典循环--dict loop")
# for v in d:
#     print("%s: %s" % (v, d[v]), end=" ")
# print()
#
# for key, val in d.items():
#     print("%s: %s" % (key, val), end=" ")
# print()
#
# print("\nDictionary comprehensions:")
# num_list = list(range(5))
# print("%s: %s" % ("num_list", num_list))
# even_num_square = {x: x ** 2 for x in num_list if x % 2 == 0}
# print(even_num_square)
# odd_num_square = {y: y ** 2 for y in num_list if y % 2 == 1}
# print(odd_num_square)
# print("========== Python Containers(dict) end ==========\n")

# print("\n========== Python Containers(set) begin ==========")
# print("容器三：集合，是可容纳不同元素(消除重复元素)的无序集合")
# animals = {"cat", "dog", "fish", "bird", "cat"}
# print("%s: %s" % (type(animals), animals))
# print("%s: %d" % ("len(animals)", len(animals)))
# animals.add("dog")
# print(animals)
# animals.add("butterfly")
# print(animals)
# animals.remove("bird")
# print(animals)
# print("bird" in animals)
#
# print("集合遍历--set loop")
# for animal in animals:
#     print(animal, end=" ")
# print()
#
# for idx, animal in enumerate(animals):
#     print("@%d: %s" % (idx + 1, animal), end="; ")
# print()
# print("========== Python Containers(set) end ==========\n")

# print("\n========== Python Containers(tuple) end ==========")
# print("容器四：元组，只读列表---即定义之后无法修改")
# lis = list(range(5))
# print(lis)
# t = tuple(lis)
# print(t)
# tt = ("abc", "def", "opq")
# print(tt)
# print("元组在很多方面类似于列表，但是元组可以作为字典中的键和集合中的元素，而列表不行")
# d = {(x, x+1): x for x in range(1, 10)}
# print(d)
# print("%s: %s" % ("d[(1, 2)]", d[(1, 2)]))
# idx_tuple = (5, 6)
# print("d.get(%s): %s" % (idx_tuple, d.get(idx_tuple)))
# print("========== Python Containers(tuple) end ==========\n")


# print("\n========== Python Class begin ==========")


class Greeter(object):
    # Constructor
    def __init__(self, name, age):
        self.name = name    # Create an instance variable
        self.age = age

    # toString
    def __repr__(self):
        return "<class: Greeter> { name: %s, age: %s }" % (self.name, self.age)

    # Instance method
    def greet(self, loud=False):
        if loud:
            print("HELLO %s!" % (self.name.upper()))
        else:
            print("hello %s!" % self.name)


greeter = Greeter("Fred", 12)
greeter_name = greeter.name
print("greeter's name: %s" % greeter_name)
print(greeter)
greeter.greet()
greeter.greet(True)

# print("========== Python Class end ==========\n")
