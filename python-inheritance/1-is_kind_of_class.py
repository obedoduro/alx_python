# finding out if same class or inherit 
# class has an object we know of
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)

# parent class
class A:
    pass

#inherit class
class B(A):
    pass

#a class
class C():
    pass

#objects assigned
obj1 = A()
obj2 = B()
obj3 = C()

a = 1
#output
# print(is_kind_of_class(obj1, A)) 
# print(is_kind_of_class(obj2, B)) 
# print(is_kind_of_class(obj2, A)) 
# print(is_kind_of_class(obj1, B)) 
# print(is_kind_of_class(obj3, A)) 
# print(is_kind_of_class(obj3, C))  