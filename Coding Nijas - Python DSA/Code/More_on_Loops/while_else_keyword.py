# while(condition):
#     //
#          code...
#               //
# else will execute only if in while loop :
#    1.Condition is false now
#    2.Or you have hit the break statement.

n = int(input())
for d in range(2, n, 1):
    if n % d == 0:
        break
# else will be executed if none of the value satisfy the if loop
else:
    print("Prime numbers")
