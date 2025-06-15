def sum_n(n):
    # base case provided
    if n == 0:
        return 0
    # main function
    small_Output = sum_n(n - 1)
    Output = small_Output + n
    return Output


# function called
n = int(input())
print(sum_n(n))
