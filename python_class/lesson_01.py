"""
第一节课：
一、文件命名规则
1、只能包含数字、字母、下划线
2、不能以数字开头
3、不能用"关键字"命名
4、不同数字和字母之间建议用下划线隔开---驼峰命名

二、Python的注释：
1、为什么需要注释
1）解释代码，方便阅读
2）若功能被删除或修改，源代码注释后相当于备份
2、注释方法
1）单行注释：#
2）多行注释：'''   '''
3）快捷键：control + /

三、Python基础语法：
1）Python对缩进非常敏感
2）Python不需要分号
3）Python区分大小写

四、Python的数据类型：
1、整型(int)
2、浮点型(float)
3、布尔型(bool)：True False
4、字符型(str)：被成对的引号包裹的内容 --- 单引号，双引号，三引号
1）引号的嵌套
2）三引号：保持格式，支持换行、缩进

五、Python的内置函数
type()
isinstance()
print()
len()：统计元素个数
str()
int()
input() :在控制台输入内容
range(): 生成一个整数序列，start == 默认值为0，stop == 必填，step == 默认为1，取头不取尾
"""

'''
第二节课：
一、变量 -- 存储数据
1、变量名（是一种标识符），最好见名知意
2、变量一定要先声明再调用

二、字符串的操作：
str1="hello world"
1、取值：索引（即位置），从0开始
print(str[0]) # 打印出来的是h
2、取多个值：切片 [开始：结束：步长] --- 取头不取尾
print(str1[2:5:1]) # 打印出来的是llo
开始省略，默认从0开始取
结束省略，默认取到结尾
步长省略，默认为1
特殊：负数--从右边开始取，-1--取最后一个
3、常用方法
1）replace：替换字符
str1 = str1.replace("world","fechin")
2）index：查找字符索引
   find
index和find都可以用来获取字符的位置，区别在于如果查找的字符不存在，index会报错且运行终止，find则会返回-1
3）count：字符的格式
4、格式化输出
1）.format
占位符：{} .format
.format() 可以按照默认顺序传变量，也可以指定位置传入 == 不能混用
2）%s -- 字符串
%d -- 整数
%f -- 小数

三、Python运算符
1、算数运算符：+ - * / % **
print("I love you" * 3000)
2、赋值运算符：= += -= 有方向性，右边值赋给左边
a = 10
a += 10 等同于 a = a + 10
3、比较运算符：>, >=, <, <=, ！=, == 
== 可以判断字符串是否相同
4、逻辑运算符: and, 真真为真
or, 假假为假
not
5、成员运算符：in, not in

第三节课
一、Python的数据类型
1、列表(list): []，元素与元素之间用英文逗号隔开
1）取值：列表名[索引]
取多个值：切片-- 同字符串一样
2) 列表的元素可以被改变
添加：
list1 = [1, 3.14, "桂花", True, [1, 2, 3, 4]]
list1.append()：追加元素在末尾
list1.insert()：在指定位置追加元素
list1.extend()：一次添加多个值--ist1.extend(["python","lemon"])
删除：
list1.pop()：默认删除最后一个元素，也可指定索引删除 
list1.remove()：指定删除某个元素，如list1.remove(3.14)
list1.clear()：清除所有元素
修改：
list1[1] = "new"
3) 列表的元素可以重复
统计个数：count()

2、元祖(tuple): ()
1）取值：元组名[索引]
取多个值：切片-- 同字符串一样
2) 元祖的元素不可以被改变
3) 元素的元素可以重复
3、字典(dict): {}
1) 键值对：key: value
2) 存储数据属性
key: 不能是可以改变的数据类型（list,dict）；不能重复
value: 可以是任何数据类型；可以被改变
3）字典中的元素没有顺序，通过key取value
dict1 = {"name": "小花", "height": "160", "weight": "60"}
print(dict1["name"])
print(dict1.get("name"))
4) 修改
dict1["weight"] = "50"
dict1["age"] = 20   --- 如果所用键不存在，则会新加入一个元素；存在就会修改
dict1.pop("name")   --- 删除name的键值对
dict1.update({"city" : "北京", "hobby": "biking"})  --- 添加多个键值对
4、集合(set): {}
1) 无序
2）元素不可以重复  -- 使用场景-去重
二、判断
if 条件 : 
    执行语句
elif 条件 :
    执行语句
(多个elif)

else 条件 :
    执行语句

三、循环
for循环：遍历对象里的所有元素
for 变量名 in 数据对象:
    循环体
    
循环中断：break  -- 执行if后，后面代码不执行,跳出整个循环
        continue -- 执行if后，后面代码继续执行，跳出本次循环

第四节课

一、函数
1、语法：
def 函数名():
    函数体
    
2、函数的调用：函数名()
3、函数的参数：
1）形参：函数里不固定的数据，都可以定义为函数的参数
2）实参：调用时传入参数
传参方式：1）位置传参 2）关键字传参：指定参数名字进行传参 3）混合传参：关键字必须跟在位置的后面
3）必备参数 -- 必传的参数
4）默认参数（缺省参数）:
-- 定义的时候给一个默认值，调用的时候可以不传，传入的话替换掉默认值
-- 默认参数必须放在必备参数后面
5）不定长参数*args：元祖，等前面的必备参数和默认参数都传完了，剩下的都给不定长参数 -- 位置传参
6）不定长参数**kwargs： 字典，等前面的必备参数和默认参数都传完了 -- 关键字传参
4、函数的返回值：传入到外面被使用
return
可以有多个返回值，用逗号隔开，用元祖保存
return标志着函数的结束，即使后面有代码也不会执行
第五节课
一、web自动化
1、元素定位八大方法：
1）id：如果id变化，就不可以用id定位
2）name
3）xpath
-- 决定路径：/html/body/div/div/div[1]/a/b   从根节点开始，有顺序性和继承性（一旦页面更改就会失效）
-- 相对路径 
1）标签名+属性 //标签名[@属性名=属性值]
2）如果元素没有属性，第一种方法就会失效，可以通过层级定位，即找到父级后再往下找
//标签名[@属性名=属性值]//标签名[@属性名=属性值]
//div[@class="login-logo"]//b
3）文本属性定位
//b[text() = "柠檬ERP"]
4）包含属性值：//标签名[contains(@属性名/text(),"属性值")]
//b[contains(text(),"柠檬")]
4）css
5）class
6）tag
7）link
8）partial link 

2、常用方法
click
send_keys
text
attribute：获取属性

3、等待
1）强制等待：time.sleep()
2）隐式等待：
在建立会话后面添加
driver.implicitly_wait(10)  最多等待10s，应用于整个代码
3）显示等待

4、iframe
有时候，页面会嵌套页面，无法直接使用id,xpath等定位方式定位到iframe中的元素，所以要先切换到iframe中再对一些元素进行操作
1）切换iframe
通过iframe的ID进行切换
driver.switch_to.frame(iframe_id)
2）通过iframe的Xpath进行切换
3）通过iframe的下标进行切换
driver.switch_to.frame(1)
'''


# str1 = "hello world"
# print(len(str1))
# str1 = str1.replace("world","fechin")
# print(str1)

# name = "小花"
# age = 18
# hobby = "读书"
# print('''----{}---
# name: {}
# age: {}
# hobby: {}
# '''.format(name, name, age, hobby))
#
# print('''----{0}---
# name: {0}
# age: {2}
# hobby: {3}
# '''.format(name, name, age, hobby))

# name = input("请输入姓名：")
# age = input("请输入年龄：")
# sex = input("请输入性别：")
# print('''************
# 姓名:  {0}
# 性别:  {1}
# 年龄:  {2}
# ************
# '''.format(name, sex, age))

# str1 = "python hello aaa 123123aabb"
# print(str1[0:6:1])
# print("ab" in str1)
# print(str1.replace("python", "lemon"))
# print(str1.index("aaa"))

# def salary_sum(bonus, subsidy, salary, *args, **kwargs):
#     sum1 = bonus + subsidy + salary
#     for num in args:
#         sum1 += num
#     for i in kwargs:
#         print(i)
#         sum1 += kwargs[i]
#     return sum1, bonus
#
#
# result = salary_sum(2000, 3000, 500)
# print(result)

# sum1 = 0
# for i in range(1, 11):
#     # print(i)
#     sum1 += i
# print(sum1)

# def length(i):
#     if type(i) == list or type(i) == dict or type(i) == str:
#         j = len(i)
#         if j > 5:
#             print(True)
#         else:
#             print(False)
#     else:
#         print("数据类型不能计算长度")
#
#
# length((1, 3, 6))

# print("1+2 ="+str(1+2))
#
#
def add(a, b):
    sum1 = a + b
    print(sum1)
    return sum1


add(15, 20)


