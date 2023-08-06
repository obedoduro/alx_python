#only sub class of a class
def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) != a_class

#parent class
class A:
    pass
#inherited directly
class B(A):
    pass
#inherited indirectly
class C(B):
    pass

#a class
class D():
    pass

#assign objects
obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()




print(" {}", None)
# print(inherits_from(obj2, B))
# print(inherits_from(obj3, A)) 
# print(inherits_from(obj3, B)) 
# print(inherits_from(obj4, D)) 
