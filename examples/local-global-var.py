# local vs. global variable
a = 6
def sum(a):
    a = 10
    print ("printing inside the function",a)
print ("printing outside of function",a)
sum(a)