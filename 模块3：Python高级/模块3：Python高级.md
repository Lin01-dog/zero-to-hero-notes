# 模块3：Python高级

## 模块概述

本课程旨在介绍Python编程语言中的面向对象编程（OOP）概念和技术。学生将学习如何使用类、对象、继承、多态等OOP的关键要素来构建灵活、可重用和可扩展的代码。通过实际编程练习和项目，学生将提高他们的编程技能，学会设计和实现面向对象的解决方案。

面向对象编程是在面向过程编程的基础上发展来的，它比面向过程编程具有更强的灵活性和扩展性。面向对象编程是程序员发展的分水岭，很多初学者会因无法理解面向对象而放弃学习编程，所以我们一定要足够重视。

#### 课程目标

- 理解面向对象编程的基本原则和思想。
- 掌握Python中的类、对象、属性和方法的概念。
- 熟悉继承、多态和封装等OOP的高级概念。
- 能够设计和实现面向对象的解决方案。
- 培养良好的编码风格和软件工程实践。
## Day11：面向对象基础

![截屏2024-02-25 18.34.35](./assets/%E6%88%AA%E5%B1%8F2024-02-25%2018.34.35-8857328.png)

### 1. 类和对象

#### 【1】类和对象的概念

面向对象编程（Object-oriented Programming，简称 OOP）是一种编程范式。

* 从思想角度讲

面向对象思想来源于对现实世界的认知。现实世界缤纷复杂、种类繁多，难于认识和理解。但是聪明的人们学会了把这些错综复杂的事物进行分类，从而使世界变得井井有条。现实世界中每一个事物都是一个对象，它是一种具体的概念。类是人们抽象出来的一个概念，所有拥有相同**属性**和**功能**的事物称为一个类；而拥有相同属性和功能的具体事物则成为这个类的实例对象。

比如现实世界中，

狗的**属性**是有尾巴，有毛，四条腿等，**功能**是能汪汪叫，能吃骨头，能咬人等。能有这些属性和功能的事物我们就认为属于狗类。

人的**属性**是两条腿，没有尾巴等，**功能**是能玩火，能尿炕，能使用工具。能有这些属性和功能的事物我们就认为属于人类。

电脑**属性**是有CPU，存储器，操作系统等，功能就是能安装APP，能连网等。能有这些属性和功能的事物我们就认为属于电脑类。

汽车的**属性**是有四个轮子，一个底盘，一个方向盘等，**功能**是能行驶，能加速，能刹车等。能有这些属性和功能的事物我们就认为属于汽车类。



![未命名文件](./assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6-8856776.png)



面向对象编程提供了一种从现实世界中抽象出概念和实体的方法。通过类和对象的概念，可以将现实世界中的问题和关系转化为代码结构，使得程序更加符合问题域的模型化。

面向对象编程通过采用类的概念，把事物编写成一个个“类”。在类中，用数据表示事物的状态，用函数实现事物的行为，这样就使编程方式和人的思维方式保持一致，极大的降低了思维难度。

![未命名文件 (2)](./assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6%20(2)-8871360.png)

```python
legs_num = 4
has_hair = True
has_tail = True

def bark(self):
    print("狗狂吠")

def bite(self):
    print("狗咬人")

def fetch(self):
    print("狗捡球")
    
legs_nums = 2
has_wings = True
has_teeth = False

def fly(self):
    print("鸟飞翔")

def eat_worms(self):
    print("鸟吃虫子")

def nest(self):
    print("鸟筑巢")
```

类版本：

```python
# 声明类
class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("狗狂吠")

    def bite(self):
        print("狗咬人")

    def fetch(self):
        print("狗捡球")

# 实例化对象
alex = Dog()
print(alex.legs_num)
alex.bark()
alex.bite()


class Bird:
    legs_nums = 2
    has_wings = True
    has_teeth = False

    def fly(self):
        print("鸟飞翔")

    def eat_worms(self):
        print("鸟吃虫子")

    def nest(self):
        print("鸟筑巢")

# 实例化对象
b1 = Bird()
print(b1.has_wings)
print(b1.has_teeth)
b1.fly()
```

* 从封装角度讲

面向对象编程（Object-oriented Programming，简称 OOP），是一种封装代码的方法。其实，在前面章节的学习中，我们已经接触了封装，比如说，将乱七八糟的数据扔进列表中，这就是一种简单的封装，是数据层面的封装；把常用的代码块打包成一个函数，这也是一种封装，是语句层面的封装。

面向对象编程，也是一种封装的思想，不过显然比以上两种封装更先进，它可以更好地模拟真实世界里的事物（将其视为对象），并把描述特征的数据和代码块（函数）封装到一起。

面向对象编程（Object-Oriented Programming，简称OOP）相较于面向过程编程（Procedural Programming）有以下几个优点：

1. **封装性（Encapsulation）**：面向对象编程通过将数据和操作封装在一个对象中，使得对象成为一个独立的实体。对象对外部隐藏了内部的实现细节，只暴露出必要的接口，从而提高了代码的可维护性和模块化程度。
2. **继承性（Inheritance）**：继承是面向对象编程的重要特性之一。它允许创建一个新的类（子类），从一个现有的类（父类或基类）继承属性和方法。子类可以通过继承获得父类的特性，并可以在此基础上进行扩展或修改。继承提供了代码重用的机制，减少了重复编写代码的工作量。
3. **多态性（Polymorphism）**：多态性使得对象可以根据上下文表现出不同的行为。通过多态机制，可以使用统一的接口来处理不同类型的对象，而不需要针对每种类型编写特定的代码。这提高了代码的灵活性和可扩展性。
4. **代码的可维护性和可扩展性**：面向对象编程强调模块化和代码复用，通过将功能划分为独立的对象和类，使得代码更易于理解、测试和维护。当需求变化时，面向对象编程的结构和机制使得代码的修改和扩展更加简洁和可靠。

总的来说，面向对象编程提供了一种更加结构化、可扩展和可维护的编程范式。它通过封装、继承和多态等特性，使得代码更加模块化、灵活和易于理解。这些优点使得面向对象编程成为当今广泛采用的编程范式之一，被广泛应用于软件开发中。

#### 【2】类和实例对象的语法

面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Person类，而实例是根据类创建出来的一个个具体的“对象”。

![img](./assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0J1YmIxZV8=,size_16,color_FFFFFF,t_70-8834249-8834252.jpeg)

```python
# 声明类
class 类名：
    类属性...
    方法...
    
# 类的实例化
实例对象 = 类名() # 开辟一块独立的属于实例空间，将空间地址作为返回值

# 实例对象可以通过句点符号调用类属性和方法
实例对象.类属性
实例对象.方法(实参)
```

> 1. 和变量名一样，类名本质上就是一个标识符，命名遵循变量规范。如果由单词构成类名，建议每个单词的首字母大写，其它字母小写。
> 2. 冒号 + 缩进标识类的范围
> 3. 无论是类属性还是类方法，对于类来说，它们都不是必需的，可以有也可以没有。另外，Python 类中属性和方法所在的位置是任意的，即它们之间并没有固定的前后次序。

![截屏2024-02-25 23.35.45](./assets/%E6%88%AA%E5%B1%8F2024-02-25%2023.35.45-8875356.png)

```python
# 声明类
class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("狗狂吠")

    def bite(self):
        print("狗咬人")

    def fetch(self):
        print("狗捡球")


# 实例化对象
alex = Dog()
print(alex.legs_num)
alex.bark()
alex.bite()
# 实例化对象
peiQi = Dog()
# print(id(alex))
# print(id(peiQi))

print(id(alex.legs_num))
print(id(peiQi.legs_num))

print(id(alex.bark))
print(id(peiQi.bark))
```

### 2. 实例属性和实例方法

![截屏2024-02-26 00.53.06](./assets/%E6%88%AA%E5%B1%8F2024-02-26%2000.53.06-8880008.png)

#### 【1】实例属性

类变量（类属性）的特点是，所有类的实例化对象都同时共享类变量，也就是说，类变量在所有实例化对象中是作为公用资源存在的。实例属性是属于类的每个实例对象的特定属性。实例属性是在创建对象时赋予的，每个对象可以具有不同的实例属性值。

```python
alex = Dog()
peiQi = Dog()
# 实例属性: 属于实例对象自己的属性
alex.name = "李杰"
alex.age = 10
peiQi.name = "武大郎"
peiQi.age = 20
# 问题1:
print(alex.name)
alex.age = 30
print(alex.age)
# 问题2:
print(peiQi.age)
# 问题3:
alex.bark()
alex.bark = "hello world"
# alex.bark()
peiQi.bark()
```

#### 【2】实例方法和self

在 Python 的类定义中，`self` 是一个特殊的参数，用于表示类的实例对象自身。`self` 参数必须作为第一个参数出现在类的方法定义中，通常被约定为 `self`，但实际上你可以使用其他名称。

当你调用类的方法时，Python 会自动将调用该方法的实例对象传递给 `self` 参数。这样，你就可以通过 `self` 参数来引用和操作实例对象的属性和方法。

```python 
class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def eat(self):
        print(f"{self.name}正在吃东西。")

    def run(self):
        print(f"{self.name}正在跑。")

    def sleep(self):
        print(f"{self.name}正在睡觉。")

    def bark(self):
        print(f"{self.name}正在狂吠。")

    def show_info(self):
        print(f"名字：{self.name}，品种：{self.breed}，颜色：{self.color}，年龄：{self.age}")


# 声明对象
bulldog = Dog()
# 赋值实例属性
bulldog.name = "小灰"
bulldog.breed = "斗牛犬"
bulldog.color = "浅灰色"
bulldog.age = 5

# 调用斗牛犬的行为
bulldog.eat()
bulldog.run()
bulldog.sleep()
bulldog.bark()
bulldog.show_info()
```

### 3. 构造方法`__init__`

在上节课的代码中，对象的属性是通过直接赋值给对象的实例属性来实现的，而不是在构造方法中进行初始化。这样做可能会导致以下问题：

1. 代码冗余：每次创建对象时都需要分别为每个对象赋值实例属性，这会导致代码冗余和重复劳动。
2. 可维护性差：如果类的属性发生变化或新增属性，需要修改多处代码来适应这些变化，而如果使用构造方法来初始化属性，则只需要在一个地方进行修改。

为了改进这种写法，可以使用构造方法来初始化对象的属性。构造方法在创建对象时自动调用，并可以接受参数来初始化对象的属性。

```python
class Dog:

    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃东西。")

    def run(self):
        print(f"{self.name}正在跑。")

    def sleep(self):
        print(f"{self.name}正在睡觉。")

    def bark(self):
        print(f"{self.name}正在狂吠。")

    def show_info(self):
        print(f"名字：{self.name}，品种：{self.breed}，颜色：{self.color}，年龄：{self.age}")


# 声明对象
bulldog = Dog("小灰", "斗牛犬", "浅灰色", 5)

# 调用斗牛犬的行为

bulldog.bark()
bulldog.show_info()

# 声明对象
beagle = Dog("小黄", "小猎犬", "橘色", 6)

beagle.bark()
beagle.show_info()
```

实例化一个类的过程可以分为以下几个步骤：

1. 创建一个新的对象（即开辟一块独立空间），它是类的实例化结果。
2. 调用类的`__init__`方法，将新创建的对象作为第一个参数（通常命名为`self`），并传递其他参数（如果有的话）。
3. 在`__init__`方法中，对对象进行初始化，可以设置对象的属性和执行其他必要的操作。
4. 返回新创建的对象，使其成为类的实例。

![未命名文件 (1)](./assets/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6%20(1)-8841742-8841743.png)

在创建类时，我们可以手动添加一个 `__init__()` 方法，该方法是一个特殊的类实例方法，称为构造方法（或构造函数）。

`__init__() `方法可以包含多个参数，但必须包含一个名为 self 的参数，且必须作为第一个参数。除了 self 参数外，还可以自定义一些参数，从而完成初始化的工作。

> 1. 注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`是指向创建的实例本身。
> 2. 实例属性，实例变量，实例成员变量都是指的存在实例空间的属性

### 4. 一切皆对象

在python语言中，一切皆对象！

我们之前学习过的字符串，列表，字典等等数据都是一个个的类，我们用的所有数据都是一个个具体的实例对象。

区别就是，那些类是在解释器级别注册好的，而现在我们学习的是自定义类，但语法使用都是相同的。所以，我们自定义的类实例对象也可以和其他数据对象一样可以进行传参、赋值等操作。

> 1. 自定义类对象是可变数据类型，我们可以在创建后对其进行修改，添加或删除属性和方法，而不会改变类对象的身份。
> 2. 实例对象也是一等公民

### 5. 类对象、类属性以及类方法

#### 【1】类对象

类对象是在Python中创建类时生成的对象，它代表了该类的定义和行为，存储着公共的类属性和方法

```python
class Car(object):
    # 类属性
    total_cars = 0
    def __init__(self,make,model):
        self.make = make
        self.model = model

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

car1 = Car("Toyota", "Camry")
```

> 类对象.实例方法会怎么样？

#### 【2】修改类属性

```python 
class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1
        
    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

    def display_total_cars(self):
        # print("Total cars:", self.total_cars)
        print("Total cars:", Car.total_cars)

    
# 创建两辆汽车
car1 = Car("Toyota", "Camry")
car1.display_total_cars()
car2 = Car("Honda", "Accord")
car1.display_total_cars()
```

#### 【3】类方法

定义：使用装饰器`@classmethod`。第一个参数必须是当前类对象，该参数名一般约定为`cls`，通过它来传递类的属性和方法（不能传实例的属性和方法）；

调用：类对象或实例对象都可以调用。

```python
class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    @classmethod
    def display_total_cars(cls):
        print(f"Total cars of {cls.__name__}: {cls.total_cars}")

# 创建两辆汽车
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# 显示车辆总数
Car.display_total_cars()  # 输出: Total cars of Car: 2

# 创建另一辆汽车
car3 = Car("Ford", "Mustang")

# 显示更新后的车辆总数
Car.display_total_cars()  # 输出: Total cars of Car: 3
```

### 6. 静态方法

定义：使用装饰器`@staticmethod`。参数随意，没有`self`和`cls`参数，但是方法体中不能使用类或实例的任何属性和方法；

调用：类对象或实例对象都可以调用。

```python
class Cal():

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def mul(x,y):
        return x*y

cal=Cal()
print(cal.add(1, 4))
or
print(Cal.add(3,4))
```

### 7. 案例练习

#### 案例1：游戏案例

函数版本：

```python
hero = {
    "name": "yuan",
    "health": 1000,
    "gold": 100,
    "defense": 10,
    "attack": 90,
    "level": 1,
    "weapon_list": []
}

# 测试攻击敌人
enemy = {
    "name": "alex",
    "health": 500,
    "defense": 5,
    "attack": 50,
    "gold": 100,
    "level": 1,
    "weapon_list": []
}


def attack_enemy(player, enemy):
    damage = player["attack"] - enemy["defense"]
    if damage > 0:
        enemy["health"] -= damage
        print(f"{player['name']}成功攻击了敌人{enemy['name']}，造成了{damage}点伤害。")
    else:
        print(f"{player['name']}的攻击被敌人防御了。")


def buy_weapon(player, weapon):
    player["weapon_list"].append(weapon)
    print(f"{player['name']}购买装备{weapon}!")


def level_up(player):
    player["level"] += 1
    player["gold"] += 100
    print(f"{player['name']}升级了，奖励金币100！")


buy_weapon(hero, "屠龙刀")
attack_enemy(hero, enemy)
level_up(hero)

```

面向对象版本：

```python
class Weapon:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def upgrade(self):
        self.attack += 50
        self.defense += 50
        print(f"{self.name}的防御力增加了50点。")
        print(f"{self.name}的防御力增加了50点。")


class Player:

    def __init__(self, name, health=100, gold=100, defense=100, attack=100, level=1, weapon_list=[]):
        self.name = name
        self.health = health
        self.gold = gold
        self.defense = defense
        self.attack = attack
        self.level = level
        self.weapon_list = weapon_list

    def attack_enemy(self, enemy, weapon_index=None):
        if weapon_index is None:
            damage = self.attack - enemy.defense
        else:
            damage = self.weapon_list[weapon_index].attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
            print(f"{self.name}成功攻击了敌人{enemy.name}，造成了{damage}点伤害。")
        else:
            print(f"{self.name}的攻击被敌人防御了。")

    def buy_weapon(self, weapon):
        self.weapon_list.append(weapon)
        print(f"{self.name}购买装备{weapon.name}!")

    def level_up(self):
        self.level += 1
        self.gold += 100
        print(f"{self.name}升级了，奖励金币100！")


p1 = Player("YUAN")
p2 = Player("ALEX")

p1.attack_enemy(p2)
w1 = Weapon("屠龙刀", 1000, 300)
p1.buy_weapon(w1)
p1.attack_enemy(p2, 0)

```

#### 案例2：客户关系管理系统【面向对象版本】

```python
customers = [
    {
        "name": "John Smith",
        "age": 35,
        "contact": "johnsmith@example.com"
    },
    {
        "name": "Jane Doe",
        "age": 28,
        "contact": "janedoe@example.com"
    },
    {
        "name": "Michael Johnson",
        "age": 42,
        "contact": "michaeljohnson@example.com"
    }
]


def add_customer():
    print("添加客户")


def delete_customer():
    print("删除客户")


def update_customer():
    print("修改客户")


def query_customer():
    print("查询客户")


class CustomersManager:
    customers = [
        {
            "name": "John Smith",
            "age": 35,
            "contact": "johnsmith@example.com"
        },
        {
            "name": "Jane Doe",
            "age": 28,
            "contact": "janedoe@example.com"
        },
        {
            "name": "Michael Johnson",
            "age": 42,
            "contact": "michaeljohnson@example.com"
        }
    ]

    def add_customer(self):
        print("添加客户")

    def delete_customer(self):
        print("删除客户")

    def update_customer(self):
        print("修改客户")

    def query_customer(self):
        print("查询客户")


cm = CustomersManager()
cm.add_customer()
cm.delete_customer()
cm.update_customer()
cm.query_customer()

```

### 今日作业

1. 创建一个名为 `Circle` 的类，并为其添加计算面积（area）、周长（circumference）等方法。

2. 人狗大战

   * 人类（`Person` 类）：
     - 属性：姓名（`name`）和健康值（`health`）。
     - 方法：
       - `kick_dog(dog)`：踢狗的方法，接受一个狗对象作为参数。在踢狗时输出踢狗的信息，同时减少狗对象的健康值。
       - `decrease_health(amount)`：减少健康值的方法，接受一个数值 `amount` 作为参数，将人的健康值减少该数值。
   * 狗类（`Dog` 类）：
     * 属性：姓名（`name`）和健康值（`health`）。
     * 方法：
       - `bite(person)`：咬人的方法，接受一个人对象作为参数。在咬人时输出咬人的信息，同时减少人对象的健康值。
       - `decrease_health(amount)`：减少健康值的方法，接受一个数值 `amount` 作为参数，将狗的健康值减少该数值。
   * 操作
     - 人踢狗时，输出踢狗的信息，并减少狗的健康值。
     - 狗咬人时，输出咬人的信息，并减少人的健康值。
     - 最后，输出人和狗的健康值，以验证掉血值的效果。

3. 创建一个名为 `BankAccount` 的类，具有以下特征：

   - 属性：`account_number`（账号）、`balance`（余额）
   - 方法：`deposit(amount)`，用于向账户存款；`withdraw(amount)`，用于从账户取款；`get_balance()`，用于获取账户余额。
   - 操作：实例化对象，存钱和取钱

4. 题目：书籍管理

   要求：

   1. 创建一个名为 `Book` 的类，具有属性 `title`、`author` 和 `publication_year`。
   2. 创建一个类属性 `book_list` 用于存储书籍对象，一个类属性book_count`存储书籍个数。
   3. 每实例化一本书籍对象，自动添加到`book_list`,并且`book_count`自加一操作
   4. 构建一个类方法 `show_books`，输出每本书籍的信息（标题、作者和出版年份）

## Day12：面向对象进阶

![截屏2024-02-25 18.34.58](./assets/%E6%88%AA%E5%B1%8F2024-02-25%2018.34.58-8857340.png)

### 1. 三大特性之继承

面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。通过继承创建的新类称为**子类**或**派生类**，被继承的类称为**基类**、**父类**或**超类**。

```python
class 派生类名(基类名)
    ...
```

#### 【1】继承的基本使用

继承是使用已存在的类的定义作为基础建立新类的技术，新类的定义可以增加新的数据或新的功能，也可以用父类的功能，但不能选择性地继承父类。通过使用继承我们能够非常方便地复用以前的代码，能够大大的提高开发的效率。

实际上继承者是被继承者的特殊化，它除了拥有被继承者的特性外，还拥有自己独有得特性。例如猫有抓老鼠、爬树等其他动物没有的特性。同时在继承关系中，继承者完全可以替换被继承者，反之则不可以，例如我们可以说猫是动物，但不能说动物是猫就是这个道理，其实对于这个我们将其称之为“向上转型”。

诚然，继承定义了类如何相互关联，共享特性。对于若干个相同或者相识的类，我们可以抽象出他们共有的行为或者属相并将其定义成一个父类或者超类，然后用这些类继承该父类，他们不仅可以拥有父类的属性、方法还可以定义自己独有的属性或者方法。

同时在使用继承时需要记住三句话：

> 1、子类拥有父类非私有化的属性和方法。
>
> 2、子类可以拥有自己属性和方法，即子类可以对父类进行扩展。
>
> 3、子类可以用自己的方式实现父类的方法。（下面会介绍）。

```python
# 无继承方式

class Dog:

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

    def swimming(self):
        print("swimming...")

class Cat:

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

    def climb_tree(self):
        print("climb_tree...")


# 继承方式

class Animal:

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")


class Dog(Animal):

    def swimming(self):
        print("toshetou...")

class Cat(Animal):

    def climb_tree(self):
        print("climb_tree...")

        
alex = Dog()
alex.run()
```

#### 【2】重写父类方法和调用父类方法

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(":::", self.name)
        print("基类sleep...")


class Emp(Person):

    # def __init__(self,name,age,dep):
    #      self.name = name
    #      self.age = age
    #      self.dep = dep

    def __init__(self, name, age, dep):
        # Person.__init__(self,name,age)
        super().__init__(name, age)
        self.dep = dep

    def sleep(self):
        # print("子类sleep...")
        # 调用父类方法
        # 方式1 ：父类对象调用 父类对象.方法（self,其他参数）
        # Person.sleep(self)
        # 方式2： super关键字 super().方法（参数）
        super().sleep()


yuan = Emp("yuan", 18, "教学部")
yuan.sleep()
print(yuan.dep)


# 测试题：

class Base:
    def __init__(self):
        self.func()
    def func(self):
        print('in base')

class Son(Base):
    def func(self):
        print('in son')

s = Son()
```

#### 【3】多重继承

如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：

```python
class SubClassName (ParentClass1[, ParentClass2, ...]):
    ...
```

多继承有什么意义呢？还拿上面的例子来说，蝙蝠和鹰都可以飞，飞的功能就重复定义了。

```python
class Animal:

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

class Eagle(Animal):

    def fly(self):
        print("fly...")

class Bat(Animal):

    def fly(self):
        print("fly...")
```

有同学肯定想那就放到父类Animal中，可是那样的话其他不会飞的动物还怎么继承Animal呢？所以，这时候多重继承就发挥功能了：

```python
class Fly:
    def fly(self):
        print("fly...")
 
class Eagle(Animal,Fly):
    pass
 
class Bat(Animal,Fly):
    pass
```

#### 【4】内置函数补充

##### （1） `type` 和`isinstance`方法

```python
class Animal:

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")


class Dog(Animal):
    def swim(self):
        print("swimming...")

alex = Dog()
mjj = Dog()

print(isinstance(alex,Dog))
print(isinstance(alex,Animal))
print(type(alex))
```

##### （2）`dir()`方法和`__dict__`属性

`dir(obj)`可以获得对象的所有属性（包含方法）列表, 而`obj.__dict__`对象的自定义属性字典

注意事项：

1. `dir(obj)`获取的属性列表中，**方法也认为属性的一种**。返回的是list
2. `obj.__dict__`只能获取自己自定义的属性，系统内置属性无法获取。返回是`dict`

```python
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def test(self):
        pass


yuan = Student("yuan", 100)
print("获取所有的属性列表")
print(dir(yuan))

print("获取自定义属性字段")
print(yuan.__dict__)
```

其中，类似`__xx__`的属性和方法都是有特殊用途的。如果调用`len()`函数视图获取一个对象的长度，其实在`len()`函数内部会自动去调用该对象的`__len__()`方法

### 2. 三大特性之封装

封装是指隐藏对象的属性和实现细节，仅对外提供公共访问方式。

我们程序设计追求“高内聚，低耦合”

> - 高内聚：类的内部数据操作细节自己完成，不允许外部干涉
> - 低耦合：仅对外暴露少量的方法用于使用。

隐藏对象内部的复杂性，只对外公开简单的接口。便于外界调用，从而提高系统的可扩展性、可维护性。通俗的说，把该隐藏的隐藏起来，该暴露的暴露岀来。这就是封装性的设计思想。

#### 【1】私有属性

在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的`name`、`score`属性：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

alvin = Student("alvin",66)
yuan = Student("yuan",88)

alvin.score=100
print(alvin.score)
```

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score


alvin = Student("alvin",66)
yuan = Student("yuan",88)

print(alvin.__score)
```

改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问`实例变量.__name`和`实例变量.__score`。这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。但是如果外部代码要获取name和score怎么办？可以给Student类增加`get_score`这样的方法：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

alvin=Student("alvin",66)
yuan=Student("yuan",88)

print(alvin.get_score())
```

如果又要允许外部代码修改score怎么办？可以再给Student类增加`set_score`方法：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score = score

alvin = Student("alvin",12)
print(alvin.get_score())
alvin.set_score(100)
print(alvin.get_score())
```

你也许会问，原先那种直接通过`alvin.score = 100`也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以设置值时做其他操作，比如记录操作日志，对参数做检查，避免传入无效的参数等等：

```python
class Student(object):
    ...
    def set_score(self,score):
        if isinstance(score,int) and 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('error!')
```

> **注意**
>
> 1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：`_类名__属性`，然后就可以访问了
>
> 2、变形的过程只在类的内部生效,在定义后的赋值操作，不会变形

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

yuan=Student("yuan",66)
print(yuan.__dict__)
yuan.__age=18
print(yuan.__dict__)
```

案例

```python
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

class Student(Person):

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score=score

yuan=Student("yuan",66)
print(yuan.__dict__)
print(yuan.get_score())
```

> 子类无法直接访问父类的私有属性。子类只能在自己的方法中访问和修改自己定义的私有属性，无法直接访问父类的私有属性。

单下划线、双下划线、头尾双下划线说明：

- `__foo__`: 定义的是特殊方法，一般是系统定义名字 ，类似 `__init__()` 之类的。
- `__foo`: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
- `_foo`: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问。（约定成俗，不限语法）

#### 【2】私有方法

私有方法是指只能在类的内部访问和调用的方法，无法在类的外部直接访问或调用。

```python
class AirConditioner:
    def __init__(self):
        # 初始化空调
        pass

    def cool(self, temperature):
        # 对外制冷功能接口方法
        self.__turn_on_compressor()
        self.__set_temperature(temperature)
        self.__blow_cold_air()
        self.__turn_off_compressor()

    def __turn_on_compressor(self):
        # 打开压缩机（私有方法）
        pass

    def __set_temperature(self, temperature):
        # 设置温度（私有方法）
        pass

    def __blow_cold_air(self):
        # 吹冷气（私有方法）
        pass

    def __turn_off_compressor(self):
        # 关闭压缩机（私有方法）
        pass

```

在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的:

```python
class Base:
    def foo(self):
        print("foo from Base")

    def test(self):
        self.foo()

class Son(Base):
    def foo(self):
        print("foo from Son")

s=Son()
s.test()


class Base:
    def __foo(self):
        print("foo from Base")

    def test(self):
        self.__foo()

class Son(Base):
    def __foo(self):
        print("foo from Son")

s=Son()
s.test()
```

#### 【3】property属性操作

##### （1）property属性装饰器

使用接口函数获取修改数据 和 使用点方法设置数据相比， 点方法使用更方便，我们有什么方法达到 既能使用点方法，同时又能让点方法直接调用到我们的接口了，答案就是property属性装饰器：

```python
class Student(object):

    def __init__(self,name,score,sex):
        self.__name = name
        self.__score = score
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) > 1 :
            self.__name = name
        else:
            print("name的长度必须要大于1个长度")

    @property
    def score(self):
        return self.__score

    # @score.setter
    # def score(self, score):
    #     if score > 0 and score < 100:
    #         self.__score = score
    #     else:
    #         print("输入错误！")


yuan = Student('yuan',18,'male')

yuan.name = '苑昊'  #  调用了@name.setter

print(yuan.name)    #  调用了@property的name函数

yuan.score = 199    # @score.setter
print(yuan.score)   # @property的score方法 
```

##### （2）property属性函数

python提供了更加人性化的操作，可以通过限制方式完成只读、只写、读写、删除等各种操作

```python
class Person:
    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    def __del_name(self):
        del self.__name
    # property()中定义了读取、赋值、删除的操作
    # name = property(__get_name, __set_name, __del_name)
    name = property(__get_name, __set_name)

yuan = Person("yuan")

print(yuan.name)   # 合法：调用__get_name
yuan.name = "苑昊"  # 合法：调用__set_name
print(yuan.name)

# property中没有添加__del_name函数，所以不能删除指定的属性
del p.name  # 错误：AttributeError: can't delete Attribute
```

`@property`广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

### 3. 三大特性之多态

#### 【1】java多态

在java里，多态是同一个对象具有不同表现形式或形态的能力，即对象多种表现形式的体现，就是指程序中定义的引用变量所指向的具体类型和通过该引用变量发出的方法调用在编程时并不确定，而是在程序运行期间才确定，即一个引用变量倒底会指向哪个类的实例对象，该引用变量发出的方法调用到底是哪个类中实现的方法，必须在由程序运行期间才能决定。

如下图所示：使用手机扫描二维码支付时，二维码并不知道客户是通过何种方式进行支付，只有通过二维码后才能判断是走哪种支付方式执行对应流程。

![img](./assets/pay.png)

```java
// 支付抽象类或者接口
 

public class Pay {
    public String pay() {
        System.out.println("do nothing!")
        return "success"
    }
}
// 支付宝支付
 
public class AliPay extends Pay {
    @Override
    public String pay() {
        System.out.println("支付宝pay");
        return "success";
    }
}
// 微信支付
 
public class WeixinPay extends Pay {
    @Override
    public String pay() {
        System.out.println("微信Pay");
        return "success";
    }
}

 // 银联支付
 
public class YinlianPay extends Pay {
    @Override
    public String pay() {
        System.out.println("银联支付");
        return "success";
    }
}

// 测试支付
public static void main(String[] args) {
    
    // 测试支付宝支付多态应用   
    Pay pay = new AliPay();
    pay.pay();
    // 测试微信支付多态应用    
    pay = new WeixinPay();
    pay.pay();
   // 测试银联支付多态应用  
    pay = new YinlianPay();
    pay.pay();
}

// 输出结果如下：

支付宝pay
微信Pay
银联支付
```

多态存在的三个必要条件：

> - 继承
> - 重写
> - 父类引用指向子类对象

比如：

```java
Pay pay = new AliPay()
```

当使用多态方式调用方法时，首先检查父类中是否有该方法，如果没有，则编译错误；如果有，再去调用子类的同名方法。

#### 【2】鸭子模型

鸭子模型（Duck typing）是一种动态类型系统中的编程风格或理念，它强调对象的行为比其具体类型更重要。根据鸭子模型的说法，如果一个对象具有与鸭子相似的行为，那么它就可以被视为鸭子。

鸭子模型源自于一个简单的说法：“如果它看起来像鸭子，叫起来像鸭子，那么它就是鸭子。”在编程中，这意味着我们更关注对象是否具有特定的方法或属性，而不是关注对象的具体类型。

通过鸭子模型，我们可以编写更灵活、通用的代码，而不需要显式地指定特定的类型或继承特定的接口。只要对象具有所需的方法和属性，就可以在代码中使用它们，无论对象的具体类型是什么。

```python

class AliPay:

    def pay(self):      
        print('通过支付宝消费')

class WeChatPay:

    def pay(self):      
        print('通过微信消费')

class Order(object):

    def account(self,pay_obj):
        pay_obj.pay()


pay1 = WeChatPay("yuan", 100)
pay2 = AliPay("alvin", 200)

order = Order()
order.account(pay1)
order.account(pay2)
```

### 4. 反射

反射这个术语在很多语言中都存在，并且存在大量的运用，今天我们说说什么是反射，反射主要是指程序可以访问、检测和修改它本身状态或行为的一种能力。

在Python中，反射是指在运行时通过名称字符串来访问、检查和操作对象的属性和方法的能力。Python提供了一些内置函数和特殊方法，使得可以动态地获取对象的信息并执行相关操作。

Python中的反射主要有下面几个方法：

```python
# 1. 判断对象中有没有一个name字符串对应的方法或属性
hasattr(object,name)
# 2. 获取对象name字符串属性的值，如果不存在返回default的值
getattr(object, name, default=None)
# 3. 设置对象的key属性为value值，等同于object.key = value
setattr(object, key, value)
# 4. 删除对象的name字符串属性
delattr(object, name)
```

应用1：

```python
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

yuan=Person("yuan",22,"male")
print(yuan.name)
print(yuan.age)
print(yuan.gender)
while 1:
    # 由用户选择查看yuan的哪一个信息
    attr = input(">>>")
    if hasattr(yuan, attr):
        val = getattr(yuan, attr)
        print(val)
    else:
        val=input("yuan 没有你该属性信息！，请设置该属性值>>>")
        setattr(yuan,attr,val)
```

应用2：

```python
class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self):
        print("添加客户")

    def del_customer(self):
        print("删除客户")

    def update_customer(self):
        print("修改客户")

    def query_one_customer(self):
        print("查询一个客户")

    def show_all_customers(self):
        print("查询所有客户")


class CustomerSystem:
    def __init__(self):
        self.cm = CustomerManager()

    def run(self):
        print("""
           1. 添加客户
           2. 删除客户
           3. 修改客户
           4. 查询一个客户
           5. 查询所有客户
           6. 保存
           7. 退出
        """)

        while True:
            choice = input("请输入您的选择:")

            if choice == "6":
                self.save()
                continue
            elif choice == "7":
                print("程序退出！")
                break

            try:
                method_name = "action_" + choice
                method = getattr(self, method_name)
                method()
            except AttributeError:
                print("无效的选择")

    def save(self):
        print("保存数据")

    def action_1(self):
        self.cm.add_customer()

    def action_2(self):
        self.cm.del_customer()

    def action_3(self):
        self.cm.update_customer()

    def action_4(self):
        self.cm.query_one_customer()

    def action_5(self):
        self.cm.show_all_customers()


cs = CustomerSystem()
cs.run()
```

### 5. 魔法方法

Python 类里有一种方法，叫做魔法方法（special method）。Python 的类里提供的，两个下划线开始，两个下划线结束的方法，就是魔法方法，魔法方法在特定行为下就会被激活，自动执行。

#### 【1】`__new__()`方法

`__new__()` 方法是在 Python 中定义一个类的时候可以定义的一个特殊方法。它被用来创建一个类的新实例（对象）。

在 Python 中，创建一个新的实例一般是通过调用类的构造函数 `__init__()` 来完成的。然而，`类名()`创建对象时，在自动执行` __init__()`方法前，会先执行 `object.__new__`方法，在内存中开辟对象空间并返回该对象。然后，Python 才会调用 `__init__()` 方法来对这个新实例进行初始化。

```python
class Person(object):
    # 其中，cls参数表示类本身，*args 和 **kwargs参数用于接收传递给构造函数的参数。
    def __new__(cls, *args, **kwargs):
        print("__new__方法执行")
        # return object.__new__(cls)

    def __init__(self, name, age):
        print("__init__方法执行")
        self.name = name
        self.age = age


yuan = Person("yuan", 23)
```

> `_new__()` 方法的主要作用是创建实例对象，它可以被用来控制实例的创建过程。相比之下，`__init__()` 方法主要用于初始化实例对象。

`__new__()` 方法在设计模式中常常与单例模式结合使用，用于创建一个类的唯一实例。单例模式是一种创建型设计模式，它确保一个类只有一个实例，并提供一个全局访问点来获取该实例。

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# 创建实例
obj1 = Singleton()
obj2 = Singleton()

# 检查是否为同一个实例
print(obj1 is obj2)  # 输出: True
```

#### 【2】`__str__`方法

改变对象的字符串显示。可以理解为使用print函数打印一个对象时，会自动调用对象的`__str__`方法

```python
class Person(object):

    def __init__(self, name, age):
        print("__init__方法执行")
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

yuan = Person("yuan", 23)
print(yuan)

# 案例2
class Book(object):

    def __init__(self, title, publisher, price):
        self.title = title
        self.publisher = publisher
        self.price = price


book01 = Book("金瓶梅", "苹果出版社", 699)
print(book01)
```

#### 【3】`__eq__` 方法

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, obj):
        return self.name == obj.name


yuan = Person("yuan", 23)
alvin = Person("alvin", 23)
print(yuan == alvin)
```

> 1. `__eq__(self, other)`: 判断对象是否相等，通过 `==` 运算符调用。
> 2. `__lt__(self, other)`: 判断对象是否小于另一个对象，通过 `<` 运算符调用。
> 3. `__gt__(self, other)`: 判断对象是否大于另一个对象，通过 `>` 运算符调用。
> 4. `__add__(self, other)`: 对象的加法操作，通过 `+` 运算符调用

#### 【4】`__len__`方法

当定义一个自定义的容器类时，可以使用 `__len__()` 方法来返回容器对象中元素的数量。下面是一个示例，演示了如何在自定义列表类中实现 `__len__()` 方法：

```python
class Cache01:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)

# 创建自定义列表对象
cache = Cache01()

# 获取列表的长度
print(len(cache)) 


class Cache02:
    def __init__(self):
        self.data = {}
        
    def __len__(self):
        return len(self.data)

    def add(self, key, value):
        self.data[key] = value

    def remove(self, key):
        del self.data[key]

```

**一定会有同学问，Yuan老师，为什么要封装这个类，直接使用self.data = {}不就完了吗？**

当我们封装一个类时，我们将相关的数据和操作放在一个包裹（类）中，就像把一些东西放进一个盒子里一样。这个盒子提供了一种保护和管理数据的方式，同时也定义了外部与内部之间的交互方式。

为什么要这样做呢？想象一下，如果我们直接将数据存储在类之外的变量中，其他代码可以直接访问和修改它。这可能导致数据被误用或篡改，造成不可预测的结果。而通过封装，我们可以将数据放在类的内部，并提供一些方法（接口）来访问和修改数据。这就像将数据放进盒子里，并用盒子上的门来控制对数据的访问。

这种封装的好处是什么呢？首先，它提供了一种信息隐藏的机制。外部代码只能通过类提供的方法来访问数据，无法直接触及数据本身。这样可以保护数据的完整性和一致性，防止不恰当的访问和修改。其次，封装使得代码更加模块化和可重用。我们可以将相关的数据和操作组织在一个类中，成为一个功能完整的单元，方便调用和扩展。

总而言之，封装就像把数据放进一个盒子里，通过提供方法来控制对数据的访问。这样做可以保护数据，提高代码的可读性和可维护性，并促进代码的模块化和重用。

#### 【5】`__item__`系列

```python
class Cache:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __contains__(self, key):
        return key in self.data
      
```

在上述例子中，我们创建了一个名为 `Cache` 的自定义类，并实现了 `__getitem__`、`__setitem__`、`__delitem__` 和 `__contains__` 这些特殊方法。

使用这个自定义的缓存类，我们可以像操作字典一样操作缓存数据，例如：

```python
cache = Cache()

# 存储数据
cache['key1'] = 'value1'
cache['key2'] = 'value2'

# 获取数据
print(cache['key1'])  # 输出: 'value1'
print(cache['key2'])  # 输出: 'value2'

# 检查键是否存在
print('key1' in cache)  # 输出: True

# 删除数据
del cache['key1']

# 检查键是否存在
print('key1' in cache)  # 输出: False
```

通过实现特殊方法，我们可以使用类似于==**字典的语法来访问和操作缓存对象**==。这样，我们可以更方便地存储、获取和删除缓存数据，同时也可以使用其他字典操作，如检查键是否存在。

#### 【6】`__attr__`系列

```python
class Cache:
    def __init__(self):
        self.__data = {}

    def __setattr__(self, name, value):
        self.__data[name] = value

    def __getattr__(self, name):
        if name in self.__data:
            return self.__data[name]
        else:
            raise AttributeError(f"'Cache' object has no attribute '{name}'")

    def __delattr__(self, name):
        if name in self.__data:
            del self.__data[name]
        else:
            raise AttributeError(f"'Cache' object has no attribute '{name}'")

    def __contains__(self, name):
        return name in self.__data
```

在这个示例中，我们使用 `__setattr__` 方法来设置属性，将属性存储在私有属性 `__data` 中。当我们尝试设置属性时，`__setattr__` 方法会被自动调用，并将属性存储到私有字典中。

而在 `__getattr__` 方法中，我们实现了对属性的访问。如果属性存在于私有字典 `__data` 中，它将返回属性的值。如果属性不存在，则会引发 `AttributeError` 异常。

类似地，我们还实现了 `__delattr__` 方法来删除属性。如果属性存在于私有字典 `__data` 中，它将被删除。如果属性不存在，则会引发 `AttributeError` 异常。

最后，我们还重写了 `__contains__` 方法，以实现在缓存中检查属性是否存在的功能。

使用这个经过修改的缓存类，我们可以使用类似于==**属性操作的语法：对象.属性**==来访问和操作缓存对象。

```python
class Cache(object):

    def __init__(self):
        self.__dict__["data"] = {}

    def __setattr__(self, key, value):
        # 有效控制，判断，监控，日志
        self.__dict__["data"][key] = value

    def __getattr__(self, key):
        if key in self.__dict__["data"]:
            return self.__dict__["data"][key]
        else:
            raise AttributeError(f"'Cache' object has no attribute '{key}'")

    def __delattr__(self, key):
        if key in self.__dict__["data"]:
            del self.__dict__["data"][key]
        else:
            raise AttributeError(f"'Cache' object has no attribute '{key}'")

    def __contains__(self, name):
        return name in self.__dict__["data"]


cache = Cache()
cache.name = "yuan"
cache.age = 19
print(cache.name)
del cache.age
print("age" in cache)
# print(cache.age)
```

### 6. 异常机制

异常机制是一种在程序运行过程中处理错误和异常情况的机制。当程序执行过程中发生异常时，会中断正常的执行流程，并转而执行异常处理的代码。这可以帮助我们优雅地处理错误，保证程序的稳定性和可靠性。

在Python中，异常以不同的类型表示，每个异常类型对应不同的错误或异常情况。当发生异常时，可以使用 `try-except` 语句来捕获并处理异常。`try` 块中的代码被监视，如果发生异常，则会跳转到对应的 `except` 块，执行异常处理的代码。

#### 【1】Error类型

在Python中，常见的错误关键字（Exception Keywords）指的是一些常见的异常类型，它们用于表示不同的错误或异常情况。以下是一些常见的错误关键字及其对应的异常类型：

1. `SyntaxError`：语法错误，通常是由于代码书写不正确而引发的异常。
2. `NameError`：名称错误，当尝试访问一个未定义的变量或名称时引发的异常。
3. `IndexError`：索引错误，当访问列表、元组或字符串等序列类型时使用了无效的索引引发的异常。
4. `KeyError`：键错误，当尝试使用字典中不存在的键引发的异常。
5. `ValueError`：值错误，当函数接收到一个正确类型但是不合法的值时引发的异常。
6. `FileNotFoundError`：文件未找到错误，当尝试打开或操作不存在的文件时引发的异常。
7. `ImportError`：导入错误，当导入模块失败时引发的异常，可能是因为找不到模块或模块中缺少所需的内容。
8. `ZeroDivisionError`：零除错误，当除法或取模运算的除数为零时引发的异常。
9. `AttributeError`：属性错误，当尝试访问对象不存在的属性或方法时引发的异常。
10. `IOError`：输入/输出错误，当发生与输入和输出操作相关的错误时引发的异常。例如，尝试读取不存在的文件或在写入文件时磁盘已满。

#### 【2】基本语法

异常的基本结构：`try except`

```python 
# (1) 通用异常
try:
    pass  # 正常执行语句
except Exception as ex:
    pass  # 异常处理语句

# (2) 指定异常
try:
     pass  # 正常执行语句
except <异常名>:
     pass  # 异常处理语句
        
# (3) 统一处理多个异常
try:
     pass  # 正常执行语句
except (<异常名1>, <异常名2>, ...):
      pass  # 异常处理语句
    
# (4) 分别处理不同的异常 
try:
     pass  # 正常执行语句
except <异常名1>:
      pass  # 异常处理语句1
except <异常名2>:
      pass  # 异常处理语句2
except <异常名3>:
      pass  # 异常处理语句3
  
# (5) 完整语法   
try:
    pass  # 正常执行语句
except Exception as e:
    pass  # 异常处理语句
else:
    pass # 测试代码没有发生异常 
finally:
    pass  # 无论是否发生异常一定要执行的语句,比如关闭文件，数据库或者socket
    
```

> 机制说明：
>
> - 首先，执行try子句（在关键字try和关键字except之间的语句）
> - 如果没有异常发生，忽略except子句，try子句执行后结束。
> - 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常那么对应的except子句将被执行。
> - 在Python的异常中，有一个通用异常：`Exception`，它可以捕获任意异常。

####  【3】raise

很多时候，我们需要主动抛出一个异常。Python内置了一个关键字`raise`，可以主动触发异常。

`raise`可以抛出自定义异常，我们已将在前面看到了python内置的一些常见的异常类型。大多数情况下，内置异常已经够用了。但是有时候你还是需要自定义一些异常：自定义异常应该继承`Exception`类，直接继承或者间接继承都可以，例如:

```python 
class CouponError01(Exception):
    def __init__(self):
        print("优惠券错误类型1")


class CouponError02(Exception):
    def __init__(self):
        print("优惠券错误类型2")


class CouponError03(Exception):
    def __init__(self):
        print("优惠券错误类型3")


try:
    print("start")
    print("...")
    x = input(">>>")
    if x == "1":
        raise CouponError01
    elif x == "2":
        raise CouponError02
    elif x == "3":
        raise CouponError03

except CouponError01:
    print("优惠券错误类型1")
except CouponError02:
    print("优惠券错误类型2")
except CouponError03:
    print("优惠券错误类型3")

```

### 今日作业

1. 关于继承与方法重写

```python
class A:  
    def get(self):  
        self.say()

    def say(self):  
        print('apple')

class B(A):  
    def say(self):  
        print('banana')

b = B()  
b.get()   # 输出结果为?
```

2. 将以下代码填写完整

```python
class A:
    def foo(self, x):
        print('executing class_foo(%s, %s)' % (self, x))

    @classmethod
    def class_foo(cls, x):
        print('executing class_foo(%s, %s)' % (cls, x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % (x))

a = A()
# 调用 foo 函数,参数传入 1
# ?
# 调用 class_foo 函数,参数传入 1
# ?
# 调用 static_foo 函数,参数传入 1
# ?
```

3. 创建一个名为 `Circle` 的类，具有 `radius` 属性。使用 `@property` 装饰器创建一个名为 `diameter` 的属性，用于计算圆的直径，并创建一个名为 `circumference` 的属性，用于计算圆的周长。

4. 创建一个名为 `Product` 的类，具有 `name` 和 `price` 属性。实现 `__str__` 方法，使其返回格式为 "Product: name - price" 的字符串表示。同时实现 `__len__` 方法，使其返回产品名称的长度。
5. 实现一个FTP类，`FTP`类包含了`get`和`post`两个方法，分别用于下载和上传文件。`run`方法首先引导用户输入命令（`get`或`post`），然后根据用户输入的命令和文件名，使用反射机制执行对应的类方法。

```python
class FTP:
    def get(self, filename):
        print(f"Downloading file: {filename}")

    def post(self, filename):
        print(f"Uploading file: {filename}")

    def run(self):
        command = input("请输入命令（get 或 post）：")
        if command == "get" or command == "post":
            try:
                method = getattr(self, command)
                filename = input("请输入文件名：")
                method(filename)
            except AttributeError:
                print("指定的方法不存在。")
        else:
            print("无效的命令。")


ftp = FTP()
ftp.run()
```

6. 一个实际的场景案例涉及一个银行账户类（`BankAccount`），其中使用私有属性和私有方法来确保账户余额的安全和一致性。

   `BankAccount`类使用私有属性 `__account_number` 和 `__balance` 来存储账户号码和余额。这样的设计使得外部无法直接访问和修改这些属性，从而确保了账户信息的安全性。

7. `__init__()` 和 `__new__()` 方法有什么区别
8. 双下划线和单下划线的区别?

9. 设计一个名为 `Dictionary` 的类，用于表示自定义的字典。该类具有以下要求：

- 初始化方法：类的初始化方法不带任何参数，创建一个空的字典对象。
- `__getitem__` 方法：实现索引操作，通过键访问字典中的值。要求传入的键必须是字符串类型，如果键不存在，则返回 `None`。
- `__setitem__` 方法：实现赋值操作，通过键设置字典中的键值对。要求传入的键必须是字符串类型。
- `__delitem__` 方法：实现删除操作，通过键删除字典中的键值对。要求传入的键必须是字符串类型，如果键不存在，则抛出 `KeyError` 异常。

```python
class Dictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data.get(key)
        else:
            raise TypeError("Key must be a string.")

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.data[key] = value
        else:
            raise TypeError("Key must be a string.")

    def __delitem__(self, key):
        if isinstance(key, str):
            if key in self.data:
                del self.data[key]
            else:
                raise KeyError(f"Key '{key}' does not exist in the dictionary.")
        else:
            raise TypeError("Key must be a string.")


dictionary = Dictionary()
dictionary['name'] = 'John'
dictionary['age'] = 30
print(dictionary['name'])  # 输出: John
del dictionary['age']
print(dictionary.get('age'))  # 输出: None
```

10. 电商项目

在电商业务场景中，需要设计商品类、购物车类和用户类。具体描述如下：

* 商品类（Product）：每个商品对象应具有以下属性和方法：

  * 属性：名称（name）、价格（price）、库存数量（stock）
  * 方法：获取商品名称（get_name()）、获取商品价格（get_price()）、获取商品库存数量（get_stock()）、更新商品库存数量（update_stock(quantity)）

* 普通商品类（RegularProduct）：继承自商品类，每个普通商品对象应具有以下特有的方法

  * 方法：购买商品（buy_product(quantity)）：根据购买的数量减少商品库存量；如果库存不足，则输出"库存不足，无法购买该商品"；否则，减少库存数量。
  * 方法：添加到购物车（add_to_cart(cart, quantity)）：将商品添加到指定购物车对象中，同时指定购买的数量。

* 折扣商品类（DiscountProduct）：继承自商品类，每个折扣商品对象应具有以下特有的属性和方法：

  * 属性：折扣（discount）
  * 方法：购买商品（buy_product(quantity)）：根据购买的数量减少商品库存量；如果库存不足，则输出"库存不足，无法购买该商品"；否则，减少库存数量。
  * 方法：添加到购物车（add_to_cart(cart, quantity)）：将商品添加到指定购物车对象中，同时指定购买的数量。
* 购物车类（Cart）：每个购物车对象应具有以下属性和方法：

  * 属性：商品项（items）,提示：考虑用字典进行存储

  * 方法：添加商品（add_item(product, quantity)）：将指定数量的商品添加到购物车中；如果商品已存在于购物车，则增加该商品的数量；否则，添加新的商品项。

  * 方法：删除商品（remove_item(product, quantity)）：从购物车中删除指定数量的商品；如果商品数量不足以删除，则直接删除该商品项；否则，减少商品数量。

  * 方法：查看购物车内容（view_items()）：输出购物车中的商品项及其对应的数量。

  * 方法：清空购物车（clear()）：将购物车中的商品项清空。
* 用户类（User）：每个用户对象应具有以下属性和方法：
  * 属性：用户名（name）、购物车（cart）
  * 方法：添加商品到购物车（add_to_cart(product, quantity)）：将指定数量的商品添加到用户的购物车中。
  * 方法：查看购物车内容（view_cart()）：输出用户购物车中的商品项及其对应的数量。
  * 方法：结算订单并支付（checkout()）：根据购物车中的商品项生成订单对象，并进行支付；支付成功后，清空购物车。
* 订单类（Order）：每个订单对象应具有以下属性和方法：
  * 属性：购物车（cart）、总价（total_price）
  * 方法：计算总价（calculate_total_price()）：根据购物车中的商品项计算订单的总价。
  * 方法：支付（pay()）：执行支付逻辑，输出支付成功信息，并显示支付金额。

请使用面向对象的思想，设计并实现这些类，并编写主程序测试上述功能。请确保代码的正确性和健壮性，并合理处理各类之间的关系。

```python

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock


class RegularProduct(Product):
    pass


class DiscountProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] <= quantity:
                del self.items[product]
            else:
                self.items[product] -= quantity

    def view_items(self):
        for product, quantity in self.items.items():
            print(f"{product.get_name()} - 数量：{quantity}")

    def clear(self):
        self.items = {}


class Order:
    def __init__(self, cart):
        self.cart = cart
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.cart.items.items():
            if isinstance(product, DiscountProduct):
                total_price += product.get_price() * quantity * product.discount
            else:
                total_price += product.get_price() * quantity
        return total_price

    def pay(self):
        # 实现支付逻辑
        print(f"支付成功！支付金额：{self.total_price}")


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def view_cart(self):
        self.cart.view_items()

    def checkout(self):
        order = Order(self.cart)
        order.pay()
        self.cart.clear()


# 创建普通商品对象和折扣商品对象
regular_product = RegularProduct("iPhone 12", 6999, 100)
discount_product = DiscountProduct("Apple Watch", 1999, 50, 0.8)

# 创建用户对象
user = User("John")

# 用户添加商品到购物车，并查看购物车
user.add_to_cart(regular_product, 2)
user.add_to_cart(discount_product, 3)
user.view_cart()

# 用户结算订单并支付
user.checkout()
```

## Day13：网络编程

![截屏2024-03-31 14.25.03](./assets/%E6%88%AA%E5%B1%8F2024-03-31%2014.25.03-1866360.png)

网络编程是指在计算机网络上进行数据传输和通信的编程技术。它涉及到在不同计算机之间建立连接、发送和接收数据以及处理网络通信的各种操作。网络编程广泛应用于各种领域，包括服务器开发、Web开发、分布式系统、云计算等。

### 1. 软件架构设计

软件架构设计可以根据应用场景的不同分为客户端/服务器（Client/Server，CS）架构和浏览器/服务器（Browser/Server，BS）架构。

#### 【1】CS架构

![截屏2024-03-25 15.07.03-1350445](./assets/%E6%88%AA%E5%B1%8F2024-03-25%2015.07.03-1350445.png)

CS架构是一种常见的软件架构，它将软件系统划分为两个主要部分：客户端和服务器。客户端负责展示用户界面和处理用户输入，而服务器负责处理业务逻辑和存储数据。客户端和服务器之间通过网络进行通信，客户端发送请求给服务器，服务器进行处理并返回结果给客户端。

在CS架构中，客户端和服务器可以运行在不同的物理设备上，通过网络连接进行通信。客户端可以是桌面应用程序、移动应用程序等，而服务器可以是独立的物理服务器或云服务器。

```python
例如：你电脑的上QQ、百度网盘、钉钉、QQ音乐 等安装在电脑上的软件。

服务端：互联网公司会开发一个程序放在他们的服务器上，用于给客户端提供数据支持。
客户端：大家在电脑安装的相关程序，内部会连接服务端进行收发数据并提供 交互和展示的功能。
```

#### 【2】BS架构

BS架构是一种特殊的CS架构，其中客户端是通过浏览器访问应用程序，而服务器负责提供应用程序的逻辑和数据。在BS架构中，客户端使用浏览器作为用户界面，通过HTTP协议与服务器进行通信。

BS架构的优势在于客户端无需安装额外的软件，只需使用普通的浏览器即可访问应用程序。这使得应用程序的部署和维护更加方便，同时也提供了跨平台和跨设备的能力。

在BS架构中，服务器端主要负责业务逻辑和数据处理，而客户端主要负责展示和用户交互。服务器端可以使用不同的技术栈，如Web服务器、应用服务器、数据库服务器等。

```
例如：淘宝、京东等网站。

服务端：互联网公司开发一个网站，放在他们的服务器上。
客户端：不需要开发，用现成的浏览器即可。
```

需要注意的是，CS架构和BS架构并不是互斥的，而是根据应用场景和需求选择最适合的架构。某些应用可能需要同时使用CS和BS架构，例如在一个企业内部系统中，可以使用CS架构的桌面应用程序和BS架构的Web应用程序相结合，以满足不同的用户需求和使用场景。

### 2. 网络三要素

![截屏2024-03-25 15.18.25](./assets/%E6%88%AA%E5%B1%8F2024-03-25%2015.18.25-1351119.png)

1. **地址（Address）：** 地址用于唯一标识网络中的设备或应用程序。在网络通信中，每个设备或应用程序都有一个唯一的地址，使得数据能够准确地发送到目标位置。在Internet中，常用的地址是IP地址（Internet Protocol Address），它是一个由数字和点分隔符组成的标识符。IP地址可以用来标识主机（计算机）或网络设备。此外，还有其他类型的地址，如MAC地址（Media Access Control Address），用于在局域网中唯一标识网络接口。
2. **端口（Port）：** 端口是在网络通信中用于标识应用程序或服务的数字。每个设备或主机上的应用程序可以使用不同的端口号，以便在同一台设备上同时运行多个应用程序。端口号是一个16位的数字，范围从0到65535。其中，0到1023之间的端口号是一些著名的端口，用于特定的服务或应用程序，如HTTP的端口号是80，HTTPS的端口号是443。端口号的使用确保了数据能够正确地传递给目标应用程序或服务。
3. **协议（Protocol）：** 协议是在网络通信中规定的一组规则和约定，用于确保数据的正确传输和交换。协议定义了数据的格式、传输方式、错误处理、连接建立和断开等操作。常见的网络协议包括TCP（传输控制协议）、UDP（用户数据报协议）、IP（互联网协议）、HTTP（超文本传输协议）等。协议的使用确保了网络中的设备和应用程序之间可以相互通信和理解。

### 3. TCP协议和UDP协议

#### 【1】TCP协议

TCP（Transmission Control Protocol，传输控制协议）是一种面向连接的、可靠的、基于字节流的通信协议，数据在传输前要建立连接，传输完毕后还要断开连接。

客户端在收发数据前要使用 connect() 函数和服务器建立连接。建立连接的目的是保证IP地址、端口、物理链路等正确无误，为数据的传输开辟通道。

![img](./assets/1-151020115S23R-1353005.jpg)

> 1. 序号：Seq（Sequence Number）序号占32位，用来标识从计算机A发送到计算机B的数据包的序号，计算机发送数据时对此进行标记。
>
> 2. 确认号：Ack（Number）确认号占32位，客户端和服务器端都可以发送，Ack = Seq + 1。
>
> 3. 标志位：每个标志位占用1Bit，共有6个，分别为 URG、ACK、PSH、RST、SYN、FIN，具体含义如下：
>
>    `// URG：紧急指针（urgent pointer）有效。 `
>
>    `// ACK：确认序号有效。 `
>
>     `// PSH：接收方应该尽快将这个报文交给应用层。 `
>
>     `// RST：重置连接。 `
>
>     `// SYN：建立一个新连接。 `
>
>     `// FIN：断开一个连接。 `

TCP建立连接时要传输三个数据包，俗称三次握手（Three-way Handshaking）。可以形象的比喻为下面的对话：

> - [Shake 1] 套接字A：“大哥，你能听到我说话吗”
> - [Shake 2] 套接字B：“可以，小弟，你能听到我说话吗？”
> - [Shake 3] 套接字A：“我也能，OK！”

使用 connect() 建立连接时，客户端和服务器端会相互发送三个数据包，请看下图：

![img](./assets/1-151020132J32G-1353032.jpg)

客户端调用 socket() 创建套接字后，因为没有建立连接，所以套接字处于`CLOSED`状态；服务器端调用 listen() 函数后，套接字进入`LISTEN`状态，开始监听客户端请求。这个时候，客户端开始发起请求：

1. 当客户端调用 connect() 函数后，TCP协议会组建一个数据包，并设置 SYN 标志位，表示该数据包是用来建立同步连接的。同时生成一个随机数字 1000，填充“序号（Seq）”字段，表示该数据包的序号。完成这些工作，开始向服务器端发送数据包，客户端就进入了`SYN-SEND`状态。
2. 服务器端收到数据包，检测到已经设置了 SYN 标志位，就知道这是客户端发来的建立连接的“请求包”。服务器端也会组建一个数据包，并设置 SYN 和 ACK 标志位，SYN 表示该数据包用来建立连接，ACK 用来确认收到了刚才客户端发送的数据包。 服务器生成一个随机数 2000，填充“序号（Seq）”字段。2000 和客户端数据包没有关系。服务器将客户端数据包序号（1000）加1，得到1001，并用这个数字填充“确认号（Ack）”字段。服务器将数据包发出，进入`SYN-RECV`状态。
3. 客户端收到数据包，检测到已经设置了 SYN 和 ACK 标志位，就知道这是服务器发来的“确认包”。客户端会检测“确认号（Ack）”字段，看它的值是否为 1000+1，如果是就说明连接建立成功。接下来，客户端会继续组建数据包，并设置 ACK 标志位，表示客户端正确接收了服务器发来的“确认包”。同时，将刚才服务器发来的数据包序号（2000）加1，得到 2001，并用这个数字来填充“确认（Ack）”字段。客户端将数据包发出，进入`ESTABLISED`状态，表示连接已经成功建立。
4. 服务器端收到数据包，检测到已经设置了 ACK 标志位，就知道这是客户端发来的“确认包”。服务器会检测“确认号（Ack）”字段，看它的值是否为 2000+1，如果是就说明连接建立成功，服务器进入`ESTABLISED`状态。至此，客户端和服务器都进入了`ESTABLISED`状态，连接建立成功，接下来就可以收发数据了。

> 注意：三次握手的关键是要确认对方收到了自己的数据包，这个目标就是通过“确认号（Ack）”字段实现的。计算机会记录下自己发送的数据包序号 Seq，待收到对方的数据包后，检测“确认号（Ack）”字段，看`Ack = Seq + 1`是否成立，如果成立说明对方正确收到了自己的数据包

#### 【2】UDP协议

TCP 是面向连接的传输协议，建立连接时要经过三次握手，断开连接时要经过四次握手，中间传输数据时也要回复 ACK 包确认，多种机制保证了数据能够正确到达，不会丢失或出错。

UDP 是非连接的传输协议，没有建立连接和断开连接的过程，它只是简单地把数据丢到网络中，也不需要 ACK 包确认。

UDP 传输数据就好像我们邮寄包裹，邮寄前需要填好寄件人和收件人地址，之后送到快递公司即可，但包裹是否正确送达、是否损坏我们无法得知，也无法保证。UDP 协议也是如此，它只管把数据包发送到网络，然后就不管了，如果数据丢失或损坏，发送端是无法知道的，当然也不会重发。

既然如此，TCP 应该是更加优质的传输协议吧？

如果只考虑可靠性，TCP 的确比 UDP 好。但 UDP 在结构上比 TCP 更加简洁，不会发送 ACK 的应答消息，也不会给数据包分配 Seq 序号，所以 UDP 的传输效率有时会比 TCP 高出很多，编程中实现 UDP 也比 TCP 简单。

UDP 的可靠性虽然比不上TCP，但也不会像想象中那么频繁地发生数据损毁，在更加重视传输效率而非可靠性的情况下，UDP 是一种很好的选择。比如视频通信或音频通信，就非常适合采用 UDP 协议；通信时数据必须高效传输才不会产生“卡顿”现象，用户体验才更加流畅，如果丢失几个数据包，视频画面可能会出现“雪花”，音频可能会夹带一些杂音，这些都是无妨的。

与 UDP 相比，TCP 的生命在于流控制，这保证了数据传输的正确性。

### 4. Socket（套接字）

#### 【1】socket 概念

socket 的原意是“插座”，在计算机通信领域，它是计算机之间进行通信的一种约定或一种方式。通过 socket 这种约定，一台计算机可以接收其他计算机的数据，也可以向其他计算机发送数据。 我们把插头插到插座上就能从电网获得电力供应，同样，为了与远程计算机进行数据传输，需要连接到因特网，而 socket 就是用来连接到因特网的工具。

![socket](./assets/socket1625716026714-1337664.png)

**socket**是在应用层与传输层之间的一个抽象层，它的本质是编程接口，通过socket，才能实现TCP/IP协议。它就是一个底层套件，用来处理最底层消息的接受和发送。

#### 【2】套接字的类型

根据数据的传输方式，可以将 Internet 套接字分成两种类型。通过 socket() 函数创建连接时，必须告诉它使用哪种数据传输方式。

##### （1）流格式套接字（SOCK_STREAM）

流格式套接字（Stream Sockets）也叫“面向连接的套接字”，在代码中使用 SOCK_STREAM 表示。SOCK_STREAM 是一种可靠的、双向的通信数据流，数据可以准确无误地到达另一台计算机，如果损坏或丢失，可以重新发送。

SOCK_STREAM 有以下几个特征：

- 数据在传输过程中不会消失；
- 数据是按照顺序传输的；
- 数据的发送和接收不是同步的（有的教程也称“不存在数据边界”）。

可以将 SOCK_STREAM 比喻成一条传送带，只要传送带本身没有问题（不会断网），就能保证数据不丢失；同时，较晚传送的数据不会先到达，较早传送的数据不会晚到达，这就保证了数据是按照顺序传递的。

![将面向连接的套接字比喻成传送带](./assets/1-1Z1232154153L-1861472.gif)



为什么流格式套接字可以达到高质量的数据传输呢？这是因为它使用了 TCP 协议（The Transmission Control Protocol，传输控制协议），TCP 协议会控制你的数据按照顺序到达并且没有错误。

你也许见过 TCP，是因为你经常听说“TCP/IP”。TCP 用来确保数据的正确性，IP（Internet Protocol，网络协议）用来控制数据如何从源头到达目的地，也就是常说的“路由”。

那么，“数据的发送和接收不同步”该如何理解呢？

假设传送带传送的是水果，接收者需要凑齐 100 个后才能装袋，但是传送带可能把这 100 个水果分批传送，比如第一批传送 20 个，第二批传送 50 个，第三批传送 30 个。接收者不需要和传送带保持同步，只要根据自己的节奏来装袋即可，不用管传送带传送了几批，也不用每到一批就装袋一次，可以等到凑够了 100 个水果再装袋。

流格式套接字的内部有一个缓冲区（也就是字符数组），通过 socket 传输的数据将保存到这个缓冲区。接收端在收到数据后并不一定立即读取，只要数据不超过缓冲区的容量，接收端有可能在缓冲区被填满以后一次性地读取，也可能分成好几次读取。

也就是说，不管数据分几次传送过来，接收端只需要根据自己的要求读取，不用非得在数据到达时立即读取。传送端有自己的节奏，接收端也有自己的节奏，它们是不一致的。

##### （2）数据报套接字（SOCK_DGRAM）

数据报格式套接字（Datagram Sockets）也叫“无连接的套接字”，在代码中使用 SOCK_DGRAM 表示。

计算机只管传输数据，不作数据校验，如果数据在传输中损坏，或者没有到达另一台计算机，是没有办法补救的。也就是说，数据错了就错了，无法重传。

因为数据报套接字所做的校验工作少，所以在传输效率方面比流格式套接字要高。

可以将 SOCK_DGRAM 比喻成高速移动的摩托车快递，它有以下特征：

- 强调快速传输而非传输顺序；
- 传输的数据可能丢失也可能损毁；
- 限制每次传输的数据大小；
- 数据的发送和接收是同步的（有的教程也称“存在数据边界”）。

众所周知，速度是快递行业的生命。用摩托车发往同一地点的两件包裹无需保证顺序，只要以最快的速度交给客户就行。这种方式存在损坏或丢失的风险，而且包裹大小有一定限制。因此，想要传递大量包裹，就得分配发送。



![将无连接套接字比喻成摩托车快递](./assets/1-1Z123222015527.gif)

另外，用两辆摩托车分别发送两件包裹，那么接收者也需要分两次接收，所以“数据的发送和接收是同步的”；换句话说，接收次数应该和发送次数相同。

总之，数据报套接字是一种不可靠的、不按顺序传递的、以追求速度为目的的套接字。

数据报套接字也使用 IP 协议作路由，但是它不使用 TCP 协议，而是使用 UDP 协议（User Datagram Protocol，用户数据报协议）。

QQ 视频聊天和语音聊天就使用 SOCK_DGRAM 来传输数据，因为首先要保证通信的效率，尽量减小延迟，而数据的正确性是次要的，即使丢失很小的一部分数据，视频和音频也可以正常解析，最多出现噪点或杂音，不会对通信质量有实质的影响。

> 注意：SOCK_DGRAM 没有想象中的糟糕，不会频繁的丢失数据，数据错误只是小概率事件。

#### 【3】基于套接字的网络编程

**socket**翻译为套接字，可以把TCP/IP复杂的操作抽象为简单的几个接口来供应用层调用来实现进程在网络中的通信。**socket**起源于Unix，而Unix的基本要素之一就是“一切都为文件”，即可以通过打开——读写——关闭的模式来操作，通过这一点我们就可以来实现socket的简单编写

![img](./assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGFyaXNfMTE5,size_16,color_FFFFFF,t_70-1342446.png)

##### （1）服务端

```python
import socket
from loguru import logger

# (1) 构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 服务端三件套：bind listen accept
sock.bind(("127.0.0.1", 8899))
sock.listen(5)
logger.info("服务器启动")
while 1:
    logger.info("等待新连接...")
    conn, addr = sock.accept()  # 阻塞函数
    # print(f"conn：{conn}，addr：{addr}")
    logger.info(f"来自于客户端{addr}的请求成功")

    while 1:
        # (3) 收消息
        data_bytes = conn.recv(1024)  # 阻塞函数
        print("data:", data_bytes.decode())

        if data_bytes == "quit".encode() or len(data_bytes) == 0:
            logger.info(f"来自于{addr}客户端退出！")
            break

        # (4) 处理数据并发送
        data = data_bytes.decode()
        res = data.upper()
        conn.send(res.encode())
```

##### （2）客户端

```PYTHON
import socket

# (1) 构建客户端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 连接服务器
sock.connect(("127.0.0.1", 8899))

while 1:
    name = input("请输入转换的姓名(英文):")

    # (3) 发消息: 网络传输的数据一定是字节串
    sock.send(name.encode())

    #  # 客户端退出
    if name == "quit":
        break

    # (4) 接受来自于服务的响应消息
    res = sock.recv(1024)

    print("来自于服务的响应消息：", res.decode())

```

### 5. 案例练习

#### 【1】模拟SSH实现

实现了一个基本的命令执行系统，允许客户端向服务器发送命令并获取执行结果。服务器接收到客户端的命令后，使用`subprocess.getoutput()`执行命令，并将结果发送回客户端。客户端接收服务器返回的结果并进行处理。

##### （1）服务端

```python
import socket
import subprocess
import time
import struct

sock = socket.socket()
sock.bind(("127.0.0.1", 6666))
sock.listen(5)

while 1:
    conn, addr = sock.accept()
    print("客户端%s建立连接" % str(addr))
    while 1:

        cmd = conn.recv(1024)  # data字节串
        if not cmd:
            print(f"{conn.getpeername()}客户端退出")
            break
        print("执行命令：", cmd.decode("gbk"))

        # 版本1
        cmd_ret_bytes = subprocess.getoutput(cmd).encode()
        conn.send(cmd_ret_bytes)

        # 版本2
        cmd_ret_bytes = subprocess.getoutput(cmd).encode()
        print("响应字节数", len(cmd_ret_bytes))
        cmd_res_bytes_len = str(len(cmd_ret_bytes)).encode()
        conn.send(cmd_res_bytes_len)
        conn.send(cmd_res_bytes)
 
```

##### （2）客户端

```python
import socket
import time

ip_port = ("127.0.0.1", 6666)
sk = socket.socket()
sk.connect(ip_port)

while 1:
    data = input("输入执行命令>>>")
    sk.send(data.encode())

    # 版本1 
    res = sk.recv(1024)
    print("字节长度：", len(res))
    print("执行命令结果:%s" % (res.decode()))

    # 版本2 
    cmd_ret_bytes_len = sk.recv(1024)
    cmd_res_len = int(cmd_ret_bytes_len.decode())
    recv_num = 0
    while recv_num < cmd_res_len:
        data = sk.recv(1024)
        print(data.decode())
        recv_num += len(data)
    print("data的长度", recv_num, cmd_res_len)

```

#### 【2】粘包现象

粘包（Packet Congestion）是计算机网络中的一个常见问题，粘包问题通常出现在使用面向连接的传输协议（如TCP）进行数据传输时，这是因为TCP是基于字节流的，它并不了解应用层数据包的具体边界。当发送端迅速发送多个数据包时，底层网络协议栈可能会将这些数据包合并成一个较大的数据块进行发送。同样地，在接收端，网络协议栈也可能将接收到的数据块合并成一个较大的数据块，然后交给应用层处理。

粘包问题可能导致数据处理的困难和不准确性。例如，在一个基于文本的协议中，接收方可能需要将接收到的数据进行分割，以便逐个处理每个完整的消息。如果数据包粘连在一起，接收方就需要额外的处理来确定消息的边界，这增加了复杂性。

`demo演示`

```python
# 服务端

import socket
import time

s = socket.socket()
s.bind(("127.0.0.1",8888))
s.listen(5)

client,addr = s.accept()
time.sleep(10)
data = client.recv(1024)
print(data)

client.send(data)


# 客户端
import socket

s = socket.socket()
s.connect(("127.0.0.1",8888))

data = input(">>>")

s.send(data.encode())
s.send(data.encode())
s.send(data.encode())

res = s.recv(1024)
print(res)
```

`解决SSH案例的粘包`

服务端

```python
import socket
import subprocess
import time
import struct

sock = socket.socket()
sock.bind(("127.0.0.1", 6666))
sock.listen(5)

while 1:
    conn, addr = sock.accept()
    print("客户端%s建立连接" % str(addr))
    while 1:

        cmd = conn.recv(1024)  # data字节串
        if not cmd:
            print(f"{conn.getpeername()}客户端退出")
            break
        print("执行命令：", cmd.decode("gbk"))

        # 版本3：粘包解决方案

        result_str = subprocess.getoutput(cmd.decode("gbk"))
        result_bytes = bytes(result_str, encoding='utf8')
        res_len = struct.pack('i', len(result_bytes))
        print("res_len:", res_len)
        conn.sendall(res_len)
        conn.sendall(result_bytes)

```

客户端

```python
import socket
import time
import struct

ip_port = ("127.0.0.1", 6666)
sk = socket.socket()
sk.connect(ip_port)

while 1:
    data = input("输入执行命令>>>")
    sk.send(data.encode())

    # 版本3：粘包解决方案
    time.sleep(5)
    length_msg = sk.recv(4)
    length = struct.unpack('i', length_msg)[0] 
    recv_num = 0
    while recv_num < length:
         data = sk.recv(1024)
         print(data.decode())
         recv_num += len(data)
    
    print("data的长度", recv_num, length)

```

#### 【3】上传文件

客户端：

```python
import socket
import os
import json

# (1) 构建套接字对象，确定通信协议
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_port = ("127.0.0.1", 5566)
sock.connect(ip_port)

while 1:
    # 客户端给服务端发送消息
    params = input("请输入命令(比如上传文件put 文件路径):")
    cmd, local_path = params.split(" ")
    # (1) 将文件信息传给服务端
    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)
    file_params = {"file_name": file_name, "file_size": file_size}

    sock.send(json.dumps(file_params).encode())

    # (2) 循环读取文件，传给server端
    with open(local_path, "rb") as f:
        for line in f:
            sock.send(line)

    print("文件发送完毕")

```

服务端：

```python
import socket
import json

# (1) 构建套接字对象，确定通信协议
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 绑定IP和端口
ip_port = ("127.0.0.1", 5566)
sock.bind(ip_port)
# (3) 监听最大排队数
sock.listen(2)
# (4) 阻塞等待客户端连接
while 1:
    print("server is waiting...")
    conn, addr = sock.accept()
    while 1:
        #  接受来自客户端的文件信息
        data_json = conn.recv(1024)  # recv是一个阻塞函数
        file_params = json.loads(data_json.decode())
        print("file_params:", file_params)
        file_size = file_params["file_size"]
        file_name = file_params["file_name"]

        # 将接收到的文件数据一行行写入到新文件中
        receive_data_len = 0
        with open("imgs/" + file_name, "wb") as f:

            while receive_data_len < file_size:
                temp = conn.recv(1024)
                f.write(temp)
                receive_data_len += len(temp)

        print("文件上传成功")
```

### 今日作业

FTP功能实现

* 解决粘包问题
* 实现文件上传与下载

## Day14：并发编程

![截屏2024-03-31 14.25.21](./assets/%E6%88%AA%E5%B1%8F2024-03-31%2014.25.21-1866389.png)

并发编程是一种编程模式，旨在使程序能够同时执行多个任务或操作。它涉及到同时处理多个独立任务的能力，这些任务可以在同一时间段内或者在不同的时间段内并行执行。

在传统的单线程编程模型中，程序按照顺序依次执行指令，每个操作都必须在上一个操作完成后才能开始。这种模型的缺点是，在处理耗时的操作时，程序可能会出现停顿或阻塞，导致执行效率低下。

并发编程通过引入多个执行线程或进程，使得程序能够并行执行多个任务，从而提高系统的吞吐量和响应性能。每个线程或进程可以独立地执行任务，它们之间可以交替执行，或者同时执行不同的任务。这种并行执行的方式可以充分利用多核处理器的优势，同时还可以提升对输入/输出等耗时操作的处理效率。

总之，并发编程是一种利用多线程或多进程实现并行执行的编程模式，它可以提高程序的性能和响应性，并充分利用多核处理器的潜力。然而，并发编程也带来了一些挑战，如资源竞争和数据同步，需要合理地设计和管理以确保程序的正确性和可靠性。

### 1、进程、线程与协程

#### 【1】进程概念

我们都知道计算机的核心是CPU，它承担了所有的计算任务；而操作系统是计算机的管理者，它负责任务的调度、资源的分配和管理，统领整个计算机硬件；应用程序则是具有某种功能的程序，程序是运行于操作系统之上的。

> 进程是一个具有一定独立功能的程序在一个数据集上的一次动态执行的**过程**，是操作系统进行资源分配和调度的一个独立单位，是应用程序运行的载体。

多道技术：空间复用+时间复用，于是有了多进程！

进程是一种抽象的概念，从来没有统一的标准定义。进程一般由程序、数据集合和进程控制块三部分组成。

````
例子：我和我的女朋友们的故事

我就是CPU，我跟三个女朋友玩就是三个任务

1. 我教第一个女朋友做菜，菜谱就是程序，食材就是数据，我做饭的过程就是一个进程（切换，状态保存）

2. 我给第二个女朋友治疗脚伤，医疗手册就是程序，医药箱就是数据，治疗脚伤的过程就是第二个进程

。。。

````

[进程](https://baike.baidu.com/item/进程/382503?fromModule=lemma_inlink)状态反映进程执行过程的变化。这些状态随着进程的执行和外界条件的变化而转换。在三态模型中，进程状态分为三个基本状态，即运行态，就绪态，阻塞态。在五态模型中，进程分为[新建](https://baike.baidu.com/item/新建/6015276?fromModule=lemma_inlink)态、终止态，运行态，就绪态，阻塞态。

![img](./assets/u=3524969454,1048049783&fm=253&fmt=auto&app=138&f=JPEG-8788665.jpeg)

#### 【2】线程的概念

在早期的操作系统中并没有线程的概念，进程是能拥有资源和独立运行的最小单位，也是程序执行的最小单位。任务调度采用的是时间片轮转的抢占式调度方式，而进程是任务调度的最小单位，每个进程有各自独立的一块内存，使得各个进程之间内存地址相互隔离。后来，随着计算机的发展，对CPU的要求越来越高，进程之间的切换开销较大，已经无法满足越来越复杂的程序的要求了。于是就发明了线程。

线程是程序执行中一个单一的顺序控制流程，是程序执行流的最小单元，是处理器调度和分派的基本单位。

一个进程可以有一个或多个线程，各个线程之间共享程序的内存空间(也就是所在进程的内存空间)。一个标准的线程由线程ID、当前指令指针(PC)、寄存器和堆栈组成。而进程由内存空间(代码、数据、进程空间、打开的文件)和一个或多个线程组成。

##### 线程的生命周期

在单个处理器运行多个线程时，并发是一种模拟出来的状态。操作系统采用时间片轮转的方式轮流执行每一个线程。现在，几乎所有的现代操作系统采用的都是时间片轮转的抢占式调度方式，如我们熟悉的Unix、Linux、Windows及macOS等流行的操作系统。

我们知道线程是程序执行的最小单位，也是任务执行的最小单位。在早期只有进程的操作系统中，进程有五种状态，创建、就绪、运行、阻塞(等待)、退出。早期的进程相当于现在的只有单个线程的进程，那么现在的多线程也有五种状态，现在的多线程的生命周期与早期进程的生命周期类似。

![](./assets/%E5%B9%B6%E5%8F%917.png)

```python 
线程的生命周期

# 创建：一个新的线程被创建，等待该线程被调用执行；
# 就绪：时间片已用完，此线程被强制暂停，等待下一个属于它的时间片到来；
# 运行：此线程正在执行，正在占用时间片；
# 阻塞：也叫等待状态，等待某一事件(如IO或另一个线程)执行完；
# 退出：一个线程完成任务或者其他终止条件发生，该线程终止进入退出状态，退出状态释放该线程所分配的资源。
```

##### 进程与线程的区别

前面讲了进程与线程，但可能你还觉得迷糊，感觉他们很类似。的确，进程与线程有着千丝万缕的关系，下面就让我们一起来理一理：

> 1. 线程是程序执行的最小单位，而进程是操作系统分配资源的最小单位；
> 2. 一个进程由一个或多个线程组成，线程是一个进程中代码的不同执行路线；
> 3. 进程之间相互独立，但同一进程下的各个线程之间共享程序的内存空间(包括代码段、数据集、堆等)及一些进程级的资源(如打开文件和信号)，某进程内的线程在其它进程不可见；
> 4. 调度和切换：线程上下文切换比进程上下文切换要快得多。

#### 【3】协程(Coroutines)

协程，英文Coroutines，是一种基于线程之上，但又比线程更加轻量级的存在，这种由程序员自己写程序来管理的轻量级线程叫做『用户空间线程』，具有对内核来说不可见的特性。因为是自主开辟的异步任务，所以很多人也更喜欢叫它们纤程（`Fiber`），或者绿色线程（`GreenThread`）。正如一个进程可以拥有多个线程一样，一个线程也可以拥有多个协程。

> 协程解决的是线程的切换开销和内存开销的问题

将多个用户级线程映射到一个内核级线程，线程管理在用户空间完成。此模式中，用户级线程对操作系统不可见（即透明）。

![Snipaste_2024-04-06_20-40-38](./assets/Snipaste_2024-04-06_20-40-38-2407266.jpg)

优点： 这种模型的好处是线程上下文切换都发生在用户空间，避免的模态切换（mode switch），从而对于性能有积极的影响。

### 2、多线程实现

#### 【1】threading模块

Python提供两个模块进行多线程的操作，分别是`thread`和`threading`，前者是比较低级的模块，用于更底层的操作，一般应用级别的开发不常用。

````python
import time


def spider01():
    print("spider01 start")
    time.sleep(3)
    print("spider01 end")


def spider02():
    print("spider02 start")
    time.sleep(5)
    print("spider02 end")
    
    
spider01()
spider02()
````

多线程并发版本

```python
import threading
import time

def spider01(timer):
    print("spider01 start")
    time.sleep(timer)  # 模拟IO
    print("spider01 end")


def spider02(timer):
    print("spider02 start")
    time.sleep(timer)  # 模拟IO
    print("spider02 end")


start = time.time()

# 创建线程对象

t1 = threading.Thread(target=spider01, args=(3,))
t1.start()
t2 = threading.Thread(target=spider02, args=(5,))
t2.start()

t1.join()
t2.join()
end = time.time()
print("时间花销:", end - start)
```

#### 【2】线程应用案例

![截屏2024-04-06 22.48.06](./assets/%E6%88%AA%E5%B1%8F2024-04-06%2022.48.06.png)

```python
import threading

import requests
import re


def get_one_img(path, n):
    domain = "https://pic.netbian.com/"
    url = domain + path
    res = requests.get(url)
    f = open(f"./imgs/{n}.jpg", "wb")
    f.write(res.content)
    f.close()

    print(f"{n}下载成功")


n = 1
for page in range(2, 11):
    res = requests.get(f"https://pic.netbian.com/4kmeinv/index_{page}.html")
    # print(res.text)

    ret = re.findall('<img src="(/uploads/allimg/.*?)"', res.text)
    print(ret)

    for path in ret:
        t = threading.Thread(target=get_one_img, args=(path, n))
        t.start()
        n += 1

```

#### 【3】线程池

系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。在这种情形下，使用线程池可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程时，更应该考虑使用线程池。

线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它。当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。

此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，会导致系统性能急剧下降，甚至导致解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。

```python
import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    print(f'任务{i}开始！')
    time.sleep(i)
    print(f'任务{i}结束！')
    return i


start = time.time()
pool = ThreadPoolExecutor(3)

future01 = pool.submit(task, 1)
# print("future01是否结束", future01.done())
# print("future01的结果", future01.result())  # 同步等待
future02 = pool.submit(task, 2)
future03 = pool.submit(task, 3)
pool.shutdown()  # 阻塞等待
print(f"程序耗时{time.time() - start}秒钟")

print("future01的结果", future01.result())
print("future02的结果", future02.result())
print("future03的结果", future03.result())
```

> 使用线程池来执行线程任务的步骤如下：
>
> 1. 调用 ThreadPoolExecutor 类的构造器创建一个线程池。
> 2. 定义一个普通函数作为线程任务。
> 3. 调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务。
> 4. 当不想提交任何任务时，调用 ThreadPoolExecutor 对象的 shutdown() 方法来关闭线程池。

#### 【4】互斥锁

并发编程中需要解决一些常见的问题，例如资源竞争和数据同步。由于多个线程或进程可以同时访问共享的资源，因此可能会导致数据不一致或错误的结果。为了避免这种情况，需要采用合适的同步机制，如互斥锁、信号量或条件变量，来确保对共享资源的访问是同步和有序的。

````python
import time
import threading

Lock = threading.Lock()


def addNum():
    global num  # 在每个线程中都获取这个全局变量

    # 上锁
    Lock.acquire()
    t = num - 1
    time.sleep(0.0001)
    num = t
    Lock.release()
    # 放锁


num = 100  # 设定一个共享变量

thread_list = []

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('Result: ', num)

````

#### 【5】线程队列

##### （1）队列的基本语法

线程队列是一种线程安全的数据结构，用于在线程之间传递和共享数据。它提供了一种解耦的方式，使生产者线程能够将数据放入队列，而消费者线程可以从队列中获取数据进行处理，从而实现线程之间的通信和协调。

线程队列的主要目的是解决多线程环境下的数据共享和同步问题。在多线程编程中，如果多个线程同时访问共享资源，可能会导致数据的不一致性和竞争条件。通过使用线程队列，可以避免直接访问共享资源，而是通过队列来传递数据，从而保证线程安全。

```python
import queue

# 创建一个空的队列
# q = queue.Queue()

# 创建具有固定大小的队列
q = queue.Queue(3)

q.put(100)  # 将元素item放入队列
q.put(200)
q.put(300)
# q.put(400)

print(q.get())
print(q.get())
print(q.get())
# print(q.empty()) # 如果队列为空，返回True；否则返回False
# print(q.qsize())  # 返回队列中的元素个数
# print(q.get())
```

线程队列还提供了一些特性和机制，如阻塞和超时等待。当队列为空时，消费者线程可以选择阻塞等待新的数据被放入队列，并且可以设置超时时间。这样可以避免消费者线程空转浪费资源，只有在有新的数据可用时才会继续执行。

##### （2）生产者-消费者模型

常见的线程队列模型是生产者-消费者模型。生产者线程负责生成数据并将其放入队列，而消费者线程则从队列中获取数据并进行处理。通过使用队列作为缓冲区，生产者和消费者之间解耦，可以实现高效的线程间通信。

案例1

```python
import queue
import time
import threading

q = queue.Queue()


def producer():
    for i in range(1, 11):
        time.sleep(1)
        q.put(i)
        print(f"生产者生产数据{i}")

    print("生产者结束")


def consumer():
    while 1:
        val = q.get()
        print("消费者消费数据:", val)

        if val == 10:
            print("消费者结束")
            break


p = threading.Thread(target=producer)
p.start()
time.sleep(1)
c = threading.Thread(target=consumer)
c.start()
```

案例2:

```python
import queue
import time
import threading

q = queue.Queue()


def producer():
    for i in range(1, 11):
        time.sleep(3)
        q.put(i)
        print(f"生产者生产数据{i}")

    print("生产者结束")


def consumer(name):
    while 1:
        val = q.get()
        print(f"消费者{name}消费数据:{val}")

        time.sleep(6)

        if val == 10:
            print("消费者结束")
            break


p = threading.Thread(target=producer)
p.start()
time.sleep(1)
c1 = threading.Thread(target=consumer, args=("消费线程1",))
c1.start()
c2 = threading.Thread(target=consumer, args=("消费线程2",))
c2.start()

```

总而言之，线程队列是一种重要的多线程编程工具，用于实现线程安全的数据传递和同步。它提供了一种简单而高效的方式，让多个线程能够安全地共享和处理数据，从而提高程序的并发性和可靠性。

### 3、多进程实现

由于GIL的存在，python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。

multiprocessing包是Python中的多进程管理包。与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。该进程可以运行在Python程序内部编写的函数。该Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，其用法与threading包中的同名类一致。所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。

python的进程调用:

```python
import multiprocessing
import time


def foo():
    print("foo start...")
    time.sleep(5)
    print("foo end...")


def bar():
    print("bar start...")
    time.sleep(3)
    print("bar end...")


if __name__ == '__main__':
  
    start = time.time()
    t1 = multiprocessing.Process(target=foo, args=())
    t1.start()
    t2 = multiprocessing.Process(target=bar, args=())
    t2.start()

    # 等待所有子线程结束
    t1.join()  # 等待子线程t1
    t2.join()  # 等待子线程t2
    end = time.time()
    print(end - start)

```

案例：

```python
import multiprocessing
import threading
import time

def foo(x):
    ret = 1
    for i in range(x):
        ret += i
    print(ret)


start = time.time()
# (1) 串行版本
# foo(120000000)
# foo(120000000)
# foo(120000000)

# (2) 多线程版本
# t1 = threading.Thread(target=foo, args=(120000000,))
# t1.start()
# t2 = threading.Thread(target=foo, args=(120000000,))
# t2.start()
# t3 = threading.Thread(target=foo, args=(120000000,))
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()

# end = time.time()
# print(end - start)

# (3) 多进程版本
if __name__ == '__main__':

    p1 = multiprocessing.Process(target=foo, args=(120000000,))
    p1.start()
    p2 = multiprocessing.Process(target=foo, args=(120000000,))
    p2.start()
    p3 = multiprocessing.Process(target=foo, args=(120000000,))
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.time()
    print(end - start)

```

这个程序展示了三种不同的执行方式：串行版本、多线程版本和多进程版本，并统计了它们的执行时间。

1. 串行版本：
   - 在串行版本中，`foo(120000000)`被连续调用了三次，以便计算累加和。
   - 这种方式是单线程执行的，每个调用都会阻塞其他调用的执行，直到计算完成并打印结果。
   - 执行时间是三次调用的总和。
2. 多线程版本：
   - 在多线程版本中，使用了三个线程并发执行三次调用：`t1 = threading.Thread(target=foo, args=(120000000,))`。
   - 每个线程独立执行一次计算，并打印结果。
   - 由于全局解释器锁（GIL）的存在，多线程并不能真正实现并行计算，因此在CPU密集型任务上可能无法获得明显的性能提升。
   - 执行时间是最长的单个线程的执行时间。
3. 多进程版本：
   - 在多进程版本中，使用了三个进程并发执行三次调用：`p1 = multiprocessing.Process(target=foo, args=(120000000,))`。
   - 每个进程独立执行一次计算，并打印结果。
   - 多进程可以实现真正的并行计算，每个进程都在独立的Python解释器中运行，不受GIL的限制。
   - 执行时间是最长的单个进程的执行时间。

### 4、协程并发

协程，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：协程是一种用户态的轻量级线程。

协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。因此：

协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态，换种说法：进入上一次离开时所处逻辑流的位置。

#### 【1】Greenlet库

Greenlet是对Python标准库中的yield关键字进行封装的库。它允许我们在协程中使用yield语句来暂停和恢复执行，从而实现协程的功能。

在Greenlet中，协程被称为greenlet对象。我们可以创建一个greenlet对象，并使用它的switch方法来切换协程的执行。当一个协程暂停时，它的状态会被保存下来，可以在需要时恢复执行。

```python
from greenlet import greenlet


def foo():
    print("foo step1")  # 第1步：输出 foo step1
    gr_bar.switch()  # 第3步：切换到 bar 函数
    print("foo step2")  # 第6步：输出 foo step2
    gr_bar.switch()  # 第7步：切换到 bar 函数，从上一次执行的位置继续向后执行


def bar():
    print("bar step1")  # 第4步：输出 bar step1
    gr_foo.switch()  # 第5步：切换到 foo 函数，从上一次执行的位置继续向后执行
    print("bar step2")  # 第8步：输出 bar step2


if __name__ == '__main__':
    gr_foo = greenlet(foo)
    gr_bar = greenlet(bar)
    gr_foo.switch()  # 第1步：去执行 foo 函数

# 注意：switch中也可以传递参数用于在切换执行时相互传递值。
```

Python Greenlet库提供了一种轻量级的协程实现方式，适合处理高并发和I/O密集型任务。其简单易用的API和良好的兼容性使其成为Python开发者的理想选择。

#### 【2】asyncio模块

asyncio即Asynchronous I/O是python一个用来处理并发(concurrent)事件的包，是很多python异步架构的基础，多用于处理高并发网络请求方面的问题。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法==async==和==await==，可以让coroutine的代码更简洁易读。

asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

asyncio 往往是构建 IO 密集型和高层级 **结构化** 网络代码的最佳选择。

##### （1）基本使用

```python
import asyncio
import time


async def task(i):
    print(f"task {i} start")
    await asyncio.sleep(1)
    print(f"task {i} end")


start = time.time()
# 创建事件循环对象
loop = asyncio.get_event_loop()
# 直接将协程对象加入时间循环中
tasks = [task(1), task(2)]
# asyncio.wait:将协程任务进行收集，功能类似后面的asyncio.gather
# run_until_complete阻塞调用，直到协程全部运行结束才返回
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()

print("cost timer:", end - start)

```

##### （2）任务对象

`task`: 任务,对**协程对象**的进一步封装,包含任务的各个状态;**asyncio.Task**是**Future**的一个子类，用于实现协作式多任务的库，且**Task**对象不能用户手动实例化，通过下面2个函数`loop.create_task() 或 asyncio.ensure_future()`创建。

```python
import asyncio, time

async def work(i, n):  # 使用async关键字定义异步函数
    print('任务{}等待: {}秒'.format(i, n))
    await asyncio.sleep(n)  # 休眠一段时间
    print('任务{}在{}秒后返回结束运行'.format(i, n))
    return i + n


start_time = time.time()  # 开始时间

tasks = [asyncio.ensure_future(work(1, 1)),
         asyncio.ensure_future(work(2, 2)),
         asyncio.ensure_future(work(3, 3))]
# tasks[1].add_done_callback()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print('运行时间: ', time.time() - start_time)
for task in tasks:
    print('任务执行结果: ', task.result())
```

##### （3）新版本语法支持

> `async.create_task()`创建task
> `async.gather()`获取返回值
>
> `async.run()` 运行协程

```python
# 用gather()收集返回值

import asyncio, time


async def work(i, n):  # 使用async关键字定义异步函数
    print('任务{}等待: {}秒'.format(i, n))
    await asyncio.sleep(n)  # 休眠一段时间
    print('任务{}在{}秒后返回结束运行'.format(i, n))
    return i + n


async def main():
    tasks = [asyncio.create_task(work(1, 1)),
             asyncio.create_task(work(2, 2)),
             asyncio.create_task(work(3, 3))]

    # 将task作为参数传入gather，等异步任务都结束后返回结果列表
    response = await asyncio.gather(tasks[0], tasks[1], tasks[2])
    print("异步任务结果：", response)


start_time = time.time()  # 开始时间

asyncio.run(main())

print('运行时间: ', time.time() - start_time)
```

#### 【3】基于协程的异步爬虫应用

![image-20240426154356544](./assets/image-20240426154356544-4117438.png)

##### （1）同步请求爬虫

```python
import os.path
import time
import requests
import re


def get_page_img_urls(page):
    # 获取页面内容
    res = requests.get(f"https://pic.netbian.com/4kmeinv/index_{page}.html")

    # 使用正则表达式提取图片URL
    ret = re.findall('<img src="(/uploads/allimg/.*?)"', res.text)

    print(ret)
    return ret


def download_one_img(url, n):
    # 下载单张图片
    res = requests.get(url)
    f = open(f"./imgs/{n}", "wb")
    f.write(res.content)
    f.close()
    print(f"{n}下载成功")


def download_page_imgs(img_urls):
    domain = "https://pic.netbian.com/"

    for path in img_urls:
        title = os.path.basename(path)
        url = domain + path
        download_one_img(url, title)


def main():
    start = time.time()
    for i in range(2, 6):
        page_img_urls = get_page_img_urls(i)
        # 获取页面中的图片URL列表
        download_page_imgs(page_img_urls)
    # 下载页面中的所有图片
    end = time.time()
    print("cost timer:", end - start)


main()
```

##### （2）基于asyncio库的异步爬虫

```python
import time
import requests
import re
import asyncio
import aiohttp
import os


async def get_page_img_urls(page):
    # 获取页面内容
    # res = requests.get(f"https://pic.netbian.com/4kmeinv/index_{2}.html")

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://pic.netbian.com/4kmeinv/index_{page}.html", verify_ssl=False) as res:
            data = await res.content.read()
            # 使用正则表达式提取图片URL
            ret = re.findall('<img src="(/uploads/allimg/.*?)"', data.decode("GBK"))
            print(ret)
            return ret


async def download_one_img(url, n):
    # 下载单张图片
    async with aiohttp.ClientSession() as session:
        async with session.get(url, verify_ssl=False) as res:
            f = open(f"./imgs/{n}", "wb")
            data = await res.content.read()
            f.write(data)
            f.close()
            print(f"{n}下载成功")


async def download_page_imgs(img_urls):
    domain = "https://pic.netbian.com/"

    for path in img_urls:
        title = os.path.basename(path)
        url = domain + path
        await download_one_img(url, title)


async def main():
    start = time.time()
    for i in range(2, 6):
        # 获取页面中的图片URL列表
        page_img_urls = await get_page_img_urls(i)
        # 下载页面中的所有图片
        await download_page_imgs(page_img_urls)
    end = time.time()
    print("cost timer:", end - start)


asyncio.run(main())
```

在这段代码中，`async with` 是用于创建一个异步上下文管理器，而不是用于等待异步操作的完成。异步上下文管理器可以在异步代码块中管理资源的获取和释放。

在这个例子中，`aiohttp.ClientSession()` 返回一个异步上下文管理器对象 `session`，它负责管理与服务器的连接和会话。使用 `async with` 可以确保在代码块执行完毕后，自动关闭和释放与服务器的连接。

在 `async with session.get(...)` 中，`session.get(...)` 返回一个异步上下文管理器对象 `response`，它负责发送 HTTP 请求并获取响应。在 `async with` 代码块内部，我们可以使用 `response` 对象进行响应的处理，例如读取响应的内容。

### 今日作业

#### 【1】多线程日志记录

需求：你需要设计一个多线程日志记录系统，用于记录系统的运行日志。系统有三个日志级别：**'INFO'**、**'WARNING'**和**'ERROR'**。每个级别的日志都应该以不同的时间间隔写入日志文件。具体要求如下：

1. 创建三个线程对象，分别表示'INFO'、'WARNING'和'ERROR'级别的日志线程。
2. 每个线程对象应该无限循环，在循环中以指定的时间间隔向日志文件写入相应级别的日志消息。
3. 'INFO'级别的日志线程每秒写入一条日志消息。
4. 'WARNING'级别的日志线程每三秒写入一条日志消息。
5. 'ERROR'级别的日志线程每五秒写入一条日志消息。
6. 日志消息的格式为：时间戳 - [级别]: 消息内容。

#### 【2】订单处理系统

1. 实现一个订单处理系统，其中包括生产者和消费者线程。
2. 生产者线程负责生成订单消息，并将其放入订单消息队列中。生成的订单消息应包括以下信息：
   - 订单号（唯一标识订单）
   - 顾客姓名
   - 订单总金额
3. 消费者线程负责从订单消息队列中获取订单消息，并进行处理。处理订单消息的具体操作是发送短信通知给顾客，通知顾客订单已支付成功，请耐心等待配送。发送短信通知时，应包括以下内容：
   - 顾客姓名
   - 订单号
4. 生产者线程和消费者线程应该并发执行，以实现订单的实时处理。
5. 订单消息的生成和发送短信通知的操作应具有随机性，以模拟实际应用中的不同订单和通知情况。例如，可以使用随机数生成订单号和随机选择顾客姓名和订单金额。
6. 程序应该持续运行，直到手动终止。生产者线程应不断生成订单消息并放入队列，而消费者线程应不断从队列中获取消息并处理。

#### 【3】异步操作数据库

将下面的案例数据库操作改为使用异步IO并发执行

```python
import time
def execute_query(query):
    # 模拟数据库查询，这里可以替换为实际的数据库查询操作
    # 这里使用time.sleep来模拟查询的阻塞操作
    import time
    time.sleep(1)
    return f"Result for query: {query}"


def main():
    queries = [
        "SELECT * FROM table1",
        "SELECT * FROM table2",
        "SELECT * FROM table3"
    ]

    results = []

    for query in queries:
        result = execute_query(query)
        results.append(result)

    print(results)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("cost timer:", end - start)
```

## 模块作业

### FTP扩展

![截屏2024-05-05 17.51.19](./assets/%E6%88%AA%E5%B1%8F2024-05-05%2017.51.19-4902689.png)

* 基于面向对象改版文件上传与下载
* 实现进度条显示功能
* 实现文件一致性校验（提示hashlib）
* 多客户端并发服务

