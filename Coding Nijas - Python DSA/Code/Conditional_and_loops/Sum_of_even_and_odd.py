## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
num = int(input())
even_sum = 0
odd_sum = 0
while num > 0:
    last = num % 10
    if last % 2 == 0:
        even_sum += last
    else:
        odd_sum += last
    num = num // 10
print(even_sum, " ", odd_sum)
