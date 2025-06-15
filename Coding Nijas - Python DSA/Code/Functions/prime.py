def prime(n):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        return True
    return False


def is_prime(n):
    for k in range(2, n + 1):
        is_k_prime = prime(k)
        if is_k_prime:
            print(k)


print(is_prime(10))
