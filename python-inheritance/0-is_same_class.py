#checking instance of object in each class
def is_same_class(obj, a_class):
#    print(".")
   return type(obj) is a_class

# Classes 
class A:
    pass

class B(A):
    pass

obj1 = A()
obj2 = B()

is_same_class(obj1, A)
a = 1
#print (  is_same_class(a, int))
