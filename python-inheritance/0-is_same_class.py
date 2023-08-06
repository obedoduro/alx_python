#checking instance of class
def is_same_class(obj, a_class):
   return type(obj) is a_class

# Classes 
class A:
    pass

class B(A):
    pass

obj1 = A()
obj2 = B()

print(is_same_class(obj1, A)) 
print(is_same_class(obj1, B))   
print(is_same_class(obj2, B))  
print(is_same_class(obj2, A))  

