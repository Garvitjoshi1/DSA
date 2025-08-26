a = "red"
b = " bull"
print(a+b)
a = a + b + " green "
print(a)
a += a
print(a)
print(id(a))
# to print same thing multiple times
a = "blue "
print(a*3)
print(id(a))
a = a*2
print(id(a))
# a = "blue" +1 will give error
# for this you need to convert it.
a = a+str(3)
print(a)
