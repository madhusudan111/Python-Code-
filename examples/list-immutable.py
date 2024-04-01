# Lists are immutable
a = [5, 6, 7]
def sum(a):
    a.append(10)
    print ("printing inside the function",a)
sum(a)
print ("printing outside of function",a)