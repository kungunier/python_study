"""
abs(x)返回一个数的绝对值。 参数可以是整数、浮点数或任何实现了 __abs__() 的对象。 如果参数是一个复数，则返回它的模。
"""
# print(abs(-123.456))

# a1 = -123.456
# b1 = a1.__abs__()
# print(b1)

# a2 = 1+2j
# print(abs(a2))
# b2 = a2.__abs__()
# print(b2)

# a3 = 'string'
# print(abs(a3))  TypeError: bad operand type for abs(): 'str'
# b4 = a3.__  str类型找不到__abs__方法



"""
all(iterable)如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True 。 
"""
# list1 = ['123','234','345','456','567']
# print(all(list1))

# for l in list1:
#     if not l:
#         print("测试结果假值")
#     else:
#         print("测试结果真值")

# list2 = []
# print(all(list2))


"""
any(iterable)如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。
"""
# list3 = ['123','234','345','456','']
# print(any(list3))

# list4 = []
# print(any(list4))


"""
ascii(object)与 repr() 类似，返回包含一个对象的可打印表示形式的字符串，
但是 repr() 返回的字符串中非 ASCII 编码的字符会使用 \\x、\\u 和 \\U 来转义。生成的字符串和 Python 2 的 repr() 返回的结果相似。
"""
# str1 = 'string1'
# list5 = ['123','234','345','456','']
# print(type(ascii(str1)))
# print(ascii(list5))
# print(type(ascii(str1)))    就是将一个对象转成字符串类型


"""
eval(expression[, globals[, locals]])
实参是一个字符串，以及可选的 globals 和 locals。globals 实参必须是一个字典。locals 可以是任何映射对象。

expression 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，并使用 globals 和 locals 字典作为全局和局部命名空间。 
如果 globals 字典存在且不包含以 __builtins__ 为键的值，则会在解析 expression 之前插入以此为键的对内置模块 builtins 的引用。 
这意味着 expression 通常具有对标准 builtins 模块的完全访问权限且受限的环境会被传播。 
如果省略 locals 字典则其默认值为 globals 字典。 如果两个字典同时省略，则表达式执行时会使用 eval() 被调用的环境中的 globals 和 locals。 
请注意，eval() 并没有对外围环境下的 (非局部) 嵌套作用域 的访问权限。

返回值就是表达式的求值结果。 语法错误将作为异常被报告。

python是用命名空间来记录变量的轨迹的，命名空间是一个dictionary，键是变量名，值是变量值。
"""
# print(globals())    # globals()Python的全局名字存储地，dict对象
# print(locals())     # locals()Python的局部名字存储地，dict对象

# 1. 不填写后两个参数时，在前两个参数省略的情况下，eval在当前的作用域执行
# eval_a1 = 10
# print(eval('eval_a1+10'))

# 2. 在globals指定的情况下
# eval_b1 = {'eval_a1':100}
# print(eval('eval_a1+11',eval_b1))

# 3. 在 locals指定的情况下 
# eval_a1 = 10; eval_a2 = 20; eval_a3 = 30
# eval_b1 = {'eval_a1':11,'eval_a2':22}
# eval_b2 = {'eval_a2':33,'eval_a3':44}
# print(eval('eval_a1+eval_a2+eval_a3',eval_b1,eval_b2))

# eval()第一个参数必须是字符串，否则会报类型错误，
# 同时eval()会剥去参数的引号，如果得到的不是字符串也会报错,不是字符串的情况下会把它当变量名去查，查不到报NameError
# print(eval(eval_a1))    # TypeError: eval() arg 1 must be a string, bytes or code object
# eval_c1 = "asdf"
# print(eval(eval_c1))    # NameError: name 'asdf' is not defined


"""
repr(object)返回包含一个对象的可打印表示形式的字符串。 
对于许多类型来说，该函数会尝试返回的字符串将会与该对象被传递给 eval() 时所生成的对象具有相同的值，
在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称与通常包括对象名称和地址的附加信息。 
类可以通过定义 __repr__() 方法来控制此函数为它的实例所返回的内容。
"""
# repr_list1 = ['123','234','345','456','']
# print(repr(repr_list1))
# print(type(repr(repr_list1)))

# print(repr_list1.__repr__())
# print(type(repr_list1.__repr__()))


"""
bin(x)将一个整数转变为一个前缀为“0b”的二进制字符串。结果是一个合法的 Python 表达式。
如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。
"""
# bin_a1 = 'string'
# print(bin(bin_a1))      # TypeError: 'str' object cannot be interpreted as an integer

# bin_a1 = 123; bin_a2 = -123
# print(bin(bin_a1))
# print(bin(bin_a2))

# bin_a2 = 'asd'
# print(bin_a2.__index__())   # AttributeError: 'str' object has no attribute '__index__'


"""
class bool([x]) 返回一个布尔值，True 或者 False。 x 使用标准的 真值测试过程 来转换。
如果 x 是假的或者被省略，返回 False；其他情况返回 True。bool 类是 int 的子类（参见 数字类型 --- int, float, complex）。
其他类不能继承自它。它只有 False 和 True 两个实例（参见 布尔值）。
"""
# print(bool(123))
# print(bool(0))
# print(bool('str'))


"""
class bytearray([source[, encoding[, errors]]])
返回一个新的 bytes 数组。 bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。
它有可变序列大部分常见的方法，见 可变序列类型 的描述；同时有 bytes 类型的大部分方法
如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。
"""
# print(bytearray(257.234))   # TypeError: cannot convert 'float' object to bytearray
# print(bytearray(123))
# print(bytearray('str'))     # TypeError: string argument without an encoding
# print(bytearray('str','utf-8'))
# print(bytearray([1,100,1000]))  # ValueError: byte must be in range(0, 256)
# print(bytearray([1,10,100]))
# print(bytearray())


"""
class bytes([source[, encoding[, errors]]])
返回一个新的“bytes”对象， 是一个不可变序列，包含范围为 0 <= x < 256 的整数。
bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作。
"""
# print(bytes())
# print(bytes(123))
# print(bytes([1,10,100]))


"""
callable(object)如果参数 object 是可调用的就返回 True，否则返回 False。 
如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。 
请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。
"""
# print(callable([1,2,3]))
# def callable1():
#     return True
# print(callable(callable1))


"""
chr(i)
返回 Unicode 码位为整数 i 的字符的字符串格式。例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。
实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 i 超过这个范围，会触发 ValueError 异常。
"""
# print(chr(1114111))


"""
@classmethod
把一个方法封装成类方法。
一个类方法把类自己作为第一个实参，就像一个实例方法把实例自己作为第一个实参。
"""
# class A():
#     bar = 123
#     def A_fun1(self):
#         print('这是方法1')
#     @classmethod
#     def A_fun2(cls):
#         print('这是方法2')
#         print(cls.bar)
# A.A_fun2()


"""
max(arg1, arg2, *args[, key])
"""
# print(max([1,2,3],[2,4,6]))
# print(max([]))  # ValueError: max() arg is an empty sequence

"""
min(arg1, arg2, *args[, key])
"""
print(min([1,2,3]))
print(min(['a','b','c'],['str','ing','123']))

