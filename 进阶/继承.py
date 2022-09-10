class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('My name is', self.name)
        print('My age is', self.age)


class Teacher(Person):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def showSalary(self):
        print('My salary is', self.salary, end='\n\n')


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def showGrade(self):
        print('My grade is', self.grade, end='\n\n')


teacher = Teacher('tom', 30, 5000)
teacher.introduce()
teacher.showSalary()
student = Student('jerry', 10, 90)
student.introduce()
student.showGrade()


# 多继承
# 子类继承所有父类的属性和方法，从而实现代码重用

class Father:
    def __init__(self, father_attr):
        self.father_attr = father_attr

    def father_method(self):
        print('father_attr =', self.father_attr)


class Mother:
    def __init__(self, mother_attr):
        self.mother_attr = mother_attr

    def mother_method(self):
        print('mother_attr =', self.mother_attr)


class Child(Father, Mother):
    def __init__(self, father_attr, mother_attr, child_attr):
        Father.__init__(self, father_attr)
        Mother.__init__(self, mother_attr)
        self.child_attr = child_attr

    def child_method(self):
        print('child_attr =', self.child_attr)


child = Child('Father1', 'Mother1', 'Child1')
child.father_method()
child.mother_method()
child.child_method()
