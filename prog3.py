class Parent:
    def method1(self):
        print("This is parent class")


class Child(Parent):
    def method2(self):
        print("This is child class")


ob = Child()
ob.method2()
ob.method1()