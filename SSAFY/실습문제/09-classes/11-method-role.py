class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) 
# ('instance method', <__main__.MyClass object at 0x000002B4E9478510>) 
print(MyClass.class_method())
# ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method())
# static method


# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())
