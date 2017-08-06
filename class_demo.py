_metaclass_ = type

class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)

print(MyClass.smeth())

myClass = MyClass()
print(myClass.cmeth())