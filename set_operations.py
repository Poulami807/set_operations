a=set()
b=set()
a.update(list(map(int,input("Enter the elements of first set separated by space ").split(" "))))
b.update(list(map(int,input("Enter the elements of second set separated by space ").split(" "))))


print("Union of a and b is",a | b)
print("Intersection of a and b is",a & b)
print("Difference of a and b is",a - b)
print("Symmetric difference of a and b is",a^ b)

