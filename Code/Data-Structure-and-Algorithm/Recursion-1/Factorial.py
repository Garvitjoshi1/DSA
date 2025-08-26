# recursive function:-
def fact(n):
    if n == 0:
        # is the provided base case to stop the recursion.
        return 1
    return n * fact(n - 1)


# given error without base case.

n = int(input())
print(fact(n))
